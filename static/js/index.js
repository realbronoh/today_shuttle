// $(document).ready(function () {
//     // $('.memo-wrap').empty();
//     // $("#last-cards").empty();
//     showCards();
//   });


// function showCards() {
//     $.ajax({
//         type: "GET",
//         url: "/allshuttles",
//         data: {},
//         success: function (response) {
//             let cards = response["allshuttle"];
//             for (let i = 0; i < cards.length; i++) {
//                 for (let j = 0; j < cards[i]['content'].length; j++) {
//                     makeCard(cards[i]['data'], cards[i]['winner'], i, j)
//                 }
//             }
//         }
//     })
// }

// function makeCard(days, winners, i, j) {  // 진자템플릿 라우팅 필요
//     let temp_html = `
//     <div class="wrap">
//       <div class="p-5 mb-4 bg-light rounded-3">
//         <div class="container-fluid py-5">
//             <h1 class="display-5 fw-bold">${days}의 셔틀 : ${winners}</h1>
//             <div class="input-box">
//             </div>
//             <div class="memo-wrap">
//             {% for shuttle in shuttles %}
//                 <div class="memo-list">
//                     <span class="memo-name">{{shuttle[${i}]['content'][${j}]['name']}}</span>
//                     <span class="memo-item">{{shuttle[${i}]['content'][${j}]['item']}}</span>
//             {% endfor %} 
//             </div>
//         </div>
//       </div>
//     </div>
//     `;
//     $("#last-cards").append(temp_html);
// }

// function showMemos() {
//     $.ajax({
    //         type: "GET",
    //         url: "",
    //         data: {},
//         success: function(response) {
    //             let item_memos = response['memos'];  // 메모창 받아오기
//             for (let i = 0; i < item_memos.length; i++) {
    //                 for (let j = 0; j < item_memos[i]['content'].length; j++)
    //                 makeMemo(item_memos[i]['content'][j]['name'], item_memos[i]['content'][j]['item'], j)
//             }
//         }
//     })
// }

// function makeMemo(name, item, j) {
//     let temp_memos = `
//     <div class="memo-list">
//         <span class="memo-name">${name}</span>
//         <span class="memo-item">${item}</span>
//         <span class="memo-del${j}"><button class="btn btn-dark btn-sm">삭제</button></span>
//     </div>
//     `;
//     $('.memo-wrap').append(temp_memos);
//     $(`.memo-del${j}`).click(function() {
    //         deleteBtn(name);
//     })
// }

function postShuttle() {
    let items = $('#post-sub').val();
    // console.log(items);
    $.ajax({
        type: "POST",
        url: "/additem",  // 라우트
        data: {items_give: items}, // 아이템 보내기 
        success: function(response) {
            if (response["result"] == "success") {
                alert('제출이 완료됐습니다!');
                window.location.reload();
            } else {
                alert('로그인 먼저 하삼');
            }
        },
        error: function(response){
            alert(response.responseJSON.error);
            window.location.reload();

        }
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

///////////////////////////////////////////////
// Delete Button  (노진형)

function handleDeleteBtn(id, date){
    $.ajax({
        type: "POST",
        url: "/deleteitem",
        data: { _id: id,
                date: date},
        success: function(response){
            alert(response.success);
            console.log(response);
            window.location.href = '/';

        },
        error: function(response){
            alert(response.responseJSON.error);
            window.location.href = '/';
        }
    })
}
