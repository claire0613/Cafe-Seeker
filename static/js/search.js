
let search_page=0;
const keyword = document.URL.split('=').slice(-1); 
const keySearchContent=document.querySelector('content')
const keySearchApi=`api/search?keyword=${keyword}&page=${search_page}`

function check_point(point){
    if (point-5 ==0){}
}

async function keySearch(){
    if (search_page==null){return}
    
    const response=await fetch(keySearchApi,{method:"GET"});
    const result=await response.json();
    const data=result.data;
    for(let cafe of data){
        let box = document.createElement('div');
        box.classList.add('cafe-box')
        if (cafe.images){
            let url=JSON.parse(cafe.images)[0]
            console.log(JSON.parse(cafe.images))
            box.style.backgroundImage="url('https://d2ltlh9sj9r3jz.cloudfront.net/cafe-seeker/taipei/巢-nido/seating1.jpg')"
            console.log(JSON.parse(cafe.images)[0])
        }

        let name = document.createElement('div');
        name.classList.add('cafe-name')
        name.innerText=cafe.name
        let card1 = document.createElement('div');
        card1.classList.add('card-one')
        card1.innerText=cafe.area
        let card2 = document.createElement('div');
        card2.classList.add('card-two')
        card2.innerText="咖啡"+cafe.food.toString()
        let card3 = document.createElement('div');
        card3.classList.add('card-three')
        
        let wifiImg = document.createElement('img');
        wifiImg.src = '../static/icons/wifi_20_w 1.png';
        card3.append(wifiImg,card3.innerText=cafe.wifi.toString())
        box.append(name,card1,card2,card3)
        keySearchContent.append(box)
    }
 


 }
keySearch()
