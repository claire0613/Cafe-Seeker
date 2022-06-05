

const signContainers = document.querySelectorAll('.sign-container')
const signpage=document.querySelector('.signpage')

const emailPattern = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;

//變換登入、註冊欄位
function changeSignContainer(){
    signContainers.forEach(container=>{
        container.classList.toggle('show');
    })
}
signContainers.forEach(container => {
    const convertBtn = container.querySelector('.convert-sign');
    convertBtn.addEventListener('click', changeSignContainer);
})












// 登入、註冊功能
const signupForm = document.querySelector('#signup');
const signinForm = document.querySelector('#signin');


// 註冊
async function signup(e){
    e.preventDefault();
    if(isValid("signup")){
        let data = {
            username : this.querySelector('input[name="username"]').value,
            email : this.querySelector('input[name="email"]').value,
            password : this.querySelector('input[name="password"]').value 
        }
        await fetch(userApi, {
            method: 'POST',
            headers: new Headers({
                'Content-Type': 'application/json'
              }),
            body: JSON.stringify(data)
          
        })
        .then(res => {
            return res.json();
    
        })
     
        .then(result => {
           
            const message = this.querySelector('.message');
            
            if(result.ok){
                message.innerText = '註冊成功';
                e.target.value='';
                changeSignContainer()
            }else{
                message.innerText = result.message;
            }
        })

    }


   
}
signupForm.addEventListener('submit', signup)

//登入
async function signin(e){
    e.preventDefault()
    if(isValid("signin")){
        let data ={
            email:this.querySelector('input[name="email"]').value,
            password:this.querySelector('input[name="password"]').value
        }
        await fetch(userApi,{
            method:'PATCH',
            headers: new Headers({
                'Content-Type': 'application/json'
              }),
            body: JSON.stringify(data)
        })
        .then(res=>{return res.json();})
         //如果有成功登入，回到原本頁面並將「註冊｜登入」按鈕改為「登出」按鈕
        .then(result=>{
            if (result.ok){

                signinCheck();
                signinupBtn.classList.remove('show');
                signoutBtn.classList.add('show');
                memberPage.classList.add('show');
                location.replace('/')
            
            }
      
            else{ 
                const message = this.querySelector('.message');
                message.innerText = result.message;
            }
          
        })
    }

}
signinForm.addEventListener('submit', signin)







// const memberapi=`/api/member`


// memberPage.addEventListener("click",async(e)=>{
//     const response=await fetch(userapi);
//     const promise=await response.json();
//     const result =await promise;
//     if (result.data){
//         location.replace('/member')
            
//         }else{
//             showUpSignpage();
//         }
// });



// // navbar ham icon
// const ham = document.querySelector('.ham')
// const navLink = document.querySelector('.nav-link')

// function toggleNavLink(){
//     navLink.classList.toggle('show')
// }

// ham.addEventListener('click', toggleNavLink)

//註冊or登入前確認每項input是否valid
function isValid(checkStatus) {
    let isValid = true;
    const checkList = document.querySelectorAll(`[input-type=${checkStatus}]`);
    for(const checkItem of checkList) {
        if(checkItem.classList.contains("invalid")) {
            isValid = false;
            continue;
        }
        const input = checkItem.querySelector("input");
        // 驗證欄位
        const checkResult = checkData(input.name, input.value);
        // 顯示驗證訊息
        renderCheck(checkItem, checkResult);
        if(checkResult) {
            isValid = false;
        }
    }
    return isValid;
}

function checkData(inputName, inputValue) {
    switch(inputName) {
        case "username":
            if(!inputValue) {
                return "姓名不可為空白";
            }
            break;
        case "email":
            if(!inputValue) {
                return  "電子信箱不可為空白";
            }
            if (!emailPattern.test(inputValue)) {
                return  "電子信箱格式錯誤";
            }
            break;
        case "password":
            if(!inputValue) {
                return  "密碼不可為空白";
            }
            if(inputValue.length < 3) {
                return "密碼長度需超過3位";
            }
            break;
        default:
            break;
    }
    // 驗證成功
    return false;
}


signpage.addEventListener("focusout", (e) => {
    const target = e.target;
    if(target.nodeName == "INPUT") {
        // 驗證欄位
        const checkResult = checkData(target.name, target.value);
        // 顯示驗證訊息
        renderCheck(target.parentElement, checkResult);
    }
});

function renderCheck(parent, checkResult) {
    const message = parent.querySelector(".user-input-msg > span");
    if(checkResult) {
        // input 加上效果
        parent.classList.add("invalid");
        parent.classList.remove("valid");
        // 訊息 加上效果
        message.textContent = checkResult;
        message.parentElement.classList.add("invalid");
        message.parentElement.classList.remove("valid");
    } else {
        // input 移除效果
        parent.classList.remove("invalid");
        parent.classList.add("valid");
        // 訊息 加上效果
        message.innerText = "驗證成功";
        message.parentElement.classList.remove("invalid");
        message.parentElement.classList.add("valid");
    }
}








// // 登入/註冊流程
// const signupForm = document.querySelector('form.signup')

// async function signup(e){
//     e.preventDefault()
//     const signupData = {
//         email : this.querySelector('input[name="email"]').value,
//         password : this.querySelector('input[name="password"]').value,
//         fromAPI: false
//     }
//     const res = await fetch(userAPI, {
//                     method: 'POST',
//                     body: JSON.stringify(signupData),
//                     headers: {'Content-Type': 'application/json'}
//                 })
//     const data =await res.json()
//     if(data.ok){
//         window.location.replace('/')
//     }else{
//         const message = this.querySelector('.message')
//         message.innerText = data.message
//     }
// }

// signupForm.addEventListener('submit', signup)



// // Google Signin
// function handleClientLoad() {
//     // Load the API's client and auth2 modules.
//     // Call the initClient function after the modules load.
//     gapi.load('client:auth2', initClient);
// }
// function initClient() {
//     //初始化 GoogleAuth 物件
//     gapi.client.init({
//         'clientId': '46769118537-mq0m5m2589ea8euptnha9903r2a85l18.apps.googleusercontent.com',
//         'cookiepolicy': "single_host_origin",
//         'scope': SCOPE
//     }).then(function () {
//         //傳回 GoogleAuth 物件
//         GoogleAuth = gapi.auth2.getAuthInstance();
        
//         // Listen for sign-in state changes.監聽目前使用者的登入狀態變化。
//         GoogleAuth.isSignedIn.listen(updateSigninStatus);
        
//         // Handle initial sign-in state. (Determine if user is already signed in.)
//         // var user = GoogleAuth.currentUser.get();
//         // setSigninStatus();
        
//         googleBtn.addEventListener('click', ()=>{
//             GoogleAuth.signIn()
//             setSigninStatus()
//         })
//     });
// }
// const googleBtn = document.querySelector('.google-signin')

// function setSigninStatus() {
//     var user = GoogleAuth.currentUser.get();
//     var isAuthorized = user.hasGrantedScopes(SCOPE);
//     if (isAuthorized) {
//         console.log(user.dt.Nt, user.dt.LS)
//         const signupData = {
//             email : `GOOGLE_${user.dt.Nt}`,
//             password : user.dt.LS,
//             fromAPI: true 
//         }
//         fetch(userAPI, {
//             method: 'POST',
//             body: JSON.stringify(signupData),
//             headers: {'Content-Type': 'application/json'}
//         })
//         .then(res => res.json())
//         .then(data => {
//             if(data.ok){
//                 window.location.replace('/')
//             }
//             else{
//                 const message = this.querySelector('.message')
//                 message.innerText = data.message
//             }
//         })

//     } else {
//         console.log('not login')
//     }
// }
// function updateSigninStatus() {
//     setSigninStatus();
// }