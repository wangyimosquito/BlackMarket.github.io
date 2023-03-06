function close_table(){
    document.getElementById("table-container").style.display = "none"
    document.getElementById("table-background").style.display = "none"
}

function open_table(){
    document.getElementById("table-container").style.display = "block"
    document.getElementById("table-background").style.display = "block"
}

function create_table(json_name){
    $.get(json_name, function (info) {
        $("#table-container tr:not(:first)").html("");
        for(let i=0; i<info.length; i++){
            let type = "<td class=\"grid1\">" + info[i][0].split("_")[1] + "</td>"
            let id = "<td class=\"grid2\">" + info[i][0].split("_")[2] + "</td>"
            let content = "<td class=\"grid3\">" + info[i][1] + "</td>"

            let result="";
            result += "<tr>";
            result += type;
            result += id;
            result += content;
            result += "</tr>";
            $("#table-container tbody").append(result);
        }
        if (info.length == 0){
            let result="";
            result += "<tr>";
            result += "<td class=\"grid1\">N/A</td>";
            result += "<td class=\"grid2\">N/A</td>";
            result += "<td class=\"grid3\">N/A</td>";
            result += "</tr>";
            $("#table-container tbody").append(result);
        }
    })
}