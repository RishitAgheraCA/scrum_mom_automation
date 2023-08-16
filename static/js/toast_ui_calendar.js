document.addEventListener('DOMContentLoaded', function () {

    var myVar = document.getElementById('myDiv').dataset.myVariable;

    var myList=myVar.replace(/'/g, '"');

    var org_list=JSON.parse(myList);

//    console.log(Object.prototype.toString.call(org_list));

    var schedules = []

    for (let i = 0; i < org_list.length; i++) {
        var task_dict = {
          id: new String(i),
          calendarId:new String(i),
          title:org_list[i].ongoing_task,
          body:'<h6>Name : '+org_list[i].name+'</h6><h6>Blockers : '+org_list[i].blockers+'</h6><h6>Deliverables : '+org_list[i].completed_task+'</h6>',
          start: new Date(org_list[i].days_req),
          category:'time',
          isReadOnly:true,
        };

        schedules.push(task_dict)
    }

    console.log(schedules)

    const calendar = new tui.Calendar('#calendar', {
          usageStatistics: false,
            defaultView: 'month',
            useCreationPopup: true, // Allow events to be created using the popup
            useDetailPopup: true,
            timezone:'America/Toronto',
            theme:'default',
        });

    calendar.createSchedules(schedules)

    document.getElementById('prevButton').addEventListener('click', () => {
      calendar.prev();
    });

    document.getElementById('nextButton').addEventListener('click', () => {
      calendar.next();
    });

    });

