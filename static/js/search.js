
let search_page=0;
const keyword = document.URL.split('=').slice(-1); 
const keySearchContent=document.querySelector('content')
const keySearchApi=`api/search?keyword=${keyword}&page=${search_page}`;
const searchWord=document.querySelector('#search-word')

function check_point(point){
    if (point-5 ==0){}
}

async function keySearch(){
    searchWord.innerText=decodeURI(keyword);
    if (search_page==null){return}
    
    const response=await fetch(keySearchApi,{method:"GET"});
    const result=await response.json();
    const data=result.data;
    for(let cafe of data){
        let box = document.createElement('div');
        box.classList.add('cafe-box')
        let img=document.createElement('img')
        if (cafe.images){
            let url=JSON.parse(cafe.images)[0]
            url=encodeURI(url)
            img.src=url;
            
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
        
        box.append(img,name,card1,card2,card3)
        keySearchContent.append(box)
    }
 


 }
keySearch()
function star(text,value,card){
        let fill=parseInt(value);
        let empty=parseInt(5-value);
        let half=value%1;
        card.append(text)

        for (let i=0;i < fill;i++){
            let i=document.createElement('img')
            i.src='../static/icons/filled-star_w_20.png'
            card.append(i)
        }
        if (half!==0){
            let i=document.createElement('img')
            i.src='../static/icons/star-half_w_20.png'
            card.append(i)
        }
        for (let i=0;i < empty;i++){
            let i=document.createElement('img')
            i.src='../static/icons/bx-star_w_20.png'
            card.append(i)
    }
    
}