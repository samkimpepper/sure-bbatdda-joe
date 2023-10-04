var modal = document.querySelector(".modal");
var trigger = document.querySelector(".trigger");
var closeButton = document.querySelector(".close-button");
var submitButton = document.querySelector('#submit');
var cancelButton = document.querySelector("#cancel");
let sellerId = -1;
let goodsId = -1;

function toggleModal(_sellerId, _goodsId) {
    sellerId = _sellerId;
    goodsId = _goodsId;
    console.log(goodsId);
    modal.classList.toggle("show-modal");


}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

submitButton.addEventListener('click', function () {
    $.ajax({
        url: '/goods/trade/complete/' + goodsId + '/',
        type: 'POST',
        success: function(data) {
            console.log(data);
        }
    });
    const tradeCompleteBtn = document.querySelector('#trade-complete');
    tradeCompleteBtn.classList.remove("trade-not-complete");
    tradeCompleteBtn.classList.add("trade-complete");
    tradeCompleteBtn.innerHTML = '거래완료';

    // 채팅에서 아마 쿼리스트링으로 seller, 매물 정보를 보내줘야합니다
    window.location.href = `/goods/trade/review/?goodsId=${goodsId}&sellerId=${sellerId}`;
});

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
cancel.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);