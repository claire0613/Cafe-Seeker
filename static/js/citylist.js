const listDescription=document.querySelector('.description')
const cityListTbody=document.querySelector('tbody')
const queryListCity=document.URL.split('/').at(3)
let cityListPage=0;
let isfetching=false;

async function cityListSearch(){
    isfetching=true;
    let cityListApi=`/api/city/list?city=${queryListCity}&page=${cityListPage}`
    if (cityListPage== null){
        return 
    }
    const response=await fetch(cityListApi,{method:'GET'});
    const result=await response.json();
    const data=result.data;

    console.log(result)
    if (result.city_tw){
        listDescription.innerText=`${result.city_tw} 網友們推薦的咖啡廳清單 : 共收錄 ${result.totalCount} 間店`;
        let today=0;
        switch (new Date().getDay()) {
            case 1: 
                today='mon';
                break
            case 2: 
                today='tue';
                break
            case 3: 
                today='wed';
                break
            case 4: 
                today='thu';
                break
            case 5: 
                today='fri';
                break
            case 6: 
                today='sat';
                break

            case 0: 
                today='sun';
                break
        }
        console.log(today)
        
        for (let cafe of data){
            let score = avg([cafe.price,cafe.wifi, cafe.vacancy, cafe.food, cafe.quiet,cafe.comfort, cafe.toilets])
            ratingScroe=(Math.max(0, Math.min(score, 5))).toFixed(1)
            const tr=document.createElement('tr')
            tr.classList.add('tr-box') 
           

            const rating_td=document.createElement('td')
            rating_td.classList.add('tb-rating')
            const rating=document.createElement('span')
            rating.innerText=ratingScroe
            rating_td.append(rating)

            const name_td=document.createElement('td')
            name_td.classList.add('tb-name')
            const cafe_link=document.createElement('a')
            cafe_link.innerText=cafe.name
            cafe_link.href=`/shop/${cafe.id}`
            name_td.append(cafe_link)

            const price_td=document.createElement('td')
            price_td.classList.add('tb-price')
            const price=document.createElement('span')
            price.innerText=cafe.price
            price_td.append(price)
            

            const wifi_td=document.createElement('td')
            wifi_td.classList.add('tb-wifi')
            const wifi=document.createElement('span')
            wifi.innerText=cafe.wifi
            wifi_td.append(wifi)

            const vaca_td=document.createElement('td')
            vaca_td.classList.add('tb-vaca')
            const vaca=document.createElement('span')
            vaca.innerText=cafe.vacancy
            vaca_td.append(vaca)
            
            const food_td=document.createElement('td')
            food_td.classList.add('tb-food')
            const food=document.createElement('span')
            food.innerText=cafe.food
            food_td.append(food)

            const quiet_td=document.createElement('td')
            quiet_td.classList.add('tb-quiet')
            const quiet=document.createElement('span')
            quiet.innerText=cafe.quiet
            quiet_td.append(quiet)

            const comfort_td=document.createElement('td')
            comfort_td.classList.add('tb-comfort')
            const comfort=document.createElement('span')
            comfort.innerText=cafe.comfort
            comfort_td.append(comfort)

            const toilets_td=document.createElement('td')
            toilets_td.classList.add('tb-toilets')
            const toilets=document.createElement('span')
            toilets.innerText=cafe.toilets
            toilets_td.append(toilets)

            const mrt_td=document.createElement('td')
            mrt_td.classList.add('tb-mrt')
            const mrt=document.createElement('span')
            mrt.innerText=cafe.transport
            mrt_td.append(mrt)

            const open_td=document.createElement('td')
            open_td.classList.add('tb-open')
            const open=document.createElement('span')
            let day=JSON.parse(cafe.open_hours)
            if(day!==null){
                open.innerText=day[today]
            }else{
                open.innerText=null
            }
           
            open_td.append(open)

            const limited_time_td=document.createElement('td')
            limited_time_td.classList.add('tb-limited_time')
            const limited_time=document.createElement('span')
            limited_time.innerText=cafe.limited_time
            limited_time_td.append(limited_time)
            
            const meal_selling_td=document.createElement('td')
            meal_selling_td.classList.add('tb-open')
            const meal_selling=document.createElement('span')
            meal_selling.innerText=cafe.meal_selling
            meal_selling_td.append(meal_selling)
            
            tr.append(rating_td,name_td,price_td,wifi_td,vaca_td,food_td,quiet_td,comfort_td,toilets_td,mrt_td,open_td,limited_time_td,meal_selling_td)
            cityListTbody.append(tr)
            

        }
        
    }
    console.log(result["nextPage"])
    cityListPage=result["nextPage"]
    isnextpage=false;
    if(cityListTbody.innerHTML === ''){
        const nodata = document.createElement('h3')   
        nodata.innerText = `沒有此城市的咖啡店`
        nodata.style.color = '#666666'
        cityListPage.append(nodata)
        
    }
    isfetching=false;
}


function avg(arr) {
    let n = 0;
    let t = 0;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] != null) {
        n++;
        t += arr[i];
      }
    }
    return n == 0 ? 0 : t / n;
  }





const options = {
    rootMargin: "0px 0px 100px 0px",
    threshold: 0
  }
let callback = ([entry]) => {
        if (entry.isIntersecting) {
            if(!isfetching){
                cityListSearch();
            }
  
        }
    
  }


// 設定觀察對象：告訴 observer 要觀察哪個目標元素
const footer = document.querySelector('footer')
console.log(footer)
// 製作鈴鐺：建立一個 intersection observer，帶入相關設定資訊
let observer = new IntersectionObserver(callback, options)
// // 設定觀察// 觀察目標元素
observer.observe(footer)
