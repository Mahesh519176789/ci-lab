let screen = document.getElementById("screen");
let currentNum = "0";
let storedNum = null;
let currentOp = null;
let clearNext = false;

function refreshScreen() {
    screen.innerText = currentNum;
}

function addDigit(digit) {

    if (clearNext) {
        currentNum = digit;
        clearNext = false;
    }
    else if (currentNum === "0" && digit !== ".") {
        currentNum = digit;
    }
    else if (digit === "." && currentNum.includes(".")) {
        return;
    }
    else {
        currentNum += digit;
    }

    refreshScreen();
}

function setOperator(op) {

    if (currentOp !== null && !clearNext) {
        getResult();
    }

    storedNum = parseFloat(currentNum);
    currentOp = op;
    clearNext = true;
}

function getResult() {

    if (currentOp === null || clearNext) return;

    let secondNum = parseFloat(currentNum);
    let answer;

    switch (currentOp) {
        case "+":
            answer = storedNum + secondNum;
            break;
        case "-":
            answer = storedNum - secondNum;
            break;
        case "*":
            answer = storedNum * secondNum;
            break;
        case "/":
            answer = secondNum === 0 ? "Error" : storedNum / secondNum;
            break;
    }

    currentNum = answer.toString();
    storedNum = null;
    currentOp = null;
    clearNext = true;
    refreshScreen();
}

function resetCalc() {
    currentNum = "0";
    storedNum = null;
    currentOp = null;
    clearNext = false;
    refreshScreen();
}

function removeDigit() {
    if (currentNum.length > 1) {
        currentNum = currentNum.slice(0, -1);
    } else {
        currentNum = "0";
    }
    refreshScreen();
}
