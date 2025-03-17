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