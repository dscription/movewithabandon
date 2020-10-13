// p5.disableFriendlyErrors = true;

// Setup more joint and posenet variables here
let frameRate = 30

// Setup CCapture here
// Create a capturer that exports a WebM video
var capturer = new CCapture({
  format: "webm", 
  framerate: frameRate,
  verbose: true,
  timeLimit: limit,
});

let canvas;
function setup() {
  let p5canvas = createCanvas(400, 400);
  canvas = p5canvas.canvas

  // start capture 
  capturer.start()
}


function draw() {
  let secondsElapsed = frameCount/frameRate;
  if(mouseIsPressed){
    ellipse(mouseX,mouseY,20)
  }

  if (secondsElapsed >= 5) {
    console.log('5 seconds elapsed')
    capturer.stop()
    // capturer.save();
    // custom save, will get a blob in the callback
    capturer.save( function(blob) {
      console.log(blob)
    } );
  }
    
  console.log('capturing')
  capturer.capture(canvas)
}