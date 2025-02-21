function validateForm() {
    let checkbox = document.getElementById("agree");
    if (!checkbox.checked) {
        alert("Please check the checkbox first");
        return false;
    }
    return true;
}