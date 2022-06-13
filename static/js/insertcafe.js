const insertForm=document.querySelector('.insertform')
const modifiedMsg = document.querySelector("#modified-msg");
const msgPage = document.querySelector(".msg-page");
async function insertInit(){
    modifiedMsg.innerHTML='';
    const userRes=await fetch(userApi)
    const userResponse=await userRes.json()
    if (!userResponse.data){
        location.replace('/login')
    }


}
insertInit()
insertForm.addEventListener('submit',async(e)=>{
    e.preventDefault();
    modifiedMsg.innerHTML='';
    const userRes=await fetch(userApi)
    const userResponse=await userRes.json()
    if (userResponse.data){
        const cityId=document.querySelector('#city').value
        const name=document.querySelector('input[name="name"]').value
        const address=document.querySelector('#address').value
        const singleSelling=document.querySelector('input[name="single-selling"]').value
        const dessertSelling=document.querySelector('input[name="dessert-selling"]').value
        const mealSelling=document.querySelector('input[name="meal-selling"]').value
        const limitedTime=document.querySelector('input[name="limited_time"]').value
        const socket=document.querySelector('input[name="socket"]').value
        const standingTables=document.querySelector('input[name="standing-table"]').value
        const music=document.querySelector('input[name="music"]').value

        const cashOnly=document.querySelector('input[name="cashonly"]').value

        const outdoorSeating=document.querySelector('input[name="outdoor-seating"]').value
        const animals=document.querySelector('input[name="animals"]').value

        const monStart=document.querySelector('input[name="mon-start"]').value
        const monEnd=document.querySelector('input[name="mon-end"]').value
        const tueStart=document.querySelector('input[name="tue-start"]').value
        const tueEnd=document.querySelector('input[name="tue-end"]').value
        const wedStart=document.querySelector('input[name="wed-start"]').value
        const wedEnd=document.querySelector('input[name="wed-end"]').value
        const thuStart=document.querySelector('input[name="thu-start"]').value
        const thuEnd=document.querySelector('input[name="thu-end"]').value
        const friStart=document.querySelector('input[name="fri-start"]').value
        const friEnd=document.querySelector('input[name="fri-start"]').value
        const satStart=document.querySelector('input[name="sat-start"]').value
        const satEnd=document.querySelector('input[name="sat-start"]').value
        const sunStart=document.querySelector('input[name="sun-start"]').value
        const sunEnd=document.querySelector('input[name="sun-start"]').value
      
        const openHours={
            'mon':hourHelper(monStart,monEnd),
            'tud':hourHelper(tueStart,tueEnd),
            'wed':hourHelper(wedStart,wedEnd),
            'thu':hourHelper(thuStart,thuEnd),
            'fri':hourHelper(friStart,friEnd),
            'sat':hourHelper(satStart,satEnd),
            'sun':hourHelper(sunStart,sunEnd),
        }
        const website=document.querySelector('#website').value
        const mrt=document.querySelector('#mrt').value
        const phone=document.querySelector('#phone').value
        const longitude=document.querySelector('#longitude').value
        const latitude=document.querySelector('#latitude').value
        const data={
            'city_id':cityId,'name':name,'latitude':latitude,'longitude':longitude,
            'single_selling':singleSelling,'dessert_selling':dessertSelling,'meal_selling':mealSelling,
            'limited_time':limitedTime,'socket':socket,'standing_tables':standingTables,'music':music,
            'outdoor_seating':outdoorSeating,'cash_only':cashOnly,'animals':animals,'open_hours':openHours,
            'phone':phone,'website':website,'mrt':mrt,'address':address
        }
        const response=await fetch('api/shop/insert',{
            method: "POST",
            body: JSON.stringify(data),
            headers: new Headers({
              "Content-Type": "application/json",
            })
          })
        const result=await response.json();
        if(result.ok){
            msgPage.classList.remove('hidden')
            modifiedMsg.innerHTML="新增成功，準備跳轉到店家頁面!"
            setTimeout(()=>{
              msgPage.classList.add('hidden')
            },2000)
            location.replace(`/shop/${result.cafe_id}`)

        }else if(result.message ==="店家已經重複請再次確認"){
            
            msgPage.classList.remove('hidden')
            modifiedMsg.innerHTML="店家已經重複請再次確認"
            setTimeout(()=>{
              msgPage.classList.add('hidden')
            },2000)
        }else{
            msgPage.classList.remove('hidden')
            modifiedMsg.innerHTML="伺服器異常，請重新再提交一次"
            setTimeout(()=>{
              msgPage.classList.add('hidden')
            },2000)
        }
        
    






    }else{
        location.replace('/')
    }
    
})


function hourHelper(start,end){
    let result='';
    if (start&&end){
        result=`${start}-${end}`
    }else if(start==="未營業"){
        result='未營業';
    }
       
    return result
}

const allDayoff=document.querySelectorAll('input[type="checkbox"]')
for (let dayoff of allDayoff){
    dayoff.addEventListener('change',(e)=>{
        const target=e.target;
        const timeTwopart=target.parentElement.parentElement.querySelectorAll('input[type="time"]')
        
        if(target.checked){
            for (let time of timeTwopart){
                time.disabled=true;
                time.value='';
                time.classList.add('disabled')
            }
           
        }else{
            for (let time of timeTwopart){
            time.disabled=false;
            time.value='';
            time.classList.remove('disabled')
            }
        }
     
        

        
    })
}
