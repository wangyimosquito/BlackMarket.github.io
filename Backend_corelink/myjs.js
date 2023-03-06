

var viz;
var flag = 0;

function draw(cmd_text) {
    var config = {
        container_id: "viz",
        server_url: "bolt://59.78.54.147:7687",
        server_user: "reader",
        server_password: "huyiyao",
        server_database: "darks",
        arrows: true,
        labels: {
            "Character": {
                "caption": "name",
                "size": "pagerank",
                "community": "community",
                "title_properties": [
                    "name",
                    "pagerank"
                ]
            }
        },
        relationships: {
            "INTERACTS": {
                "thickness": "weight",
                "caption": "name"
            }
        },
        initial_cypher: cmd_text
    };
    
    if(flag == 1){
        viz.updateWithCypher(cmd_text);
        
    }else if(flag == 0){
        viz = new NeoVis.default(config);
        viz.render();
    }
    
    flag = 1;
}

$(document).ready(function(){
    $("#input_btn").click(function(){
        var my_cmd = $("#input_cmd").val();
        draw(my_cmd);
        console.log("draw complete.")
    });
    $("#clear_btn").click(function(){
        if(flag == 1){
            viz.clearNetwork();
        }   
    });
    $("#stable_btn").click(function(){
        if(flag == 1){
            viz.stabilize();
        }
    });
  });