var gamePattern = [];
var buttonColours=["red","green","blue","yellow"];

var userClickedPattern=[];

var started = false;
var level = 0;
$(document).keydown(function(){
    if(!started){
    $("#level-title").text("Level " + level);
    nextSequence();
    started = true;
    }


})
$(".btn").click(function(){
    var userClickedButton = $(this).attr("id")
    userClickedPattern.push(userClickedButton);
    playSound(userClickedButton);
    animatePress(userClickedButton);

    checkAnswer(userClickedPattern.length-1)
})

function nextSequence(){

    userClickedPattern=[];

    level++;
    $("#level-title").text("Level " + level);

    var randNum = Math.floor(Math.random()*4);
    var randColour = buttonColours[randNum];

    gamePattern.push(randColour);

    $("#"+randColour).fadeIn(100).fadeOut(100).fadeIn(100);
    playSound(randColour);
}
function playSound(name){
    var audio = new Audio ("sounds/"+name+".mp3")
    audio.play();
}
function animatePress(Pressed){
    $("#"+Pressed).addClass("pressed");
    setTimeout(function () {
        $("#" + Pressed).removeClass("pressed");
      }, 100);
}
function checkAnswer(currentLevel){
    if(userClickedPattern[currentLevel]===gamePattern[currentLevel]){
        console.log("ok")
        if (userClickedPattern.length === gamePattern.length){
            setTimeout(function () {
              nextSequence();
            }, 1000);
    
          }
    }
    else{
        console.log("not ok")
        gameOver();
        startOver();
    }
}
function gameOver(){
    playSound("wrong");
    $("body").addClass("game-over")
    setTimeout(function(){
        $("body").removeClass("game-over")
    },200)
    $("#level-title").text("Game Over, Press Any Key to Restart");
}
function startOver(){
    level=0;
    gamePattern=[];
    started=0;
}