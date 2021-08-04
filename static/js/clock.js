const clock = document.querySelector("span#clock");

function getClock(){
    const date = new Date();
    const minute = 2 - date.getMinutes()%3
    const second = 60 - date.getSeconds()
    
    if ((minute === 2 && second === 60)){
        clock.innerText = `추첨중입니다...`;
    }
    else if (minute === 2 && second === 59){
        clock.innerText = `추첨중입니다...`;
        window.location.href = '/';
    }
    else{
        clock.innerText = `${String(minute).padStart(2,"0")}:${String(second).padStart(2,"0")}`;
    }
}

getClock(); setInterval(getClock, 1000);