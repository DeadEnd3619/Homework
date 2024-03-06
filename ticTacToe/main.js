var playBoard = [0,0,0,0,0,0,0,0,0],playerTurn = 'Player one',turnXO = 'X',winningPos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]],turns = 0,game = true, formerTurn = 'X', winningPlayer = ''
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('player').innerHTML = playerTurn
})
function getBoardPos(playBoardPos){
    var index = playBoardPos - 1
    if (playerTurn == 'Player one'){
        turnXO = 'X'
    }else{
        turnXO = 'O'}
    if (playBoardPos == 1 || playBoardPos == 2 || playBoardPos == 3){
        doPlayerAction(index)
    }else if (playBoardPos == 4 || playBoardPos == 5 || playBoardPos == 6){
        doPlayerAction(index)
    }else{
        doPlayerAction(index)}}
function doPlayerAction(index){
    if (playBoard[index] == 0){
        playBoard[index] = turnXO
        doHTMLEdit(index, 1)
        turns++}
    else{
        console.log('invalid input')}
    let boolBoard = [Boolean(playBoard[0]), Boolean(playBoard[1]), Boolean(playBoard[2]), Boolean(playBoard[3]), Boolean(playBoard[4]), Boolean(playBoard[5]), Boolean(playBoard[6]), Boolean(playBoard[7]), Boolean(playBoard[8])]
    for (let i of winningPos){
        let i1 = i[0], i2 = i[1], i3 = i[2];
        if (boolBoard[i1] && boolBoard[i2] && boolBoard[i3]){
            if (playBoard[i1] == playBoard[i2] && playBoard[i2] == playBoard[i3]){
                game = false;
                winningPlayer = playBoard[i1]
                doHTMLEdit(index, 2)
            }}}
    if (turns == 9 && game == true){
        game = false
        winningPlayer = 'Tie'
    doHTMLEdit(index, 2)}}
function doHTMLEdit(index, condition){
    if (condition == 1){
    document.getElementById(index + 1).innerHTML = turnXO
    if (playerTurn == 'Player one'){
        playerTurn = 'Player two'
    }else{
        playerTurn = 'Player one'}
        document.getElementById('player').innerHTML = playerTurn}
    if (condition == 2){
        if (winningPlayer = 'X'){
            winningPlayer = 'Player one'
        }else{
            winningPlayer = 'Player two'
        }
        if (winningPlayer == 'Tie'){
            document.getElementById('player').innerHTML = "It's a tie"
        }else{
        document.getElementById('player').innerHTML = `${winningPlayer} has won`
    }}}








