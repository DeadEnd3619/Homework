$(document).ready(function() {
    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    let playerPOS = [3, 3];
    let Game = true;
    let input = true;
    let gameBoard = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],//botom of screen to top of screen         Very Left of screen
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]//                                         very right of screen
    ];


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
                while (gameBoard[future[0]][future[1]] === 0) {
                    squares++;
                    future = [future[0], future[1] - 1];
                }
                playerPOS = [playerPOS[0], playerPOS[1] - squares];
                console.log(playerPOS);
                $('#player').animate({ top: `-=${squares * 10}px` }, 100);
                break;
            case 'down':
                future = [playerPOS[0], playerPOS[1] + 1];
                while (gameBoard[future[0]][future[1]] === 0) {
                    squares++;
                    future = [future[0], future[1] + 1];
                }
                playerPOS = [playerPOS[0], playerPOS[1] + squares];
                console.log(playerPOS);
                $('#player').animate({ top: `+=${squares * 10}px` }, 100);
                break;
            case 'left':
                future = [playerPOS[0] - 1, playerPOS[1]];
                while (gameBoard[future[0]][future[1]] === 0) {
                    squares++;
                    future = [future[0] - 1, future[1]];
                }
                playerPOS = [playerPOS[0] - squares, playerPOS[1]];
                console.log(playerPOS);
                $('#player').animate({ left: `-=${squares * 10}px` }, 100);
                break;
            case 'right':
                future = [playerPOS[0] + 1, playerPOS[1]];
                while (gameBoard[future[0]][future[1]] === 0) {
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
            input = true;
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