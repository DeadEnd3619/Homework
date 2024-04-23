const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let keyAction = function (key) {
    if (key == 'w') {
        $('#player').animate({top: "-=10px"}, 33); 
    } else if (key == 's') {
        $('#player').animate({top: "+=10px"}, 33);
    } else if (key == 'a') {
        $('#player').animate({left: "-=10px"}, 33); 
    } else if (key == 'd') {
        $('#player').animate({left: "+=10px"}, 33); 
    }
};

$(document).on("keydown", (e) => {
    if (canLogInput) {
        console.log(e.key);
        canLogInput = false;
        keyAction(e.key);
    }
});

// async function game() {
//     let startTime, elapsedTime;
//     while (Game) {
//         startTime = Date.now();
//         await sleep(Math.max(0, 1000 / 30 - elapsedTime));
//         lastKey =  keyLog[keyLog.length - 1][0];
//         canLogInput = true;
//         pressedKey = "";
//         elapsedTime = Date.now() - startTime;
//     }
// }

// game();
