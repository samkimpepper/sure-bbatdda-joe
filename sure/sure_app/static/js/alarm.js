
$(document).ready(function() {
    var user_id = document.getElementById('user_id').textContent;
    console.log(user_id);

    const socket = new WebSocket(`ws://127.0.0.1:8000/ws/alarm/?user_id=${user_id}`);

    socket.addEventListener('open', (event) => {
        console.log('WebSocket 연결이 열렸습니다.');
    });

    socket.addEventListener('message', (event) => {
        const data = JSON.parse(event.data);
        console.log('서버로부터 데이터 수신:', data);
        console.log(data.content);
        
    });

});