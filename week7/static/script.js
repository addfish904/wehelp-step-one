function queryMember(){
    let username = document.getElementById("queryUsername").value;
    fetch(`http://127.0.0.1:3000/api/member?username=${username}`)
    .then(response => response.json())
    .then(data => {
        if(data.data){
            document.getElementById("queryResult").innerText = `${data.data.name} (${data.data.username})`
        }
        else{
            document.getElementById("queryResult").innerText = 'No Data'
        }
        console.log()
    })
}

function updateName(){
    let newName = document.getElementById("updateName").value;
    fetch(`http://127.0.0.1:3000/api/member`,{
        method: "PATCH",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: newName })
    })
    .then(response => response.json())
    .then(data => {
        if(data.ok){
            document.getElementById("updateResult").innerText = "更新成功";
        }else{
            document.getElementById("updateResult").innerText = "更新失敗";
        }
    })
}