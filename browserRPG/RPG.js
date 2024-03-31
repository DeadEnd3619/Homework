const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let Game = true;
let pressedKey = "";
let canLogInput = true;
let keyLog = [];
let keyLogger = function (Key) {
    const previousKey = keyLog[keyLog.length - 1];
    if (previousKey!== Key) {
        keyLog.push(Key);
        console.log(keyLog);
    }
    else{
        
    }
};

window.addEventListener("keydown", (e) => {
    if (canLogInput) {
        pressedKey = e.key;
        console.log(pressedKey);
        canLogInput = false;
        keyLogger(pressedKey);
    }
});

async function game() {
    while (Game) {
        await sleep(33);
        canLogInput = true;
        pressedKey = "";
    }
}
game();
