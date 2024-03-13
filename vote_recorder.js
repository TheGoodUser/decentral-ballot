window.addEventListener("DOMContentLoaded", () => {
    let parties = document.querySelectorAll('.party');

    const socket = new WebSocket("ws://localhost:8765");

    socket.onopen = () => {
        console.log('Connected to server');
    };

    parties.forEach(party => {
        party.addEventListener('click', function(event) {
            event.preventDefault();
            let id = party.querySelector('p').id;
            socket.send(id);
        });
    });

    socket.onmessage = (event) => {
        let elibible = event.data;
        votesDiv = document.querySelector('.votes');
        if (event.data == "1"){
            document.querySelector('button').innerHTML = "Eligible";
            votesDiv.style.pointerEvents = 'auto';
        }else {
            document.querySelector('button').innerHTML = "Not Eligible";
            votesDiv.style.pointerEvents = 'none';
        }
    };

    document.querySelector('button').addEventListener('click', function(event) {
        event.preventDefault();
        socket.send(document.querySelector('input').value);
    });    

});




















