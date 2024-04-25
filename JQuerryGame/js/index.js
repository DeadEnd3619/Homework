$(document).ready(function() {
    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    let playerX = 1;
    let playerY = 5;
    let playerPOS = [playerX, playerY];
    let Game = true
    let input = true;
    let gameBoard = [[1,1,1,1,1,1,1],[1,0,0,0,0,2,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]

    

    let values

    $(document).on("keydown", (e) => {
        if (input){
        console.log(e.key);
        inputCheck(e.key);
    }});


    $(document).on("keyup", (e) => {
        input = true;
    })


    

    let inputCheck = function(key){

        switch(key){
            case 'w':
            case 'W':
            case 'ArrowUp':
                values = colsionCheck('up')
                if (playerY <= 1){break;}
                else {
                    $('#player').animate({top: "-=10px"}, 100);
                    playerY = playerY - 1;
                    input = false;
                    playerPOS = [playerX, playerY];
                    console.log(playerPOS);
                    values = []
                    break;
                }
            case 'a':
            case 'A':
            case 'ArrowLeft':
                values = colsionCheck('left')
                if (playerX <= 1){break;}
                else {
                    $('#player').animate({left: "-=10px"}, 100);
                    playerX = playerX - 1;
                    input = false;
                    playerPOS = [playerX, playerY];
                    console.log(playerPOS);
                    values = []
                    break;
                }
            case 's':
            case 'S':
            case 'ArrowDown':
                values = colsionCheck('down')
                if (values[4]){break;}
                else {
                    $('#player').animate({top: "+=10px"}, 100);
                    playerY = playerY + 1;
                    input = false;
                    playerPOS = [playerX, playerY];
                    console.log(playerPOS);
                    values = []
                    break;
                }
            case 'd':
            case 'D':
            case 'ArrowRight':
                values = colsionCheck('right')
                if (playerX >= 120){break;}
                else {
                $('#player').animate({left: "+=10px"}, 100);
                playerX = playerX + 1;
                input = false;
                playerPOS = [playerX, playerY];
                console.log(playerPOS);
                values = []
                break;
        }}
    }


    let colsionCheck = function(direction){
        let values = []
        let squares = 0
        switch(direction){
        case 'up':
        case 'down':
            values.push('top');
            break;
        
        case 'left':
        case 'right':
            values.push('left')
            break;}

        switch(direction){
            case 'left':
            case 'up':
                values.push('-=');
                break;

            case 'right':
            case 'down':
                values.push('+=');
                break;}
         
            
            
}


        


    let game = async function(){
        while (Game) {
            await sleep(100);
            input = true;
    }};








    game();
});