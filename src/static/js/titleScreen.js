// Disable button if no player name
let input = document.querySelector("#playerName");
let button = document.querySelector("#beginGame");

button.disabled = true; //setting button state to disabled

input.addEventListener("change", stateHandle);

function stateHandle() {
    if (document.querySelector("#playerName").value === "") {
        button.disabled = true; //button remains disabled
    } else {
        button.disabled = false; //button is enabled
    }
};