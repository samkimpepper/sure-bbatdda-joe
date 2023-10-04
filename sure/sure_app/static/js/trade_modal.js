var modal = document.querySelector(".modal"); 
var trigger = document.querySelector(".trigger"); 
var closeButton = document.querySelector(".close-button"); 
var submitButton = document.querySelector('#submit');
var cancelButton = document.querySelector("#cancel");

console.log(trigger);

function toggleModal() { 
    modal.classList.toggle("show-modal"); 
}

function windowOnClick(event) { 
    if (event.target === modal) { 
        toggleModal(); 
    } 
}

submitButton.addEventListener('click', function() {
    // 채팅에서 아마 쿼리스트링으로 seller, 매물 정보를 보내줘야합니다
    window.location.href = '/goods/trade/review/';
});

trigger.addEventListener("click", toggleModal); 
closeButton.addEventListener("click", toggleModal); 
cancel.addEventListener("click", toggleModal); 
window.addEventListener("click", windowOnClick); 

