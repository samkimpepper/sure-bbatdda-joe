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
        console.log(data.type);

        if(data.alarm_cnt > 0) {
            document.querySelector('.no-alarm').remove();
        }

        if(data.type == "unread_alarms") {
            console.log("unread_alarms");
            $('.alarm_cnt').textContent = data.alarm_cnt;
            console.log(document.getElementById('alarmCnt'));
            console.log($('.alarm_cnt').textContent);
            document.getElementById('alarmCnt').textContent = data.alarm_cnt;
            
            var dropdown = document.querySelector(".dropdown-ul");
            for(let i=0; i<data.alarm_cnt; i++) {
                var li = document.createElement('li');
                li.textContent = data.alarms[i].content;
                li.setAttribute('data-link', data.alarms[i].link);
                li.classList.add('alarm');
                li.setAttribute('data-alarm-id', data.alarms[i].id);
                dropdown.appendChild(li);
            }
            liClickEvent();
            return;
        }
        else if(data.type == "alarm_cnt") {
            document.getElementById('alarmCnt').textContent = data.alarm_cnt;
        }
        
        var dropdown = document.querySelector(".dropdown-ul");
        var a = document.createElement('li');
        a.textContent = data.content;
        a.setAttribute('data-link', data.link);
        a.setAttribute('data-alarm-id', data.alarm_id);
        a.classList.add('alarm');

        dropdown.appendChild(a);
    });
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }

    function liClickEvent(){
        var aElements = document.querySelectorAll('.alarm');

        aElements.forEach(function(a) {
            a.addEventListener('click', function(event) {
                event.preventDefault();
                var alarmId = event.currentTarget.getAttribute('data-alarm-id');
                var link = event.currentTarget.getAttribute('data-link');
    
                // 이제 해당 알람을 읽었다고 서버에 알리기 위해 요청할 건데 HTTP 요청을 할지 웹소켓으로 할지 모르겠음
                $.ajax({
                    url: '/alarm/read/' + alarmId + '/',
                    type: 'POST',
                    crossDomain: true,
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    success: function(data) {
                        window.location.href = link;
                    }
                });
            });
        });
    }


});