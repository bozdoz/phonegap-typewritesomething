var keypress_audio = new makeMultiAudio('typewritesomething/inc/keypress.mp3'),
    newline_audio = new makeMultiAudio('typewritesomething/inc/return.mp3');

function makeMultiAudio (src) {
    var output = [],
         current = 0,
         num = 5;
    for (var i = 0; i < num; i++) {
        output.push(new Audio(src));
    }
    this.play = function () {
        output[current++ % num].play();
    };
}

function ga () {
	console.log.call(this, arguments);
}