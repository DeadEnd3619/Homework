var playBoard = [null,null,null,null,null,null,null,null,null];
var playerTurn = 'Player one'
var turnXO = 'X'
var winningPos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
function getBoardPos(playBoardPos){
    var index = playBoardPos - 1
    if (playerTurn == 'Player one'){
        turnXO = 'X'
    }else{
        turnXO = 'O'
    }
    if (playBoardPos == 1 || playBoardPos == 2 || playBoardPos == 3){
        doPlayerAction(index)
    }else if (playBoardPos == 4 || playBoardPos == 5 || playBoardPos == 6){
        doPlayerAction(index)
    }else{
        doPlayerAction(index)
    }
}
function doPlayerAction(index){
    if (playBoard[index] == null){
        playBoard[index] = turnXO
        
        if (playerTurn == 'Player one'){
            playerTurn = 'Player two'
        }else{
            playerTurn = 'Player one'
        }
    }
    else{
        console.log('invalid input')
    }
    let boolBoard = [bool(playBoard[0]), bool(playBoard[1]), bool(playBoard[2]), bool(playBoard[3]), bool(playBoard[4]), bool(playBoard[5]), bool(playBoard[6]), bool(playBoard[7]), bool(playBoard[8])]
    for (let i of winningPos){
        
    }
    console.log(playBoard)
}









