var gameArea;
var previousState;

function generateWaitingHtml(gameState) {
    var html = `Players:
                <ul>`;

    for (player of gameState.players) {
        html += '<li>' + player.player_id + '</li>'
    }

    html += '</ul><br>'

    html += `<form id='startGameButton' action='/lobby/` + lobbyId + `/start' method='post'>
            <div>
                <input type='submit' value='Start the game'>
            </div>
            </form>`


    return html;
}

function fixStartGame() {
    document.getElementById('startGameButton').addEventListener('submit', (function (e) {
        e.preventDefault();

        var request = new XMLHttpRequest();
        request.open('POST', '/lobby/' + lobbyId + '/start');
        request.send();

        refreshContent();
    }));

}

function generateGameEndedHtml(gameState) {
    var html = 'Game ended! Final standings:';

    gameState.players.sort((a, b) => { return b['score'] - a['score'] })

    html += '<ul>';

    for (player of gameState.players) {
        html += '<li> Player name: ' + player.player_id;
        html += '<br>';
        html += 'Score: ' + player.score;
        html += '</li>';
    }

    html += '</ul>'

    return html;
}

function generateRoundEndedHtml(gameState) {
    var html = `Answers given:
                <ul>`;

    for (player of gameState.players) {
        html += '<li> Player name:' + player.player_id;
        html += '<ul>';

        html += '<li> Title:';
        if (player['round_no'] == gameState['round']) {
            if (player['correct_title']) {
                html += '<div style="color:green">' + player['last_title'] + '</div>';
            }
            else {
                html += '<div style="color:red">' + player['last_title'] + '</div>';
            }
        }
        html += '</li>';

        html += '<li> Author:';
        if (player['round_no'] == gameState['round']) {
            if (player['correct_author']) {
                html += '<div style="color:green">' + player['last_author'] + '</div>';
            } else {
                html += '<div style="color:red">' + player['last_author'] + '</div>';
            }
        }
        html += '</li>';

        html += '<li> Source:';
        if (player['round_no'] == gameState['round']) {
            if (player['correct_source']) {
                html += '<div style="color:green">' + player['last_source'] + '</div>';
            } else {
                html += '<div style="color:red">' + player['last_source'] + '</div>';
            }
        }
        html += '</li>';

        html += '</ul></li>';
    }

    html += '</ul>'

    return html;
}

function generateGuessingTimeHtml(gameState) {
    var html = `Guessing Time
    <iframe width="1" height="1"
        src = '` + gameState.url + `'
        hidden allow = 'autoplay'>
    </iframe>
    <form id='answerForm'>
    <div >
        <label for="title">Enter song title: </label>
        <input type="text" name="title" id="title">
    </div>
    <div >
        <label for="author">Enter song author: </label>
        <input type="text" name="author" id="author">
    </div>
    <div >
        <label for="source">Enter song source: </label>
        <input type="text" name="source" id="source">
    </div>
    <div>
        <input type="submit" value="Submit">
    </div>
    </form>`;

    return html;
}

function fixAnswer(gameState) {
    var form = document.getElementById('answerForm');
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        var formData = new FormData(form);
        formData.append('round', gameState.round);
        var request = new XMLHttpRequest();
        request.open('POST', '/lobby/' + lobbyId + '/answer');
        request.send(formData);
    });

}



function refreshContent() {
    var request = new XMLHttpRequest();
    request.onload = () => {
        var gameState = JSON.parse(request.response);
        if (gameState.game_state != previousState || gameState.game_state == 'waiting_for_players') {
            switch (gameState.game_state) {
                case 'waiting_for_players':
                    gameArea.innerHTML = generateWaitingHtml(gameState);
                    fixStartGame();
                    break;
                case 'game_ended':
                    gameArea.innerHTML = generateGameEndedHtml(gameState);
                    break;
                case 'round_ended':
                    gameArea.innerHTML = generateRoundEndedHtml(gameState);
                    break;
                case 'guessing_time':
                    gameArea.innerHTML = generateGuessingTimeHtml(gameState);
                    fixAnswer(gameState);
                    break;
            }
        }

        previousState = gameState.game_state;

        window.setTimeout(refreshContent, 200);
    }
    request.open('GET', '/lobby/' + lobbyId + '/state');
    request.send();
}


window.onload = () => {
    gameArea = document.getElementById('GameArea');
    window.setTimeout(refreshContent, 200);
}