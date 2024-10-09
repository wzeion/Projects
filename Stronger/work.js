$(".btn").click(function(){
    var name = $(this).attr("id")
    playSound(name);
    Pressed(name);
    
});

function playSound(name){
    var audio = new Audio("sounds/"+name+".mp3");
    audio.play();
}

function Pressed(button){
    $("#"+button).addClass("pressed");
    setTimeout(function(){
        $("#"+button).removeClass("pressed");
    },100);
}