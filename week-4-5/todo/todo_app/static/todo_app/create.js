/**
 * Validates the form inputs before submission.
 *
 * This function checks if the required fields (title, priority level, 
 * due date, and status) are filled. If any field is empty, an alert 
 * message is displayed, and the function returns false to prevent form submission.
 *
 * @returns {boolean} Returns true if all fields are valid, otherwise false.
 */
function validation(){
    let isValid = true;
    let title = document.getElementById("title").value;
    let priority_level = document.getElementById("priority_level").value;
    let due_date = document.getElementById("due_date").value;
    let status = document.getElementById("status").value;
    if (title==""){
        alert("Enter a title!");
        isValid = false;
        return false;
    }
    if(priority_level==""){
        alert("Select the priority!");
        isValid = false;
        return false;
    }
    if(due_date == ""){
        alert("Pick a due date!");
        isValid = false;
        return false;
    }
    if(status == ""){
        alert("Select a status!");
        isValid = false;
        return false;
    }
    return isValid;
}