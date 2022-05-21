const loadmore=document.querySelector('.load-more');
const content=document.querySelector('content');
const keywordform=document.querySelector('#keywordform');

let page=0;

async function cityLoad(){
    console.log(page)
    let cityBlockApi=`api/city?page=${page}`;
    if (page==null){return}
    const response=await fetch(cityBlockApi,{method:"GET"});
    const result=await response.json();
    const data=result.data;
    for(let city of data){
        let box = document.createElement('div');
        box.classList.add('city-box')
        let name = document.createElement('div');
        name.classList.add('cityname')
        name.innerText=city.city_tw
        let nav = document.createElement('div');
        nav.classList.add('navigation')
        


        let cityLink= document.createElement('a')
        cityLink.href = `/${city.city}`
        
        let cityLinkImg = document.createElement('img');
        cityLinkImg.src = '../static/icons/home.svg'

        let cityList= document.createElement('a')
        cityList.href = `/${city.city}/list`
        
        let cityListImg = document.createElement('img');
        cityListImg.src = '../static/icons/list.svg'

        cityLink.append(cityLinkImg,cityLinkImg.innerText='首頁')
        cityList.append(cityListImg,cityListImg.innerText='清單')

        nav.append(cityLink,cityList)
        box.append(name,nav)
        content.append(box)
    }
    page=result.nextPage;
    console.log(page)

}

loadmore.addEventListener('click',()=>{
    loadmore.classList.add('hide')
    cityLoad()

})

cityLoad()



function keyFormSubmit(e){
    e.preventDefault();
    let keyword=document.querySelector('input[name="keyword"]').value;
 
    location.replace(`/search?keyword=${keyword}`)
 


}
console.log(keywordform)
keywordform.addEventListener('submit',keyFormSubmit)