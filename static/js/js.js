let buttons_open = document.querySelectorAll('.open-btn');
let buttons_green = document.querySelectorAll('.btn-green');
let sections = document.querySelectorAll('.sinformation-box');

for(let i = 0;i < buttons_open.length;i++){
    buttons_open[i].addEventListener('click', (e)=>{
        sections[i].classList.toggle("open-section");
        buttons_open[i].classList.toggle("open-btn-active");
    })
}

for(let i = 0; i < buttons_green.length;i++){
    buttons_green[i].addEventListener('click', (e)=>{
        document.querySelectorAll('.change-form')[i].classList.toggle('active');
    });
}

let button_exit = document.querySelectorAll('.exit');
for(let i= 0;i < button_exit.length; i++){
    button_exit[i].addEventListener('click', (e)=>{
        document.querySelectorAll('.change-form')[i].classList.toggle('active');
    });
}

let button_settings = document.querySelector('.settings-btn');
button_settings.addEventListener('click', (e)=>{
    document.querySelector('.settings-ul').classList.toggle('active');
});

let buttons_profile = document.querySelectorAll('.change-profile-btn');
for(let i = 0; i < buttons_profile.length; i++){
    buttons_profile[i].addEventListener('click', (e)=>{
        document.querySelectorAll('.profile-form')[i].classList.toggle('active');
    });
}