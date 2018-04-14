$(document).ready(function(){

    console.log('inside results.js')
    animateValue('entries', 0, 900, 1500);
    var op = 
        {strings : ['  people completed the survey'],
         typeSpeed: 40};
        var entries_txt = new Typed('#entries-txt',op);

    var options = {strings: ['Senior Project: Internet Usage in Paraguay'],
        typeSpeed:40,
        callback: function () {
                $('.typed-cursor').hide();
        } 
    }
                $('.typed-cursor').hide();
    var title = new Typed('#title', options)
                $('.typed-cursor').hide();
});
// https://stackoverflow.com/questions/16994662/count-animation-from-number-a-to-b
function animateValue(id, start, end, duration) {
    //assumes integer values for start and end
    console.log('inside animate')
    var obj = document.getElementById(id);
    var range = end - start;

    //no timer shorter than 50ms (not really visible any way)
    var minTimer = 50;
    //calc step time to show all interediate values
    var stepTime = Math.abs(Math.floor(duration / range));

    // never go below minTimer
    stepTime = Math.max(stepTime, minTimer);

    // get current time and calculate desired end time
    var startTime = new Date().getTime();
    var endTime = startTime + duration;
    var timer;

    function run() {
        var now = new Date().getTime();
        var remaining = Math.max((endTime - now) / duration, 0);
        var value = Math.round(end - (remaining * range));
        obj.innerHTML = value;
        if (value == end) {
            clearInterval(timer);
        }
    }

    timer = setInterval(run, stepTime);
    run();
}
