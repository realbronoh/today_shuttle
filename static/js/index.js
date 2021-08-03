$(document).ready(function () {
    // $("#last-cards").empty();
    showCards();
  });


function showCards() {
    $.ajax({
        type: "GET",
        url: "",
        data: {},
        success: function (response) {
            let cards = response[""];  // 값 정하기
            for (let i = 0; i < cards.length; i++) {
                for (let j = 0; j < cards[i]['이름'].length; j++) {
                    makeCard(cards[i]['날짜'], cards[i]['당첨자'], cards[i][j]['이름'], cards[i][j]['아이템'])
                }
            }
        }
    })
}

// 함수 인자(날짜, 당첨자, 셔틀별 이름, 셔틀별 아이템) <-- 이름, 아이템은 또 for문 실시
function makeCard(days, winners, name, items) {
    let temp_html = `
    <div class="wrap">
      <div class="p-5 mb-4 bg-light rounded-3">
        <div class="container-fluid py-5">
            <h1 class="display-5 fw-bold">${days}의 셔틀 : ${winners}</h1>
            <div class="input-box">
            </div>
            <div class="memo-wrap">
            <div class="memo-list">
                <span class="memo-name">장덕수</span>
                <span class="memo-item">슬리퍼, 물티슈</span>
            </div>
            <div class="memo-list">
                <span class="memo-name">노진형</span>
                <span class="memo-item">휴지</span>
            </div>
            <div class="memo-list">
                <span class="memo-name">우정범</span>
                <span class="memo-item">바디워시, 샴푸</span>
            </div>
            </div>
        </div>
      </div>
    </div>
    `
}