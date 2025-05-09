$(document).ready(function () {

    $("#todoForm").on("submit", function (event) {
        if (!validation()) {
            event.preventDefault(); // Prevent form submission
        }
    });
    // Fetch To-Do List from Backend
    function fetchTodos(search = "", filter = "") {
        $.ajax({
            url: `/todos?search=${search}&filter=${filter}`,
            method: "GET",
            dataType: "json",
            success: function (response) {
                let todoList = response.todo;
                let tableBody = "";
                let count=1;
                // Loop through each task and append to table
                todoList.forEach(todo => {
                    tableBody += `
                        <tr>
                            <td>${count}</td>
                            <td>${todo.title}</td>
                            <td>${todo.priority_level}</td>
                            <td>${todo.due_date}</td>
                            <td>${todo.status}</td>
                            <td>
                                <button class="btn btn-primary btn-sm update-btn" data-id="${todo.todo_id}">
                                    <svg width="15px" height="15px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M2.5 21.4998L8.04927 19.3655C8.40421 19.229 8.58168 19.1607 8.74772 19.0716C8.8952 18.9924 9.0358 18.901 9.16804 18.7984C9.31692 18.6829 9.45137 18.5484 9.72028 18.2795L21 6.99982C22.1046 5.89525 22.1046 4.10438 21 2.99981C19.8955 1.89525 18.1046 1.89524 17 2.99981L5.72028 14.2795C5.45138 14.5484 5.31692 14.6829 5.20139 14.8318C5.09877 14.964 5.0074 15.1046 4.92823 15.2521C4.83911 15.4181 4.77085 15.5956 4.63433 15.9506L2.5 21.4998ZM2.5 21.4998L4.55812 16.1488C4.7054 15.7659 4.77903 15.5744 4.90534 15.4867C5.01572 15.4101 5.1523 15.3811 5.2843 15.4063C5.43533 15.4351 5.58038 15.5802 5.87048 15.8703L8.12957 18.1294C8.41967 18.4195 8.56472 18.5645 8.59356 18.7155C8.61877 18.8475 8.58979 18.9841 8.51314 19.0945C8.42545 19.2208 8.23399 19.2944 7.85107 19.4417L2.5 21.4998Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                    </svg>
                                </button>
                                <button class="btn btn-danger btn-sm delete-btn" data-id="${todo.todo_id}">
                                <svg width="15px" height="15px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M16 6V5.2C16 4.0799 16 3.51984 15.782 3.09202C15.5903 2.71569 15.2843 2.40973 14.908 2.21799C14.4802 2 13.9201 2 12.8 2H11.2C10.0799 2 9.51984 2 9.09202 2.21799C8.71569 2.40973 8.40973 2.71569 8.21799 3.09202C8 3.51984 8 4.0799 8 5.2V6M10 11.5V16.5M14 11.5V16.5M3 6H21M19 6V17.2C19 18.8802 19 19.7202 18.673 20.362C18.3854 20.9265 17.9265 21.3854 17.362 21.673C16.7202 22 15.8802 22 14.2 22H9.8C8.11984 22 7.27976 22 6.63803 21.673C6.07354 21.3854 5.6146 20.9265 5.32698 20.362C5 19.7202 5 18.8802 5 17.2V6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                                </svg>
                                </button>
                            </td>
                        </tr>
                    `;
                    count++;
                });

                // Update the table body
                $("#todoList").html(tableBody);
            },
            error: function (error) {
                console.log("Error fetching todos:", error);
            }
        });
    }

    //search-bar
    $('#search-bar').on("input",function(){
        let search_val = $('#search-bar').val();
        let filter_val = $('#filter-bar').val();
        fetchTodos(search = search_val, filter = filter_val);
    })

    //filter-bar
    $('#filter-bar').on("input", function () {
        let search_val = $('#search-bar').val();
        let filter_val = $('#filter-bar').val();
        fetchTodos(search = search_val, filter = filter_val);
    })

    // Fetch todos when page loads
    fetchTodos();

    // Handle Delete Task
    $(document).on("click", ".delete-btn", function () {
        let csrfToken = getCSRFToken(); // Fetch CSRF token
        let todoId = $(this).data("id");

        if (confirm("Are you sure you want to delete this task?")){
            $.ajax({
                url: `/delete/${todoId}/`,
                method: "DELETE",
                headers: { "X-CSRFToken": csrfToken },
                success: function () {
                    fetchTodos(); // Refresh list
                },
                error: function (error) {
                    console.log("Error deleting task:", error);
                }
            });
        }
    });

    function getCSRFToken() {
        return $('input[name="csrfmiddlewaretoken"]').val();
    }

    // Handle Update Task
    $(document).on("click", ".update-btn", function () {
        let todoId = $(this).data("id");

        // Fetch task details using AJAX
        $.ajax({
            url: `/get_todo_update/${todoId}/`, // API to fetch task details
            method: "GET",
            dataType: "json",
            success: function (response) {
                // Populate modal fields
                $("#updateTodoId").val(response.todo_id);
                $("#updateTitle").val(response.title);
                $("#updatePriority").val(response.priority_level.toLowerCase());
                $("#updateDueDate").val(response.due_date);
                $("#updateStatus").val(response.status.toLowerCase());

                // Show modal
                $("#updateModal").modal("show");
            },
            error: function (error) {
                console.log("Error fetching task:", error);
            }
        });
    });

    $("#saveUpdateBtn").on("click", function () {
        let csrfToken = getCSRFToken();
        let todoId = $("#updateTodoId").val();
        let updatedData = {
            title: $("#updateTitle").val(),
            priority_level: $("#updatePriority").val(),
            due_date: $("#updateDueDate").val(),
            status: $("#updateStatus").val(),
        };

        // Check for empty fields before making the request
        if (!updatedData.title || !updatedData.priority_level || !updatedData.due_date || !updatedData.status) {
            alert("All fields are required!");
            return;
        }

        // Send update request
        $.ajax({
            url: `/update/${todoId}/`, 
            method: "POST",
            headers: { "X-CSRFToken": csrfToken },
            data: updatedData,
            success: function () {
                $("#updateModal").modal("hide");  // Hide modal after update
                fetchTodos();  // Refresh the list
            },
            error: function (xhr) {
                let errorMessage = xhr.responseJSON?.error || "An error occurred!";
                alert(errorMessage); // Show error message
            }
        });
    });
});


/**
 * Validates the form inputs before submission.
 *
 * This function checks if the required fields (title, priority level, 
 * due date, and status) are filled. If any field is empty, an alert 
 * message is displayed, and the function returns false to prevent form submission.
 *
 * @returns {boolean} Returns true if all fields are valid, otherwise false.
 */
function validation() {
    let isValid = true;
    let title = $("#id_title").val().trim();
    let priority_level = $("#id_priority_level").val();
    let due_date = $("#id_due_date").val();
    let status = $("#id_status").val();
    if (title == "") {
        alert("Enter a title!");
        isValid = false;
        return false;
    }
    if (priority_level == "") {
        alert("Select the priority!");
        isValid = false;
        return false;
    }
    if (due_date == "") {
        alert("Pick a due date!");
        isValid = false;
        return false;
    }
    if (status == "") {
        alert("Select a status!");
        isValid = false;
        return false;
    }
    return isValid;
}