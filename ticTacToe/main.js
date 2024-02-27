var playBoard = [0,0,0,0,0,0,0,0,0],playerTurn = 'Player one',turnXO = 'X',winningPos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]],turns = 0,game = true, formerTurn = 'X'
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
        doHTMLEdit(index)
        turns++
        if (playerTurn == 'Player one'){
            playerTurn = 'Player two'
        }else{
            playerTurn = 'Player one'}}
    else{
        console.log('invalid input')}
    let boolBoard = [Boolean(playBoard[0]), Boolean(playBoard[1]), Boolean(playBoard[2]), Boolean(playBoard[3]), Boolean(playBoard[4]), Boolean(playBoard[5]), Boolean(playBoard[6]), Boolean(playBoard[7]), Boolean(playBoard[8])]
    for (let i of winningPos){
        let i1 = i[0], i2 = i[1], i3 = i[2];
        if (boolBoard[i1] && boolBoard[i2] && boolBoard[i3]){
            if (playBoard[i1] == playBoard[i2] && playBoard[i2] == playBoard[i3]){
                console.log('winner');
                game = false;}}}
    if (turns == 9 && game == true){
        console.log('Tie')}}
function doHTMLEdit(index){
    document.getElementById(index + 1).innerHTML = turnXO
    console.log(playBoard)}








