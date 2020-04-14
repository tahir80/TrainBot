var timer = 0;
var reward = 0;
var result = 0;

var temp_timer = '';

var sec = 0;
var seconds;

function startTimer() {
  seconds = sec;
  timer = setInterval(function() {
    seconds++;
    document.getElementById("timer").innerText = SecondsTohhmmss(seconds);
  }, 1000);
}

function callback() {
  clearInterval(timer);
}
function stopTimer() {
  sec = seconds;
  document.getElementById("timer").innerText = result;
  callback();
}

function SecondsTohhmmss(totalSeconds) {
  var hours = Math.floor(totalSeconds / 3600);
  var minutes = Math.floor((totalSeconds - (hours * 3600)) / 60);
  var seconds = totalSeconds - (hours * 3600) - (minutes * 60);

  // round seconds
  seconds = Math.round(seconds * 100) / 100

  result = (hours < 10 ? "0" + hours : hours);
  result += "-" + (minutes < 10 ? "0" + minutes : minutes);
  result += "-" + (seconds < 10 ? "0" + seconds : seconds);
  return result;
}
