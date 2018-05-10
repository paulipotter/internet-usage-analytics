$(document).ready(function(){
    window.sr = ScrollReveal()//{ reset: true });
    console.log('results')

    //title
    var options = {
        strings: ['Senior Project: Internet Usage in Paraguay'],
        typeSpeed:40,
        callback: function () {
            $('.typed-cursor').hide();
        }
    }
    $('.typed-cursor').hide();
    sr.reveal('#title', {
        origin: 'right',
        duration: 200,
        afterReveal: function(){
            var title = new Typed('#title', options)
            $('.typed-cursor').hide();
        }});

    $('.typed-cursor').hide();

    sr.reveal('#description', {
      origin: 'right',
      duration: 2000,
      reset: true
    });
    $('.typed-cursor').hide();


    var op = {strings : ['  people completed the survey'], typeSpeed: 40};
    sr.reveal('#ent1', {
        origin: 'right',
        duration: 1000,
        afterReveal: function(){
            animateValue('entries', 0, 900, 1500);
            var ent_txt = new Typed("#entries-txt", op);
            $('.typed-cursor').hide();
        }
    });

    sr.reveal('#ent-donuts', {
        origin: 'right',
        duration: 1000,
        delay: 100,
        reset: true,
        afterReveal: function(){
            //load donuts
            loadDonuts();
        }
    });

    var tv_txt = {strings: ["Prefer the TV as their source for the news"]}
    sr.reveal('#ent2', {
        viewFactor: 0.5,
        afterReveal: function(){
            var tv = new Typed('#tv-txt', tv_txt);
            $('.typed-cursor').hide();
            //load gauge
            load1();
      }
    });

    var mi_txt = {strings: [counts["millenials"]["string"]],typeSpeed:40}
    sr.reveal('#ent3', {
        duration: 200,
        afterReveal: function(){
            var mi = new Typed('#mi-txt', mi_txt);
            $('.typed-cursor').hide();
            //load gauge
            load2();
        }
    });

    var bb_txt = {strings: [counts["baby_boomers"]["string"]],typeSpeed:40}
    sr.reveal('#ent4', {
      duration: 200,
      afterReveal: function(){
          var bb = new Typed('#bb-txt', bb_txt);
          $('.typed-cursor').hide();
          //load gauge
          load3();
      }
    });
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
