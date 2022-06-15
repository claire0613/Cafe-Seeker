const shopName=document.querySelector('.shop-name')
const priceRating=document.querySelector('.price-rating')
const wifiRating=document.querySelector('.wifi-rating')
const wifiCheck=document.querySelector('input[name="ignore-wifi"]')
const vacaRating=document.querySelector('.vaca-rating')
const quietRating=document.querySelector('.quiet-rating')
const comfortRating=document.querySelector('.comfort-rating')
const drinksRating=document.querySelector('.drinks-rating')
const foodRating=document.querySelector('.food-rating')
const viewRating=document.querySelector('.view-rating')
const toiletsRating=document.querySelector('.toilets-rating')
const speedCheck=document.querySelector('#ignore-speed')
import  {getValueColor} from './datahelper.js'

priceRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="price-rating"]:checked').value
    const score=document.querySelector('.score-price')
    if(value !==''){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }
   
    const labels=document.querySelectorAll('label[tag="price-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})
wifiRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="wifi-rating"]:checked').value
    const score=document.querySelector('.score-wifi')
    if (value !==''){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }
    const labels=document.querySelectorAll('label[tag="wifi-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})
wifiCheck.addEventListener('click',(e)=>{
    const check=document.querySelector('input[name="ignore-wifi"]');
    const inputs=document.querySelectorAll('input[name="wifi-rating"]');
    const labels=document.querySelectorAll('label[tag="wifi-rating"]');
    const score=document.querySelector('.score-wifi');
    score.innerText='';
    inputs[0].checked=true;
    for (let i=1;i<inputs.length;i++){
        
        if (check.checked){
            inputs[i].disabled=true;
            
        }else{
            inputs[i].disabled=false;
        }
    }
    for (let label of labels){
        label.classList.remove('checked');
        if (check.checked){
            label.classList.add('disabled');
        }else{
            label.classList.remove('disabled');
        }
    }
})


vacaRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="vaca-rating"]:checked').value
    const score=document.querySelector('.score-vaca')
    if(value !==''){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }
  
    const labels=document.querySelectorAll('label[tag="vaca-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})
quietRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="quiet-rating"]:checked').value
    const score=document.querySelector('.score-quiet')
    if(value !==''){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }
    const labels=document.querySelectorAll('label[tag="quiet-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})

comfortRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="comfort-rating"]:checked').value
    const score=document.querySelector('.score-comfort')
    if(value !==0){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }
    const labels=document.querySelectorAll('label[tag="comfort-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})
drinksRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="drinks-rating"]:checked').value
    const score=document.querySelector('.score-drinks')
    if(value !==0){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }
    const labels=document.querySelectorAll('label[tag="drinks-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})
foodRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="food-rating"]:checked').value
    const score=document.querySelector('.score-food')
    if(value !==''){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }
    const labels=document.querySelectorAll('label[tag="food-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})
viewRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="view-rating"]:checked').value
    const score=document.querySelector('.score-view')
    if(value !==''){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }
    const labels=document.querySelectorAll('label[tag="view-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})
toiletsRating.addEventListener('click',(e)=>{
    const value=document.querySelector('input[name="toilets-rating"]:checked').value
    const score=document.querySelector('.score-toilets')
    if(value !==''){
        score.innerText=`${value} 分`
        score.style.color=getValueColor(value)
    }

    const labels=document.querySelectorAll('label[tag="toilets-rating"]')
    for (let label of labels){
        label.classList.remove('checked')
    }
    for (let i=0;i<value;i++){
        labels[4-i].classList.add('checked')
    
    }
   
})

speedCheck.addEventListener('click',(e)=>{
    const check=document.querySelector('#ignore-speed')
    const input=document.querySelector('input[name="speed-rating"]')
    input.value='';
    if (check.checked){
            input.disabled=true;
            input.classList.add('disabled')
    }else{
            input.disabled=false;
            input.classList.remove('disabled')
    }
  

})
const cafe_id=document.URL.split('/').at(-1)

async function ratingInit(){
    const response=await fetch(userApi);
    const result=await response.json();
    if (result.data){
        const shopApi=`/api/shop/${cafe_id}`
        const shopres=await fetch(shopApi,{method:'GET'});
        const shopResult=await shopres.json();
        if(shopResult.data){
            let link=document.createElement('a')
            link.href=`/shop/${cafe_id}`
            link.innerText=shopResult.data.name
            shopName.append("您正在對",link,"評分")
        //    shopName.innerText=`您正在對" ${shopResult.data.name} 評分"`;
        }
    }else{
        location.replace('/login');
    }
}
ratingInit();
const scoreForm=document.querySelector('#score-form')
scoreForm.addEventListener('submit',insertScore)

const ratingApi=`/api/rating/${cafe_id}`;


async function insertScore(e){
    e.preventDefault();
    const response=await fetch(userApi,{method:'GET'});
    const result= await response.json();
    if (result.data){
        console.log(result.data)
        let price=checkInt(this.querySelector('input[name="price-rating"]:checked').value)
        let wifi=checkInt(this.querySelector('input[name="wifi-rating"]:checked').value)
        let vacancy=checkInt(this.querySelector('input[name="vaca-rating"]:checked').value)
        let quiet=checkInt(this.querySelector('input[name="quiet-rating"]:checked').value)
        let comfort=checkInt(this.querySelector('input[name="comfort-rating"]:checked').value)
        let drinks=checkInt(this.querySelector('input[name="drinks-rating"]:checked').value)
        let food=checkInt(this.querySelector('input[name="food-rating"]:checked').value)
        let view=checkInt(this.querySelector('input[name="view-rating"]:checked').value)
        let toilets=checkInt(this.querySelector('input[name="toilets-rating"]:checked').value)
        let speed=checkInt(this.querySelector('input[name="speed-rating"]').value)

        let data={
            price:price,wifi:wifi,vacancy:vacancy,quiet:quiet,comfort:comfort,drinks:drinks,
            food:food,view:view,toilets:toilets,speed:speed
        }
        
        const ratingfetch=await fetch(ratingApi,{
            method: 'POST',
            body: JSON.stringify(data),
            headers: new Headers({
                'Content-Type': 'application/json'
            })
        });
        const ratingResult=await ratingfetch.json();
        if(ratingResult.data){
            
            let orderId=ratingResult.number;
            location.replace(`/success/${orderId}`);
        }else{
            location.replace(`/fail/${cafe_id}`);
        }
    }else{
        console.log('fail')
        location.replace('/login');
       
    }
    

     
}

function checkInt(value){
    if (value===''){
        return null
    }else{
        return parseInt(value)
    }
}