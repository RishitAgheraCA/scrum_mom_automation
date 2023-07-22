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





