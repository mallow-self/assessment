from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpRequest, HttpResponseRedirect, HttpResponse
from .models import Todo
from .form import TodoForm
from typing import Dict, Any, Union, List
from asgiref.sync import sync_to_async

# Create your views here.


async def list_todo(request: HttpRequest) -> HttpRequest:
    """Render the to-do list page. Asynchronous doesn't have any real benefits, Just for future-proofing.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered to-do list page.
    """
    return render(request, "todo_app/index.html")

# def get_todos(request: HttpRequest) -> JsonResponse:
#     """Fetch and return a list of to-do items in JSON format.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         JsonResponse: A JSON response containing a list of to-do items with
#         their details such as ID, title, priority, due date, status, and timestamps.
#     """
#     try:
#         todo_data: list[Dict[str, Any]] = list(
#             Todo.objects.all().values(
#                 "todo_id",
#                 "title",
#                 "priority_level",
#                 "due_date",
#                 "status",
#                 "created_at",
#                 "updated_at",
#             )
#         )

#         priority_map: Dict[str:str] = {"low": "Low", "medium": "Medium", "high": "High"}
#         status_map: Dict[str:str] = {
#             "pending": "Pending",
#             "in-progress": "In Progress",
#             "completed": "Completed",
#             "overdue": "Overdue",
#         }
#         for todo in todo_data:
#             todo["priority_level"] = priority_map.get(todo.get("priority_level"), todo.get("priority_level"))
#             todo["status"] = status_map.get(todo.get("status"), todo.get("status"))

#         responseData: Dict[str, list[Dict[str, Any]]] = {"todo": todo_data}
#         return JsonResponse(responseData)
#     except Exception as e:
#         return JsonResponse({"Exception Occurred:":f"{e}"})


async def get_todos(request: HttpRequest) -> JsonResponse:
    """Asynchronously fetch and return a list of to-do items in JSON format.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of to-do items with
        their details such as ID, title, priority, due date, status, and timestamps.
    """
    try:
        # Fetch data asynchronously
        todo_data: List[Dict[str, Any]] = await sync_to_async(list)(
            Todo.objects.all().values(
                "todo_id",
                "title",
                "priority_level",
                "due_date",
                "status",
                "created_at",
                "updated_at",
            )
        )

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

        responseData: Dict[str, List[Dict[str, Any]]] = {"todo": todo_data}
        return JsonResponse(responseData)
    except Exception as e:
        return JsonResponse({"Exception Occurred": str(e)})


def create_todo(request: HttpRequest) -> JsonResponse | HttpResponseRedirect:
    """Handle the creation of a new to-do item.

    This function processes a POST request to create a new to-do item
    with the given title, priority level, due date, and status.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse or HttpResponseRedirect:
            - If successful, redirects to the to-do list page.
            - If fields are missing, returns a 400 JSON response.
            - If an error occurs, returns a JSON response with the error message.
            - If the request method is not POST, returns a 400 JSON response.
    """
    if request.method == "POST":
        try:
            title: str | None = request.POST.get("title")
            priority_level: str | None = request.POST.get("priority_level")
            due_date: str | None = request.POST.get("due_date")
            status: str | None = request.POST.get("status")

            if not all([title, priority_level, due_date, status]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            todo = Todo.objects.create(
                title=title,
                priority_level=priority_level,
                due_date=due_date,
                status=status,
            )

            return redirect("todo:list")

        except Exception as e:
            return JsonResponse({"server-error": f"{e}"})

    return JsonResponse({"error": "Invalid request"}, status=400)


def create(request: HttpRequest) -> HttpResponse:
    """Render the to-do creation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page for creating a new to-do item.
    """
    return render(request, "todo_app/create.html")


def delete_todo(request: HttpRequest, todo_id: int) -> JsonResponse:
    """Delete a specific to-do item.

    This function retrieves a to-do item by its ID and deletes it if the
    request method is POST.

    Args:
        request (HttpRequest): The HTTP request object.
        todo_id (int): The ID of the to-do item to be deleted.

    Returns:
        JsonResponse:
            - On success, returns a JSON response confirming deletion and prompting a reload.
            - On failure, returns a JSON response with an error message.
            - If the request method is not POST, returns a 400 JSON response.
    """
    todo = get_object_or_404(Todo, todo_id=todo_id)

    if request.method == "POST":
        try:
            todo.delete()
            return JsonResponse(
                {"message": "Todo deleted successfully", "reload": True}
            )
        except Exception as e:
            return JsonResponse({"server-error": f"{e}"})

    return JsonResponse({"error": "Invalid request"}, status=400)


def edit(request: HttpRequest, todo_id: int) -> HttpResponse | JsonResponse:
    """Render the to-do edit page with existing details.

    This function retrieves a to-do item by its ID and prepares the context
    for rendering the edit page.

    Args:
        request (HttpRequest): The HTTP request object.
        todo_id (int): The ID of the to-do item to be edited.

    Returns:
        HttpResponse: The rendered HTML page with the to-do item's details.
    """
    try:
        todo = get_object_or_404(Todo, todo_id=todo_id)
        due_date_str: str = todo.due_date.strftime(
            "%Y-%m-%d") if todo.due_date else ""
        context: Dict[str, Any] = {
            "todo_id": todo.todo_id,
            "title": todo.title,
            "priority_level": todo.priority_level,
            "due_date": due_date_str,
            "status": todo.status,
        }
        return render(request, "todo_app/edit.html", context)
    except Exception as e:
        return JsonResponse({"Exception Occurred:": f"{e}"})


def update_todo(request: HttpRequest, todo_id: int) -> Union[JsonResponse, HttpResponse]:
    """Update an existing to-do item.

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
    todo = get_object_or_404(Todo, todo_id=todo_id)

    if request.method == "POST":
        try:
            title: str = request.POST.get("title")
            priority_level: str = request.POST.get("priority_level")
            due_date: str = request.POST.get("due_date")
            status: str = request.POST.get("status")

            if not all([title, priority_level, due_date, status]):
                return JsonResponse({"error": "All fields are required"}, status=400)

            # Update the todo object
            todo.title = title
            todo.priority_level = priority_level
            todo.due_date = due_date
            todo.status = status
            todo.save()

            return redirect("todo:list")
        except Exception as e:
            return JsonResponse({"server-error": f"{e}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


async def todo_form(request: HttpRequest):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            await sync_to_async(form.save)()
            return JsonResponse({"message": "Successfully created form"})
        else:
            return JsonResponse({"message": "Invalid data", "errors": form.errors}, status=400)
    form = TodoForm()
    context = {"form": form}
    # Render asynchronously
    return await sync_to_async(render)(request, "todo_app/todoForm.html", context=context)

async def dfindex(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            await sync_to_async(form.save)()
            return JsonResponse({"message": "Successfully created form"})
        else:
            return JsonResponse({"message": "Invalid data", "errors": form.errors}, status=400)
    form = TodoForm()
    context = {"form": form}
    # Render asynchronously
    return await sync_to_async(render)(request, "todo_app/todo.html", context=context)