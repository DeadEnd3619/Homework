$(document).ready(function() {
    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    let playerPOS = [3, 3];
    let Game = true;
    let input = true;
    let gameBoard = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], // 0          Very Left of screen 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], // 1
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 2
        [1, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 3
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 4
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 5
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 6
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 7
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 8
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 9
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 10
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 11
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 12
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 13
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 14
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 15
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 16
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 17
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 18
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 19
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 20
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 21
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 22
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 23
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 24
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 25
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 26
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], // 27
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  // 28            very right of screen
    ];
    
    let x = 1;
    for (let i of gameBoard) {
        let y = 1;
        for (let j of i) {
            if (j == 1) {
                $("body").append(`<div class="wall" style="grid-column: ${x} / ${x + 1 }; grid-row: ${y} / ${y + 1};"></div>`);
            }
            y++;
        }
        x++;
    }
    

    $(document).on("keydown", (e) => {
        if (input) {
            console.log(e.key);
            inputCheck(e.key);
        }
    });

    $(document).on("keyup", (e) => {
        input = true;
    });

    let inputCheck = function(key) {
        switch (key) {
            case 'w':
            case 'W':
            case 'ArrowUp':
                movePlayer('up');
                break;

            case 'a':
            case 'A':
            case 'ArrowLeft':
                movePlayer('left');
                break;

            case 's':
            case 'S':
            case 'ArrowDown':
                movePlayer('down');
                break;

            case 'd':
            case 'D':
            case 'ArrowRight':
                movePlayer('right');
                break;
        }
    };

    let movePlayer = function(direction) {
        let future;
        let squares = 0;

        switch (direction) {
            case 'up':
                future = [playerPOS[0], playerPOS[1] - 1];
                while (gameBoard[future[0]][future[1]] !== 1) {
                    squares++;
                    future = [future[0], future[1] - 1];
                }
                playerPOS = [playerPOS[0], playerPOS[1] - squares];
                console.log(playerPOS);
                
                $('#player').animate({ top: `-=${squares * 10}px` }, 100);
                break;
            case 'down':
                future = [playerPOS[0], playerPOS[1] + 1];
                while (gameBoard[future[0]][future[1]] !== 1) {
                    squares++;
                    future = [future[0], future[1] + 1];
                }
                playerPOS = [playerPOS[0], playerPOS[1] + squares];
                console.log(playerPOS);
                
                $('#player').animate({ top: `+=${squares * 10}px` }, 100);
                break;
            case 'left':
                future = [playerPOS[0] - 1, playerPOS[1]];
                while (gameBoard[future[0]][future[1]] !== 1) {
                    squares++;
                    future = [future[0] - 1, future[1]];
                }
                playerPOS = [playerPOS[0] - squares, playerPOS[1]];
                console.log(playerPOS);
                
                $('#player').animate({ left: `-=${squares * 10}px` }, 100);
                break;
            case 'right':
                future = [playerPOS[0] + 1, playerPOS[1]];
                while (gameBoard[future[0]][future[1]] !== 1) {
                    squares++;
                    future = [future[0] + 1, future[1]];
                }
                playerPOS = [playerPOS[0] + squares, playerPOS[1]];
                console.log(playerPOS);
                
                $('#player').animate({ left: `+=${squares * 10}px` }, 100);
                break;
        }
    };
    let checkWin = function() {
        if (playerPOS[0] === 15 && playerPOS[1] === 7) {
            return true;
        }else{
            return false;
        }}

    let game = async function() {
        while (Game) {
            await sleep(100);
            if (checkWin() === true){
                Game = false;
                console.log('you win');
            }
        }
        console.log('game over');
    };

    console.log(gameBoard.length);
    console.log(gameBoard[0].length);
    game();
});