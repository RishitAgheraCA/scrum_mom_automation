////define some sample data
//var tabledata = [
//    {id:1, name:"Oli Bob", age:"12", col:"red", dob:""},
//    {id:2, name:"Mary May", age:"1", col:"blue", dob:"14/05/1982"},
//    {id:3, name:"Christine Lobowski", age:"42", col:"green", dob:"22/05/1982"},
//    {id:4, name:"Brendon Philips", age:"125", col:"orange", dob:"01/08/1980"},
//    {id:5, name:"Margret Marmajuke", age:"16", col:"yellow", dob:"31/01/1999"},
// ];

//Table to move rows from
var table = new Tabulator("#example-table-1", {
    height:311,
    layout:"fitColumns",
    movableRows:true,
    movableRowsConnectedTables:["#example-table-2","#example-table-3","#example-table-4"],
    movableRowsReceiver: "add",
    movableRowsSender: "delete",
    placeholder:"No Data set",
    columns:[
        {title:"Name", field:"name"},
    ],
});

//Table to move rows to
var table_1 = new Tabulator("#example-table-2", {
    height:311,
    layout:"fitColumns",
    movableRows:true,
    movableRowsConnectedTables:["#example-table-1","#example-table-3","#example-table-4"],
    movableRowsReceiver: "add",
    movableRowsSender: "delete",
    placeholder:"Drag Rows Here",
    data:[],
    columns:[
       {title:"Task", field:"task"},
    ],
});

var table_2 = new Tabulator("#example-table-3", {
    height:311,
    layout:"fitColumns",
    movableRows:true,
    movableRowsConnectedTables:["#example-table-2","#example-table-1","#example-table-4"],
    movableRowsReceiver: "add",
    movableRowsSender: "delete",
    placeholder:"Drag Rows Here",
    data:[],
    columns:[
        {title:"Status", field:"task"},
    ],
});

var table_3 = new Tabulator("#example-table-4", {
    height:311,
    layout:"fitColumns",
    movableRows:true,
    movableRowsConnectedTables:["#example-table-1","#example-table-2","#example-table-3"],
    movableRowsReceiver: "add",
    movableRowsSender: "delete",
    placeholder:"Drag Rows Here",
    data:[],
    columns:[
        {title:"Time", field:"name"},
    ],
});

//document.getElementById("ajax_load").addEventListener("click", function(){
//    table.setData("/task/load");
//});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function load_data(){
    var token = '{{csrf_token}}';

    $.ajax({
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        url:'./load',
        type:"POST",
        success : function(json) {
            console.log(json.details)
            table.setData(json.details)
            table_1.setData(json.details)
        },

    });
}


$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    load_data()
});