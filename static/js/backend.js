console.log("Dashboard Javascript Loaded");

document.getElementById("reset_kiosk").onclick = function(){
    if (confirm("Are you sure you want to reset the Kiosk?")){
        fetch('/reset_kiosk').then(location.href = "/redirect");
    }
}

document.getElementById("delete_all").onclick = function(){
    if (confirm("Are you sure you want to delete all coopertitions from the database?")){
        fetch("/delete_all").then(location.href = "/redirect");
    }
}

document.getElementById("set_status").onclick = function(){
    var status = document.getElementById("status_text").value;
    if (status != ""){
        fetch("/setstatus", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"status": status})
        })
        .then(location.href = "/redirect");
    } else {
        alert("Missing Status!");
    }
}

function assignArchive(i){
    i.onclick = function(){
        for (j = 0; j < red_inputs.length; j++){
            if (red_inputs[j].getAttribute("red") == i.getAttribute("archive")){
                red_input = red_inputs[j];
            }
        }

        for (j = 0; j < blue_inputs.length; j++){
            if (blue_inputs[j].getAttribute("blue") == i.getAttribute("archive")){
                blue_input = blue_inputs[j];
            }
        }
        if (red_input.value != "" && blue_input.value != ""){
            if(confirm("Are you sure you want to archive "+i.getAttribute("archive")+"\n Red "+red_input.value+" vs Blue "+blue_input.value+"?")){
                fetch("/archive", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({"red": red_input.value, "blue": blue_input.value, "match": i.getAttribute("archive")})
                })
                .then(location.href = "/redirect");
            }
        } else {
            alert("Missing Values!");
        }
    }
}

red_inputs = document.querySelectorAll("[red]");
blue_inputs = document.querySelectorAll("[blue]");
archive_inputs = document.querySelectorAll("[archive]");
delete_inputs = document.querySelectorAll("[delete]");

for (i = 0; i < archive_inputs.length; i++){
    assignArchive(archive_inputs[i]);
}

for (i = 0; i < delete_inputs.length; i++){
    delete_inputs[i].onclick = function(e){
        if (confirm("Are you sure you want to delete "+e.target.getAttribute("delete")+"?")){
            fetch("/delete", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({"match": e.target.getAttribute("delete")})
            })
            .then(location.href = "/redirect");
        }
    }
}