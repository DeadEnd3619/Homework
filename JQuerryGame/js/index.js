$(document).ready(function() {
    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    let playerX = 60.0;
    let playerY = 30.0;
    let playerPOS = [playerX, playerY];
    let Game = true;
    let input = true;
    counter = 0;
    $(document).on("keydown", (e) => {
        if (input == true){
        console.log(e.key);
        switch(e.key){
            case 'w':$('#player').animate({top: "-=10px"}, 100);playerY = playerY - 1;console.log(playerPOS);input=false;break;
            case 'a':$('#player').animate({left: "-=10px"}, 100);playerX = playerX - 1;console.log(playerPOS);input=false;break;
            case 's':$('#player').animate({top: "+=10px"}, 100);playerY = playerY + 1;console.log(playerPOS);input=false;break;
            case 'd':$('#player').animate({left: "+=10px"}, 100);playerX = playerX + 1;console.log(playerPOS);input=false;break;
        }}});




async function game() {
    while (Game) {
        input = true;
        counter++;
        await sleep(1000);
        if (counter == 1000) {
            Game = false;
    
    }
}


game();

}});