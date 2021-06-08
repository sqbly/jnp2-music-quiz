var gameArea;
var previousState;
function refreshContent() {
    var request = new XMLHttpRequest();
    request.open('GET', '/lobby/' + lobbyId + '/state');
    request.send();
    
    var gameState = JSON.parse(request.response);
    if (gameState.game_state != previousState) {
        switch (gameState.game_state) {
            case 'waiting_for_players':
                gameArea.innerHTML = '';
                break;
            case 'game_ended':
                gameArea.innerHTML = '';    
                break;
            case 'round_ended':
                gameArea.innerHTML = '';
                break;
            case 'guessing_time':
                gameArea.innerHTML = '';
                break;
        }
    }
    
    previousState = gameState.game_state;
}


window.onload = () => {
    gameArea = document.getElementById('GameArea');
    var intervalId = window.setInterval(refreshContent, 100);
}   