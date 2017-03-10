/*

Phonegap specific scripts to manipulate/use
the typewriter app

*/

var keypress_audio = new makeMultiAudio('typewritesomething/inc/keypress.mp3', 5),
    newline_audio = new makeMultiAudio('typewritesomething/inc/return.mp3', 2);

document.addEventListener('deviceready', function () {
	navigator.splashscreen.hide();
});

function makeMultiAudio (src, instances) {
    var output = [],
        current = 0,
        num = instances || 5;
    for (var i = 0; i < num; i++) {
        output.push(new Audio(src));
    }
    this.play = function () {
        var audio = output[current++ % num];
        audio.currentTime = 0;
        audio.play();
    };
}

function ga () {
	console.log.call(this, arguments);
}