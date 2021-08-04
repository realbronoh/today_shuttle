const signupForm = document.querySelector("form[name='signup-form']");
const loginForm = document.querySelector("form[name='login-form']");
const changePWForm = document.querySelector("form[name='change-pw-form']");
const createAccountBtn = document.querySelector("#createAccountBtn");
const changePWBtn = document.querySelector('#changePWBtn');

// 계정 생성
function handleSubmit(event) {
    const form = event.target;
    // form 내용을 모두 가져옴 FormData object로
    const formdata = new FormData(form);
    // object 형식으로 변환
    let objectData = {}
    for (let [key, val] of formdata){
        objectData[key] = val;
    }

    $.ajax({
        type: "POST",
        url: "/user/signup",
        data: objectData,
        success: function(response){
            console.log(response);
            window.location.href = "/";
        },
        error: function(response){
            console.log(response);
            const errorBox = event.target.querySelector(".error");
            errorBox.innerText = response.responseJSON.error;
            errorBox.classList.remove("error--hidden");
        }
    })
    event.preventDefault();
}


// 로그인
function handleSubmitLogin(event) {
    const form = event.target;
    // form 내용을 모두 가져옴 FormData object로
    const formdata = new FormData(form);
    // object 형식으로 변환
    let objectData = {}
    for (let [key, val] of formdata){
        objectData[key] = val;
    }
    ////////////////
    console.log(objectData);

    $.ajax({
        type: "POST",
        url: "/user/login",
        data: objectData,
        success: function(response){
            console.log(response);
            window.location.href = "/";
        },
        error: function(response){
            console.log(response);
            const errorBox = event.target.querySelector(".error");
            errorBox.innerText = response.responseJSON.error;
            errorBox.classList.remove("error--hidden");
        }
    })
    event.preventDefault();
}

function handleSubmitChangePW(event) {
    const form = event.target;
    // form 내용을 모두 가져옴 FormData object로
    const formdata = new FormData(form);
    // object 형식으로 변환
    let objectData = {}
    for (let [key, val] of formdata){
        objectData[key] = val;
    }
    ////////////////
    console.log(objectData);

    $.ajax({
        type: "POST",
        url: "/user/change_pw",
        data: objectData,
        success: function(response){
            console.log(response);
            window.location.href = "/";
        },
        error: function(response){
            console.log(response);
            const errorBox = event.target.querySelector(".error");
            errorBox.innerText = response.responseJSON.error;
            errorBox.classList.remove("error--hidden");
        }
    })
    event.preventDefault();
}

// function handleClickCreateAccountBtn(event){
//     const signUpCard = document.querySelector("#sign-up-card");
//     if (signUpCard.classList.contains("hide")){
//         event.target.value = "Close Create Account Card";
//     }
//     else{
//         event.target.value = "CREATE ACCOUNT";
//     }
//     signUpCard.classList.toggle("hide");
// }

// function handleClickChangePWBtn(event){
//     const changePWCard = document.querySelector("#change-pw-card");
//     if (changePWCard.classList.contains("hide")){
//         event.target.value = "Close Change PW Card";
//     }
//     else{
//         event.target.value="CHANGE PASSWORD";
//     }
//     changePWCard.classList.toggle("hide");
// }

$('#change-pw-card').hide();
$('#sign-up-card').hide();

function showSignUpbtn() {
    $('#sign-up-card').show();
    $('#log-in-card').hide();
}

function showChangeBtn() {
    $('#change-pw-card').show();
    $('#log-in-card').hide();
}

function backtoLogin() {
    $('#change-pw-card').hide();
    $('#sign-up-card').hide();
    $('#log-in-card').show();
}


signupForm.addEventListener("submit", handleSubmit);
loginForm.addEventListener("submit", handleSubmitLogin);
changePWForm.addEventListener("submit", handleSubmitChangePW);
// createAccountBtn.addEventListener("click", handleClickCreateAccountBtn);
// changePWBtn.addEventListener("click", handleClickChangePWBtn);