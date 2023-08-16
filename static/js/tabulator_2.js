var myVar = document.getElementById("json_val").value;

var myList=myVar.replace(/'/g, '"');

var org_list=JSON.parse(myList);

var tables=[]

org_list.forEach(function(element) {
        var table_1 = new Tabulator("#completed_task_"+element.name, {
            height:311,
            layout:"fitDataTable",

            movableRows:true,
            movableRowsReceiver: "add",
            movableRowsConnectedTables:['.a'],
            movableRowsSender: "delete",
            placeholder:"No Data set",
            data:[{'task':element.task}],
            columns:[
                {title:"Task", field:"task"},
            ],
        });

        tables.push(table_1)

        var check_2 = new Tabulator("#blockers_"+element.name, {
            height:311,
            layout:"fitDataTable",
            movableRows:true,
            movableRowsConnectedTables:['.a']
            movableRowsReceiver: "add",
            movableRowsSender: "delete",
            placeholder:"No Data set",
            data:[{'blockers':element.blockers}],
            columns:[
                {title:"Blockers", field:"blockers"},
            ],
        });

        var check_3 = new Tabulator("#deliverables_"+element.name, {
            height:311,
            layout:"fitDataTable",
            movableRows:true,
            movableRowsConnectedTables:['.a'],
            movableRowsReceiver: "add",
            movableRowsSender: "delete",
            placeholder:"No Data set",
            data:[{'deliverables':element.deliverables}],
            columns:[
                {title:"Deliverables", field:"deliverables"},
            ],
        });

});

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

function send_task_load(data){
    var token = '{{csrf_token}}';

    $.ajax({
        headers: { "X-CSRFToken": getCookie("csrftoken") },
        url:'./main',
        type:"POST",
        data: JSON.stringify(data),
        contentType: 'application/json',
        success : function(json) {
                 alertify.success(json.msg);
//                 $('textarea').each(function() {
//                      $(this).val('');
//                  });
        },
        error: function(json){
                 alertify.error(json.msg);
        },
    });
}

//$("#task_user_email").submit(function(e){
//    e.preventDefault();
//    const data = Object.fromEntries(new FormData(e.target).entries());
//
//    alertify.confirm("Would you like to send the mail to the users ?",
//      function(){
//        send_task_load(data)
//      },
//      function(){
//        alertify.error('Process Canceled');
//      });
//});

