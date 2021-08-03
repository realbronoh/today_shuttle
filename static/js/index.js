$(document).ready(function () {
    // $('.memo-wrap').empty();
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
                    makeCard(cards[i]['날짜'], cards[i]['당첨자'], i, j)
                }
            }
        }
    })
}

// 함수 인자(날짜, 당첨자, 셔틀별 이름, 셔틀별 아이템) <-- 이름, 아이템은 또 for문 실시
function makeCard(days, winners, i, j) {
    let temp_html = `
    <div class="wrap">
      <div class="p-5 mb-4 bg-light rounded-3">
        <div class="container-fluid py-5">
            <h1 class="display-5 fw-bold">${days}의 셔틀 : ${winners}</h1>
            <div class="input-box">
            </div>
            <div class="memo-wrap">
            {% for memo in memos %}
                <div class="memo-list">
                    <span class="memo-name">{{memo[${i}][${j}]['이름']}}</span>
                    <span class="memo-item">{{memo[${i}][${j}]['아이템']}}</span>
            {% endfor %}
            </div>
        </div>
      </div>
    </div>
    `;
    $("#last-cards").append(temp_html);
}

function postShuttle() {
    let items = $('input-item').val();

    $.ajax({
        type: "POST",
        url: "",  // 라우트
        data: {items_give: items}, // 아이템 보내기 
        success: function(response) {
            if (response["result"] == "success") {
                alert('제출이 완료됐습니다!');
                window.location.reload();
            }
        }
    })
}

function showMemos() {
    $.ajax({
        type: "GET",
        url: "",
        data: {},
        success: function(response) {
            let item_memos = response['memos'];  // 메모창 받아오기
            for (let i = 0; i < item_memos.length; i++) {
                makeMemo(item_memos[i]['이름'], item_memos[i]['아이템'], i)
            }
        }
    })
}

function makeMemo(name, item, i) {
    let temp_memos = `
    <div class="memo-list">
        <span class="memo-name">${name}</span>
        <span class="memo-item">${item}</span>
        <span class="memo-del${i}"><button class="btn btn-dark btn-sm">삭제</button></span>
    </div>
    `;
    $('.memo-wrap').append(temp_memos);
    $(`.memo-del${i}`).click(function() {
        deleteBtn(name);
    })
}

function deleteBtn(name) {
    $.ajax({
        type: "POST",
        url: "",  // 삭제 라우팅
        data: {'name-give':name},
        success: function (response) {  // 세션별로 삭제기능 분리해야 함
            if (response["result"] == "success") {
                alert('삭제 완료!');
                window.location.reload();
            }
        }
    })
}