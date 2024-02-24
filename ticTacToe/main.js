var playBoard = [[null,null,null], [null,null,null], [null,null,null]];
var playerTurn = 'Player one'
var turnXO = 'X'
var winningpos = [[[0,0],[0,1],[0,2]], [[1,0],[1,1],[1,2]], [[2,0],[2,1],[2,2]], [[0,0],[1,0],[2,0]], [[0,1],[1,1],[2,1]], [[0,2],[1,2],[2,2]], [0,0],[1,1],[2,2], [[0,2],[1,1],[2,0]]]
function getBoardPos(playBoardpos){
    var index1 = (playBoardpos % 3)
    if (playerTurn == 'Player one'){
        turnXO = 'X'
    }else{
        turnXO = 'O'
    }
    if (playBoardpos == 1 || playBoardpos == 2 || playBoardpos == 3){
        doPlayerAction(index1, 0)
    }else if (playBoardpos == 4 || playBoardpos == 5 || playBoardpos == 6){
        doPlayerAction(index1, 1)
    }else{
        doPlayerAction(index1, 2)
    }
}
function doPlayerAction(index2, index1){
    if (playBoard[index1][index2] == null){
        playBoard[index1][index2] = turnXO
        
        if (playerTurn == 'Player one'){
            playerTurn = 'Player two'
        }else{
            playerTurn = 'Player one'
        }
    }
    console.log(playBoard)
}









