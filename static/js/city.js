const searchDiv=document.querySelector('.search-div');
const favorDiv=document.querySelector('.favor-div');
const ratingDiv=document.querySelector('.rating-div');
const msgDiv=document.querySelector('.msg-div');
import  {star} from './datahelper.js'



async function renderInit(){
    const response=await fetch('/api/city/view');
    const result=await response.json();
    const search_list=result.search_count;
    //熱門搜尋店家
        for(let cafe of search_list){
            let box = document.createElement('div');
            box.classList.add('cafe-box')
            let link=document.createElement('a');
            link.href=`/shop/${cafe.id}`
            let img=document.createElement('img')
            if (cafe.photo_url){
                let url=encodeURI(cafe.photo_url)
                img.src=url;
                img.alt='no pic';
                box.append(img)
            }

            let name = document.createElement('div');
            name.classList.add('cafe-name')
            name.innerText=cafe.name
            let card1 = document.createElement('div');
            card1.classList.add('card-one')
            card1.innerText=cafe.area
            let card2 = document.createElement('div');
            card2.classList.add('card-two')
            if (cafe.food!==0){
                star("咖啡",cafe.food,card2)
            }else{
                star("咖啡",0,card2)
            }
            let card3 = document.createElement('div');
            card3.classList.add('card-three')
            let wifiImg = document.createElement('img');
            wifiImg.src = '../static/icons/wifi_20_w 1.png';
            if (cafe.wifi!==0){
                star(wifiImg,cafe.wifi,card3)
            }else{
                star(wifiImg,0,card3)
            }
            
            box.append(name,card1,card2,card3)
            link.append(box)
            searchDiv.append(link)
        }
    const favor_list=result.cafe_favor;  
     //熱門收藏店家
     for(let cafe of favor_list){
        let box = document.createElement('div');
        box.classList.add('cafe-box')
        let link=document.createElement('a');
        link.href=`/shop/${cafe.id}`
        let img=document.createElement('img')
        if (cafe.photo_url){
            let url=encodeURI(cafe.photo_url)
            img.src=url;
            img.alt='no pic';
            box.append(img)
        }

        let name = document.createElement('div');
        name.classList.add('cafe-name')
        name.innerText=cafe.name
        let card1 = document.createElement('div');
        card1.classList.add('card-one')
        card1.innerText=cafe.area
        let card2 = document.createElement('div');
        card2.classList.add('card-two')
        if (cafe.food!==0){
            star("咖啡",cafe.food,card2)
        }else{
            star("咖啡",0,card2)
        }
        let card3 = document.createElement('div');
        card3.classList.add('card-three')
        let wifiImg = document.createElement('img');
        wifiImg.src = '../static/icons/wifi_20_w 1.png';
        if (cafe.wifi!==0){
            star(wifiImg,cafe.wifi,card3)
        }else{
            star(wifiImg,0,card3)
        }
        
        box.append(name,card1,card2,card3)
        link.append(box)
        favorDiv.append(link)
        }
    const rating_list=result.cafe_rating;
    //最多人評分收藏店家
     for(let cafe of rating_list){
        let box = document.createElement('div');
        box.classList.add('cafe-box')
        let link=document.createElement('a');
        link.href=`/shop/${cafe.id}`
        let img=document.createElement('img')
        if (cafe.photo_url){
            let url=encodeURI(cafe.photo_url)
            img.src=url;
            img.alt='no pic';
            box.append(img)
        }

        let name = document.createElement('div');
        name.classList.add('cafe-name')
        name.innerText=cafe.name
        let card1 = document.createElement('div');
        card1.classList.add('card-one')
        card1.innerText=cafe.area
        let card2 = document.createElement('div');
        card2.classList.add('card-two')
        if (cafe.food!==0){
            star("咖啡",cafe.food,card2)
        }else{
            star("咖啡",0,card2)
        }
        let card3 = document.createElement('div');
        card3.classList.add('card-three')
        let wifiImg = document.createElement('img');
        wifiImg.src = '../static/icons/wifi_20_w 1.png';
        if (cafe.wifi!==0){
            star(wifiImg,cafe.wifi,card3)
        }else{
            star(wifiImg,0,card3)
        }
        
        box.append(name,card1,card2,card3)
        link.append(box)
        ratingDiv.append(link)
        }
    const msg_list=result.cafe_msg;
    //最多討論收藏店家
     for(let cafe of msg_list){
        let box = document.createElement('div');
        box.classList.add('cafe-box')
        let link=document.createElement('a');
        link.href=`/shop/${cafe.id}`
        let img=document.createElement('img')
        if (cafe.photo_url){
            let url=encodeURI(cafe.photo_url)
            img.src=url;
            img.alt='no pic';
            box.append(img)
        }

        let name = document.createElement('div');
        name.classList.add('cafe-name')
        name.innerText=cafe.name
        let card1 = document.createElement('div');
        card1.classList.add('card-one')
        card1.innerText=cafe.area
        let card2 = document.createElement('div');
        card2.classList.add('card-two')
        if (cafe.food!==0){
            star("咖啡",cafe.food,card2)
        }else{
            star("咖啡",0,card2)
        }
        let card3 = document.createElement('div');
        card3.classList.add('card-three')
        let wifiImg = document.createElement('img');
        wifiImg.src = '../static/icons/wifi_20_w 1.png';
        if (cafe.wifi!==0){
            star(wifiImg,cafe.wifi,card3)
        }else{
            star(wifiImg,0,card3)
        }
        
        box.append(name,card1,card2,card3)
        link.append(box)
        msgDiv.append(link)
        }      






    }


    renderInit()