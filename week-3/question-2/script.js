function validation() {
    alert("Validation Starts");
    let profile = document.getElementById("profile");
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let dob = document.getElementById("dob").value;
    let gender = document.querySelector('input[name="gender"]:checked');
    let lang = document.getElementById("language").value;
    let isValid = true;

    //profile picture validation
    if (profile.files.length === 0) {
        document.getElementById("profileErr").textContent = "Upload profile picture!";
        document.getElementById("profileErr").style.display = "block";
        isValid = false;
    } else {
        const allowedExtensions = ["jpg", "jpeg", "png", "gif", "bmp"];
        const fileName = profile.files[0].name.toLowerCase();
        const fileExtension = fileName.split(".").pop();

        //profile picture filetype validation
        if (!allowedExtensions.includes(fileExtension)) {
            document.getElementById("profileErr").textContent = "Only JPG, JPEG, PNG, GIF, BMP files are allowed!";
            document.getElementById("profileErr").style.display = "block";
            isValid = false;
        } else {
            document.getElementById("profileErr").style.display = "none";
        }
    }
    
    //name validation
    if(name===""){
        document.getElementById("nameErr").style.display = "block";
        isValid = false;
    }else{
        document.getElementById("nameErr").style.display = "none";
    }

    //email validation
    if (email === "") {
        document.getElementById("emailErr").textContent = "Enter an email address!";
        document.getElementById("emailErr").style.display = "block";
        isValid = false;
    } else {
        const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailPattern.test(email)) {
            document.getElementById("emailErr").textContent = "Enter a valid email address!";
            document.getElementById("emailErr").style.display = "block";
            isValid = false;
        } else {
            document.getElementById("emailErr").style.display = "none";
        }
    }

    //dob validation
    let dobInput = new Date(dob);
    let today = new Date();

    // Check if DOB is empty
    if (dob === "") {
        document.getElementById("dobErr").textContent = "Enter a valid Date of Birth!";
        document.getElementById("dobErr").style.display = "block";
        isValid = false;
    } else if (dobInput >= today) {
        document.getElementById("dobErr").textContent = "Date of Birth cannot be in the future!";
        document.getElementById("dobErr").style.display = "block";
        isValid = false;
    } else {
        document.getElementById("dobErr").style.display = "none";
    }

    //gender validation
    if(!gender){
        document.getElementById("genderErr").style.display = "block";
        isValid = false;
    }else{
        document.getElementById("genderErr").style.display = "none";
    }

    //language validation
    if(lang===""){
        document.getElementById("langErr").style.display = "block";
        isValid = false;
    }else{
        document.getElementById("langErr").style.display = "none";
    }

    // let dict = [profile,name,email,dob,gender.value,lang];
    // alert(JSON.stringify(dict, null, 2));
    alert("Validation Ends!");

    if(isValid){
        return true;
    }else{
        return false;
    }
}


// For removing the profile picture after selecting
document.getElementById("removeProfile").addEventListener("click", function () {
    const fileInput = document.getElementById("profile");
    fileInput.value = ""; // clear file input
});