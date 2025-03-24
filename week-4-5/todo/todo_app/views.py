from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from .form import TodoForm
from typing import Dict, Any, Union, List
from asgiref.sync import sync_to_async
from django.db.models import Q


async def index(request: HttpRequest) -> Union[JsonResponse, HttpResponse]:
    """Render the to-do list page and handle form submissions asynchronously.
    
    If a POST request is received with valid form data, a new to-do item is saved.
    Otherwise, an empty form is rendered.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        Union[JsonResponse, HttpResponse]: JSON response on error, otherwise renders the to-do page.
    """
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            await sync_to_async(form.save)()
            return redirect('todo:dfindex')
        else:
            return JsonResponse({"message": "Invalid data", "errors": form.errors}, status=400)

    form = TodoForm()
    context = {"form": form}
    return await sync_to_async(render)(request, "todo_app/todo.html", context=context)


async def get_todos(request: HttpRequest) -> JsonResponse:
    """Asynchronously fetch and return a list of to-do items in JSON format."""
    try:
        search: str = request.GET.get("search", "").strip()
        priority_filter: str = request.GET.get("filter", "").strip()

        filters = Q()
        if search:
            filters &= Q(title__icontains=search)
        if priority_filter:
            filters &= Q(priority_level=priority_filter)

        todo_data: List[Dict[str, Any]] = await sync_to_async(list)(
            Todo.objects.filter(filters).values(
                "todo_id", "title", "priority_level", "due_date", "status", "created_at", "updated_at"
            )
        )

        priority_map: Dict[str, str] = {
            "low": "Low", "medium": "Medium", "high": "High"}
        status_map: Dict[str, str] = {
            "pending": "Pending", "in-progress": "In Progress", "completed": "Completed", "overdue": "Overdue"
        }

        for todo in todo_data:
            todo["priority_level"] = priority_map.get(
                todo.get("priority_level"), todo.get("priority_level"))
            todo["status"] = status_map.get(
                todo.get("status"), todo.get("status"))

        return JsonResponse({"todo": todo_data})
    except Exception as e:
        return JsonResponse({"Exception Occurred": str(e)}, status=500)


async def delete_todo(request: HttpRequest, todo_id: int) -> JsonResponse:
    """Asynchronously delete a specific to-do item."""
    todo = await sync_to_async(get_object_or_404)(Todo, todo_id=todo_id)

    if request.method == "DELETE":
        try:
            await sync_to_async(todo.delete)()
            return JsonResponse({"message": "Todo deleted successfully", "reload": True})
        except Exception as e:
            return JsonResponse({"server-error": f"{e}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


async def update_todo(request: HttpRequest, todo_id: int) -> Union[JsonResponse, HttpResponse]:
    """Asynchronously update an existing to-do item."""
    todo = await sync_to_async(get_object_or_404)(Todo, todo_id=todo_id)

    if request.method == "POST":
        try:
            title: str = request.POST.get("title")
            priority_level: str = request.POST.get("priority_level")
            due_date: str = request.POST.get("due_date")
            status: str = request.POST.get("status")

            if not all([title, priority_level, due_date, status]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            todo.title = title
            todo.priority_level = priority_level
            todo.due_date = due_date
            todo.status = status
            await sync_to_async(todo.save)()

            return redirect("todo:dfindex")
        except Exception as e:
            return JsonResponse({"server-error": f"{e}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


async def get_todo_update(request: HttpRequest, todo_id: int) -> JsonResponse:
    """Asynchronously retrieve a specific to-do item and return its details as JSON."""
    todo = await sync_to_async(get_object_or_404)(Todo, pk=todo_id)

    return JsonResponse({
        "todo_id": todo.todo_id,
        "title": todo.title,
        "priority_level": todo.priority_level,
        "due_date": str(todo.due_date),
        "status": todo.status
    })
