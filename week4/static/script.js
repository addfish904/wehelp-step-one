function validateForm() {
    let checkbox = document.getElementById("agree");
    if (!checkbox.checked) {
        alert("Please check the checkbox first");
        return false;
    }
    return true;
}

function calculateSquare(event) {
    event.preventDefault(); 

    let input = document.getElementById("square-input").value;
    let number = parseInt(input, 10);

    if (isNaN(number) || number <= 0) {
        alert("請輸入正整數！");
        return false;
    }

    window.location.href = "/square/" + number;
}
