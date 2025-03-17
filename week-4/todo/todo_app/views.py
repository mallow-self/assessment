from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Todo


# Create your views here.
def list_todo(request):
    """Render the to-do list page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered to-do list page.
    """
    return render(request, "todo_app/index.html")


def get_todos(request):
    """Fetch and return a list of to-do items in JSON format.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing a list of to-do items with
        their details such as ID, title, priority, due date, status, and timestamps.
    """
    todo_data = list(
        Todo.objects.all()
        .values(
            "todo_id",
            "title",
            "priority_level",
            "due_date",
            "status",
            "created_at",
            "updated_at",
        )
        .order_by("-created_at")
    )
    responseData = {"todo": todo_data}
    return JsonResponse(responseData)


def create_todo(request):
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
            title = request.POST.get("title")
            priority_level = request.POST.get("priority_level")
            due_date = request.POST.get("due_date")
            status = request.POST.get("status")

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


def create(request):
    """Render the to-do creation page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page for creating a new to-do item.
    """
    return render(request, "todo_app/create.html")


def delete_todo(request, todo_id):
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


def edit(request, todo_id):
    """Render the to-do edit page with existing details.

    This function retrieves a to-do item by its ID and prepares the context
    for rendering the edit page.

    Args:
        request (HttpRequest): The HTTP request object.
        todo_id (int): The ID of the to-do item to be edited.

    Returns:
        HttpResponse: The rendered HTML page with the to-do item's details.
    """
    todo = get_object_or_404(Todo, todo_id=todo_id)
    due_date_str = todo.due_date.strftime("%Y-%m-%d") if todo.due_date else ""
    context = {
        "todo_id": todo.todo_id,
        "title": todo.title,
        "priority_level": todo.priority_level,
        "due_date": due_date_str,
        "status": todo.status,
    }
    return render(request, "todo_app/edit.html", context)


def update_todo(request, todo_id):
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
            title = request.POST.get("title")
            priority_level = request.POST.get("priority_level")
            due_date = request.POST.get("due_date")
            status = request.POST.get("status")

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
