from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpRequest, HttpResponseRedirect, HttpResponse
from .models import Todo
from .form import TodoForm
from typing import Dict, Any, Union, List
from asgiref.sync import sync_to_async
from django.db.models import Q


# Create your views here.
async def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            await sync_to_async(form.save)()
            return redirect('todo:dfindex')
        else:
            return JsonResponse({"message": "Invalid data", "errors": form.errors}, status=400)
    form = TodoForm()
    context = {"form": form}
    # Render asynchronously
    return await sync_to_async(render)(request, "todo_app/todo.html", context=context)


async def get_todos(request: HttpRequest) -> JsonResponse:
    """Asynchronously fetch and return a list of to-do items in JSON format."""
    try:
        search: str = request.GET.get("search", "").strip()
        priority_filter: str = request.GET.get("filter", "").strip()

        # Construct the filter condition
        filters = Q()
        if search:
            # Match title starting with search value
            filters &= Q(title__icontains=search)
        if priority_filter:
            # Match priority level
            filters &= Q(priority_level=priority_filter)

        # Fetch filtered data asynchronously
        todo_data: List[Dict[str, Any]] = await sync_to_async(list)(
            Todo.objects.filter(filters).values(
                "todo_id",
                "title",
                "priority_level",
                "due_date",
                "status",
                "created_at",
                "updated_at",
            )
        )

        # Mapping for priority and status labels
        priority_map: Dict[str, str] = {
            "low": "Low", "medium": "Medium", "high": "High"}
        status_map: Dict[str, str] = {
            "pending": "Pending",
            "in-progress": "In Progress",
            "completed": "Completed",
            "overdue": "Overdue",
        }

        # Modify data asynchronously
        for todo in todo_data:
            todo["priority_level"] = priority_map.get(
                todo.get("priority_level"), todo.get("priority_level"))
            todo["status"] = status_map.get(
                todo.get("status"), todo.get("status"))

        return JsonResponse({"todo": todo_data})

    except Exception as e:
        return JsonResponse({"Exception Occurred": str(e)}, status=500)


async def delete_todo(request: HttpRequest, todo_id: int) -> JsonResponse:
    """Asynchronously delete a specific to-do item.

    This function retrieves a to-do item by its ID and deletes it if the
    request method is DELETE.

    Args:
        request (HttpRequest): The HTTP request object.
        todo_id (int): The ID of the to-do item to be deleted.

    Returns:
        JsonResponse:
            - On success, returns a JSON response confirming deletion.
            - On failure, returns a JSON response with an error message.
            - If the request method is not DELETE, returns a 400 JSON response.
    """
    todo = await sync_to_async(get_object_or_404)(Todo, todo_id=todo_id)

    if request.method == "DELETE":
        try:
            await sync_to_async(todo.delete)()
            return JsonResponse(
                {"message": "Todo deleted successfully", "reload": True}
            )
        except Exception as e:
            return JsonResponse({"server-error": f"{e}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


async def update_todo(request: HttpRequest, todo_id: int) -> Union[JsonResponse, HttpResponse]:
    """Asynchronously update an existing to-do item.

    This function processes a POST request to update the details of a
    to-do item, including title, priority level, due date, and status.

    Args:
        request (HttpRequest): The HTTP request object.
        todo_id (int): The ID of the to-do item to be updated.

    Returns:
        JsonResponse or HttpResponseRedirect:
            - On success, redirects to the to-do list page.
            - If fields are missing, returns a 400 JSON response.
            - If an error occurs, returns a 500 JSON response with the error message.
            - If the request method is not POST, returns a 400 JSON response.
    """
    todo = await sync_to_async(get_object_or_404)(Todo, todo_id=todo_id)

    if request.method == "POST":
        try:
            title: str = request.POST.get("title")
            priority_level: str = request.POST.get("priority_level")
            due_date: str = request.POST.get("due_date")
            status: str = request.POST.get("status")

            if not all([title, priority_level, due_date, status]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            # Update the todo object asynchronously
            todo.title = title
            todo.priority_level = priority_level
            todo.due_date = due_date
            todo.status = status
            await sync_to_async(todo.save)()

            return redirect("todo:dfindex")
        except Exception as e:
            return JsonResponse({"server-error": f"{e}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


async def get_todo_update(request, todo_id):
    """Asynchronously retrieve a specific to-do item and return its details as JSON."""

    todo = await sync_to_async(get_object_or_404)(Todo, pk=todo_id)

    return JsonResponse({
        "todo_id": todo.todo_id,
        "title": todo.title,
        "priority_level": todo.priority_level,
        "due_date": str(todo.due_date),
        "status": todo.status
    })
