# 🥕 AI 챗봇과 라이브 스트리밍 기능이 있는 당근 마켓 클론코딩 (당근빳따조)

## 프로젝트 요약
- ESTsoft 오르미 2기 교육과정 중 한 django 미니 프로젝트로, 당근 마켓을 클론코딩 해보았습니다.
- 기존의 당근마켓의 핵심 기능인 매물 작성, 수정, 삭제, 동네인증, 채팅 기능을 구현하였으며 chatGPT 3.5 모델을 사용한 AI 챗봇과 라이브 스트리밍, 길찾기 기능을 추가로 구현하였습니다.

<br>

## 팀원 소개
|김유진(조장)|오준경|이진혁|이채림|
|:----:|:-----:|:----:|:----:|
| <a href="https://github.com/superkingyj" target="_blank"> <img src="https://avatars.githubusercontent.com/u/43868490?v=4" alt="김유진 프로필" style="width:150px; border-radius:50px"/> </a> | <a href="https://github.com/Jun-Kyeong" target="_blank"><img src="https://avatars.githubusercontent.com/u/68678903?v=4" alt="오준경 프로필" style="width:150px; border-radius:50px"/> </a>|<a href="https://github.com/jhyeokqq" target="_blank"> <img src="https://avatars.githubusercontent.com/u/130131572?v=4" alt="이진혁 프로필" style="width:150px; border-radius:50px"/></a>|<a href="https://github.com/samkimpepper" target="_blank"> <img src="https://avatars.githubusercontent.com/u/62634206?v=4" alt="이채림 프로필" style="width:150px; border-radius:50px"/></a>|
|채팅 개발|매물 검색 개발|매물 작성/수정/삭제 개발|알림 개발|
|AI 챗봇 개발|매물 목록 개발|동네 인증 개발|거래 후기 작성 개발|
|라이브 스트리밍 개발|길찾기 개발||메인 페이지 개발|

<br>

## 시연 영상
![](https://velog.velcdn.com/images/superkingyj/post/64ffa5b2-7795-451d-8e41-f95c28b83cac/image.png)
[시연영상 바로가기](https://drive.google.com/file/d/1grJwfuvhS79rN4UTsMU5ZNch9RWpuN2E/view?resourcekey)

<br>

## 상세 기능
<details>
<summary>1. 로그인 페이지</summary>
<div markdown="1">
    <li>아이디와 비밀번호로 로그인을 할 수 있다.</li>
    <li>아이디외 비밀번호로 회원가입을 할 수 있다.</li>
    <li>로그인시 메인 페이지로 리다이렉트 된다.</li>
    <li>로그인시 채팅을 할 수 있다.</li>
    <li>로그아웃을 할 수 있다.</li>
</div>
</details>
<br>


<details>
<summary>2. 메인 페이지</summary>
<div markdown="1">
    <li>당근마켓 앱 구글 플레이 스토어로 갈 수 있다.</li>
    <li>당근마켓 앱 앱 스토어로 갈 수 있다.</li>
    <li>동네 인증을 할 사람은 인기매물 더보기 링크로 인기매물 페이지로 갈 수 있다.</li>
    <li>동네 인증을 하지 않은 사람이 인기매물 더보기 링크 클릭시 동네 인증 페이지로 리다이렉트 된다.</li>
    <li>중고거래 인기 매물을 8개 볼 수 있다.</li>
</div>
</details>

<br>

</details>
<details>
<summary>3. 인기 매물 페이지</summary>
<div markdown="1">
    <li>지역에서 인기순으로 인기매물을 볼 수 있다.</li>
    <li>각 매물의 사진, 가격, 동네, 채팅수, 조회수를 볼 수 있다.</li>
    <li>각 매물 클릭시 매물 상세 페이지로 갈 수 있다.</li>
    <li>거래 완료된 글은 거래 완료 표시가 뜬다.</li>
</div>
</details>

<br>

</details>
<details>
<summary>4. 매물 상세 페이지</summary>
<div markdown="1">
    <li>판매자 아이디, 위치, 글 제목, 내용, 가격, 희망 거래 장소, 조회수를 볼 수 있다.</li>
    <li>구매자는 판매자와 채팅페이지로 리다이렉트 할 수 있다.</li>
    <li>구매자는 마음에 드는 매물에 좋아요를 누를 수 있다.</li>
    <li>판매자 자신의 글을 수정할 수 있다.</li>
    <li>판매자는 자신의 글을 삭제할 수 있다.</li>
    <li>판매자는 자신의 글을 거래완료로 표시할 수 있다.</li>
</div>
</details>

<br>

</details>
<details>
<summary>5. 매물 작성 페이지</summary>
<div markdown="1">
    <li>글 제목을 작성할 수 있다.</li>
    <li>매물 가격을 작성할 수 있다.</li>
    <li>매물 설명을 적을 수 있다.</li>
    <li>거래 희망 장소를 지도에서 선택하여 작성할 수 있다.</li>
</div>
</details>

<br>

</details>
<details>
<summary>6. 검색 결과 페이지</summary>
<div markdown="1">
    <li>검색어와 글 제목이 일치하는 글을 볼 수 있다.</li>
    <li>검색한 지역과 글 작성자의 지역이 일치하는 글을 볼 수 있다.</li>
    <li>각 물품의 사진, 가격, 동네, 채팅수, 조회수를 볼 수 있다.</li>
    <li>각 거래 클릭시 거래 상세 페이지로 갈 수 있다.</li>
    <li>거래 완료된 글은 후순위로 출력한다.</li>
</div>
</details>

<br>

</details>
<details>
<summary>7. 채팅 페이지</summary>
<div markdown="1">
    <li>AI 챗봇과 채팅을 할 수 있다. </li>
    <li>AI 챗봇은 가장 위에 위치하며 채팅 페이지 첫 진입시에도 존재한다.</li>
    <li>채팅을 했던 사람들과의 채팅 목록을 볼 수 있다.</li>
    <li>채팅 목록은 마지막 채팅 기록의 최신순으로 정렬된다.</li>
    <li>채팅 목록 클릭시 해당 채팅 기록을 볼 수 있다.</li>
    <li>구매자는 판매자와 채팅을 할 수 있다.</li>
    <li>구매자가 판매자에게 채팅을 보내면 매물의 채팅수가 +1 된다.</li>
    <li>읽지 않은 메시지가 있는 채팅은 new!가 채팅 목록 옆에 표시된다.</li>
    <li>읽지 않은 메시지가 있는 채팅만 볼 수 있다.</li>
    <li>리다이렉트 된 매물 상세 페이지를 볼 수 있다.</li>
    <li>매물 정보를 클릭하면 매물 상세 페이지로 갈 수 있다.</li>
    <li>현재 매물의 거래 상태를 볼 수 있다.</li>
    <li>거래 완료를 누를 수 있다.</li>
</div>
</details>

<br>

</details>
<details>
<summary>8. 동네 인증 페이지</summary>
<div markdown="1">
    <li>동네 주소를 입력하여 내 위치를 설정할 수 있다.</li>
    <li>지도를 통하여 현재 위치를 볼 수 있다.</li>
    <li>지도에서 보이는 현재위치와 입력한 주소의 위치가 같을 때 동네 인증을 할 수 있다.</li>
</div>
</details>

<br>

</details>
<details>
<summary>9. 추가 기능 </summary>
<div markdown="1">
    <li>판매자가 거래를 완료하면 후기를 보낼 수 있다.</li>
    <li>구매자는 판매자와의 거래에 대해 별로에요 / 좋아요 / 최고에요를 선택할 수 있다</li>
    <li>판매자는 별로에요 / 좋아요 / 최고에요 를 통해 매너 온도가 정해진다.</li>
    <li>판매자의 매너 온도를 볼 수 있다.</li>
    <li>내 위치로부터 거래희망장소까지의 경로를 볼 수 있다.</li>
    <li>서로 실시간 스트리밍 화면을 볼 수 있다</li>
</div>
</details>

<br>

## 개발 소감
- **김유진**: 장고 channels로 개발해 보는것이 처음이라 첫째날, 이튿날 까지 작업이 별로 된게 없었는데 절 믿고 응원해준 팀원들에게 정말 감동받았습니다. 어렵긴 했지만 채팅, 라이브 스트리밍 구현하면서 한단계 성장하게되어 기쁩니다.

<br>

- **오준경**: 블로그 프로젝트에 비해서 필요한 기능도 더 많았고 시간도 짧았던것 같지만 다들 너무 잘하시고 추석 연휴에도 열심히 해주시는 모습에 귀감을 받았습니다. 일부 코드들에 대해 동작원리를 잘 이해하지 못하고 넘어간 부분이 있어 많이 부족함을 느꼈고 더 공부해야겠다는 생각이 들었습니다.
어렵기도 했지만 가장 재밌는 프로젝트 시간이었던것 같습니다.

<br>

- **이진혁**: 어려운 부분이 있었지만 해결했을때 성취감을 느껴 좋았습니다. 훌륭한 팀원들과 함께 작업할 수 있어서 많이 배우고 감사했습니다.

<br>

- **이채림**: 이전의 프로젝트를 하면서 느꼈던 아쉬운 점을 이번 프로젝트 때 해결하며 보람을 느낄 수 있었습니다. 좋은 팀원분들과 함께할 수 있어서 좋았습니다.

<br>

## 인상 깊었던 기능
- **채팅 읽음 처리**
    - 캐시를 사용하여 connection이 맺어질 때마다 유저 아이디를 캐시에 저장한다. 
    - 메시지를 받을 때, 다른 사람의 캐시에 나의 아이디가 있는지 확인하여 상태를 True 또는 False로 설정. connection이 끊어지면 유저 아이디를 삭제하여 메시지를 읽었는지 여부를 확인할 수 있다. 

<br>

- **동네 인증**
    - 지도를 불러오고 마커를 찍으며 내 위치를 GPS로 불러오는 등의 API들이 인상깊었다. 이러한 기능들을 사용하여 우리는 자신의 위치를 확인하고 동네를 인증할 수 있었다. 
    - 예를 들어, 지도를 불러올 때는 실시간으로 현재 위치를 나타내는 마커를 찍어주는데, 이렇게 하면 어디에서든지 손쉽게 내 위치를 확인할 수 있다. 
    - 또한, GPS를 통해 정확한 위치 정보를 받아와서 동네인증에 사용할 수 있었다. 



