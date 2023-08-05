URL = window.URL || window.webkitURL;
var gumStream;
//stream from getUserMedia()
var rec;
//Recorder.js object
var input;
//MediaStreamAudioSourceNode we'll be recording
// shim for AudioContext when it's not avb.
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext = new AudioContext;
//new audio context to help us record
var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");
var pauseButton = document.getElementById("pauseButton");
//add events to those 3 buttons
recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);
pauseButton.addEventListener("click", pauseRecording);

function startRecording() {
  var imageContainer = document.getElementById("imageContainer");
  var image = document.createElement("img");

  const imageUrl = document.getElementById('myImage').src;

  image.src = imageUrl;
  imageContainer.appendChild(image);


audioContext.resume()
/* Simple constraints object, for more advanced audio features see
context.resume()
https://addpipe.com/blog/audio-constraints-getusermedia/ */

var constraints = {
    audio: true,
    video: false
}
/* Disable the record button until we get a success or fail from getUserMedia() */

recordButton.disabled = true;
stopButton.disabled = false;
pauseButton.disabled = false

/* We're using the standard promise based getUserMedia()

https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia */

navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
    console.log("getUserMedia() success, stream created, initializing Recorder.js ...");
    /* assign to gumStream for later use */
    gumStream = stream;
    /* use the stream */
    input = audioContext.createMediaStreamSource(stream);
    /* Create the Recorder object and configure to record mono sound (1 channel) Recording 2 channels will double the file size */
    rec = new Recorder(input, {
        numChannels: 1
    })
    //start the recording process
    rec.record()
    console.log("Recording started");
}).catch(function(err) {
    //enable the record button if getUserMedia() fails
    recordButton.disabled = false;
    stopButton.disabled = true;
    pauseButton.disabled = true
});

console.log("recordButton clicked");
}

function pauseRecording() {
    console.log("pauseButton clicked rec.recording=", rec.recording);
    if (rec.recording) {
        //pause
        rec.stop();
        pauseButton.innerHTML = "Resume";
    } else {
        //resume
        rec.record()
        pauseButton.innerHTML = "Pause";
    }
}

function stopRecording() {
    console.log("stopButton clicked");

    var container = document.getElementById("imageContainer");
    container.innerHTML = "";

    //disable the stop button, enable the record too allow for new recordings
    stopButton.disabled = true;
    recordButton.disabled = false;
    pauseButton.disabled = true;
    //reset button just in case the recording is stopped while paused
    pauseButton.innerHTML = "Pause";
    //tell the recorder to stop the recording
    rec.stop(); //stop microphone access
    gumStream.getAudioTracks()[0].stop();
    //create the wav blob and pass it on to createDownloadLink
    rec.exportWAV(createDownloadLink);
}


function createDownloadLink(blob) {
    var url = URL.createObjectURL(blob);
    var au = document.createElement('audio');
    var br = document.createElement('br')
    var li = document.createElement('li');
    var link = document.createElement('a');
    //add controls to the <audio> element
    au.controls = true;
    au.src = url;
    //link the a element to the blob
    link.href = url;
    link.download = new Date().toISOString() + '.wav';
    link.innerHTML = link.download;
    //add the new audio and a elements to the li element
    li.appendChild(br);
    li.appendChild(au);
    li.appendChild(br);
    li.appendChild(link);
    li.appendChild(br);
    //add the li element to the ordered list
    recordingsList.appendChild(li);

    //for label
    var label = document.createElement('label');
    label.setAttribute('for', 'num_users');
    label.innerHTML = 'Number of Participants';

    li.appendChild(label)

    //For select tag
    var select = document.createElement('select');

    select.setAttribute('name', 'num_users');

    select.setAttribute('id','participants')

    for (var i = 1; i <= 10; i++) {
      var option = document.createElement('option');
      option.value = i;
      option.text = i;
      select.appendChild(option);
    }

    li.appendChild(select)

    //upload file code

    var filename = `${getDateTime()}.wav`;
    //filename to send to server without extension
    //upload link
    var upload = document.createElement('button');
    upload.href = "#";
    upload.classList.add('btn');
    upload.classList.add('btn-success');
    upload.innerHTML = "Submit";
    upload.addEventListener("click", function(event) {
//        var xhr = new XMLHttpRequest();
//        xhr.onload = function(e) {
//            if (this.readyState === 4) {
//                console.log("Server returned: ", e.target.responseText);
//            }
//        };
//        var fd = new FormData();
//        fd.append("audio_data", blob, filename);
//        xhr.open("POST", "upload.php", true);
//        xhr.send(fd);
        var form = new FormData();
        form.append("audio_data", blob, filename);
        form.append("csrfmiddlewaretoken",$("#csrf").val())
        form.append("filename",filename)
        form.append("num_users",$('#participants').val())
        $.ajax(
        {
            url: '../transcribe/speechtotext/',
            type: "POST",
            data: form,
            contentType: false,
            processData: false,
            success: function(getData)
            {
                console.log(getData);
                $('#replace').html(getData)
//                let element = document.getElementById('recordingsList');
//                element.insertAdjacentText('afterend', getData.text);
            }
        });
    })
    li.appendChild(document.createTextNode(" ")) //add a space in between
    li.appendChild(upload) //add the upload link to li

}

function getDateTime(){
    const cd = new Date();
    const dateTime = `${cd.getDate()}-${cd.getMonth()}-${cd.getFullYear()} ${cd.getHours()}-${cd.getMinutes()}-${cd.getSeconds()}`;
    return dateTime
}