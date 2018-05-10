$(document).ready(function(){
    window.sr = ScrollReveal({ reset: true });
    console.log('results')

    //title
    sr.reveal('#title', { duration: 200 });
    var options = {strings: ['Senior Project: Internet Usage in Paraguay'],
        typeSpeed:40,
        callback: function () {
                $('.typed-cursor').hide();
        }
    }
                $('.typed-cursor').hide();

        var title = new Typed('#title', options)
        $('.typed-cursor').hide();


    sr.reveal('#description', {
      origin: 'right',
      duration: 2000
    });

    sr.reveal('#ent1', {
      rotate: { x: 100, y: 100, z: 0 },
      duration: 1000
    });
    animateValue('entries', 0, 900, 1500);
    var op = {strings : ['  people completed the survey'], typeSpeed: 40};
        var entries_txt = new Typed('#entries-txt',op);
        $('.typed-cursor').hide();
    sr.reveal('.#ent2', {
      viewFactor: 0.5
    });
    var tv_txt = {strings: ['watch TV as means to get informed on news'],typeSpeed:40}
    var tv = new Typed('#tv-txt', tv_txt)
    sr.reveal('#ent3', {
      duration: 200
    });
    var mi_txt = {strings: [counts["millenials"]["string"]],typeSpeed:40}
    var mi = new Typed('#mi-txt', mi_txt)
    sr.reveal('#ent4', {
      duration: 200
    });
    var bb_txt = {strings: [counts["baby_boomers"]["string"]],typeSpeed:40}
    var bb = new Typed('#bb-txt', bb_txt)
    $('.typed-cursor').hide();

    // GENERAL SETTING

    // Custom Settings



});
// https://stackoverflow.com/questions/16994662/count-animation-from-number-a-to-b
function animateValue(id, start, end, duration) {
    //assumes integer values for start and end
    // console.log('inside animate')
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
