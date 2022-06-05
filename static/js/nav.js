const signinupBtn = document.querySelector('#signin-up-btn');
const signoutBtn=document.querySelector('#signout-btn')
const memberPage=document.querySelector('#member-page')
const userApi = '/api/user';


//進入頁面後先檢查使用者有沒有登入
 async function signinCheck(){
    const response=await fetch(userApi,{method:'GET'});
    const result= await response.json();
    
    if(result.data){
        signinupBtn.classList.remove('show');
        signoutBtn.classList.add('show');
        memberPage.classList.add('show');
        
        
    }else{
        signinupBtn.classList.add('show');
        signoutBtn.classList.remove('show');
        memberPage.classList.remove('show');
        
    }
       
}
signinCheck()




//登出
function signout(){
    fetch(userApi, {
        method: 'DELETE'
    })
    .then(() => {
        location.reload();

    })
}

signoutBtn.addEventListener('click', signout);

const memberapi=`/api/member`


memberPage.addEventListener("click",async(e)=>{
    const response=await fetch(userApi);
    const promise=await response.json();
    const result =await promise;
    if (result.data){
        location.replace('/member')
            
        }else{
            location.replace('/login');
        }
});



// navbar ham icon
const ham = document.querySelector('.ham')
const navLink = document.querySelector('.nav-link')

function toggleNavLink(){
    navLink.classList.toggle('show')
}

ham.addEventListener('click', toggleNavLink)



