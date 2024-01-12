let questions = [
    ['Sonic the Hedgehog is a blue character. True or False?', 'True'],
    ['Tetris is a game where you arrange falling blocks. True or False?', 'True'],
    ['"Pokémon" is short for "Pocket Monsters." True or False?', 'True'],
    ['The main character in "The Legend of Zelda" series is named Zelda. True or False?', 'True'],
    ['Minecraft allows players to build and explore blocky worlds. True or False?', 'True'],
    ['"Pac-Man" was released in the 1980s. True or False?', 'True'],
    ['In "Super Mario Bros.," Marios brother is named Luigi. True or False?', 'True'],
    ['"Fortnite" is a game that features a battle royale mode. True or False?', 'True'],
    ['The iconic yellow character in "Pac-Man" is called Blinky. True or False?', 'True'],
    ['"Angry Birds" is a mobile game where birds are launched at structures. True or False?', 'True']
]
let score = 0
let popUp, question


//Above is where is create my variables. 


for (question of questions){
    let input = prompt(question[0])
    if (input == question[1]){
        score++
    }else if(input.length == 0){
        alert('Please type in a vaild responce')
    }else{
        null
    }
}



//The above is the basic quiz loop. I use a for loop using a nested array to store the question and the answer.



if (score <= 6){
    popUp = 'Try again'
}else if(score <= 8){
    popUp = 'Good job'
}else if(score >= 9){
    popUp = 'Excellent'
}


//This determines what the popup is when the quiz is completed using simple if and else if statesments.



alert(popUp + '\nYou got a ' + score + ' out of 10!')


//This displays the final score after the quiz is completed with a message then on the next line the final score