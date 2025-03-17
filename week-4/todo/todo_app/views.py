from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Todo

# Create your views here.
def list_todo(request):
    return render(request,"todo_app/index.html")

def get_todos(request):
    todo_data = list(Todo.objects.all().values(
            "todo_id",
            "title",
            "priority_level",
            "due_date",
            "status",
            "created_at",
            "updated_at",
        )
    )
    responseData = {"todo": todo_data}
    return JsonResponse(responseData)

def create_todo(request):
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
    return render(request,"todo_app/create.html")


def delete_todo(request, todo_id):
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


