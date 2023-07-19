const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];

var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = monthNames[today.getMonth()]; //January is 0!
var yyyy = today.getFullYear();

today = mm + ' , ' + dd + ' , ' + yyyy;

function formatAMPM(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'PM' : 'AM';
  hours = hours % 12;
  hours = hours ? hours : 12; // the hour '0' should be '12'
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return strTime;
}

$('#date_label').text(today);

$('#time_label').text(formatAMPM(new Date));

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
        data:data,
        success : function(json) {
                 alertify.success(json.msg);
                 $('textarea').each(function() {
                      $(this).val('');
                  });
        },
        error: function(json){
                 alertify.error(json.msg);
        },
    });
}


//$("#task_user_email").submit(function(e){
////    e.preventDefault();
//    const data = Object.fromEntries(new FormData(e.target).entries());
//
//    alertify.confirm("Would you like to send the mail to the users ?",
//      function(){
//        //send_task_load(data);
//      },
//      function(){
//        alertify.error('Process Canceled');
//      });
//});
