const listDescription = document.querySelector(".description");
const cityListTbody = document.querySelector("tbody");
const queryListCity = document.URL.split("/").at(3);
const resetBtn = document.querySelector(".reset");
import { getValueColor, scoreRender } from "./datahelper.js";
let cityListPage = 0;
let fKeyword = "";
let fRating = 0;
let fPrice = 0;
let fWifi = 0;
let fVaca = 0;
let fDrinks = 0;
let fQuiet = 0;
let fComfort = 0;
let fLimted_time = "";
let fMeal_selling = "";

let isfetching = false;

async function cityListSearch() {
  isfetching = true;
  let cityListApi = `/api/city/list/filter?city=${queryListCity}&page=${cityListPage}&keyword=${fKeyword}&rating=${fRating}&price=${fPrice}&wifi=${fWifi}&vacancy=${fVaca}&drinks=${fDrinks}&quiet=${fQuiet}&comfort=${fComfort}&limited_time=${fLimted_time}&meal_selling=${fMeal_selling}`;
  if (cityListPage == null) {
    return;
  }
  const response = await fetch(cityListApi, { method: "GET" });
  const result = await response.json();
  const data = result.data;
  if (result.city_tw) {
    listDescription.innerText ='';
    listDescription.innerText = `"${result.city_tw}" 網友們推薦的咖啡廳清單 :共收錄 ${result.totalCount} 間店`;
    let today = 0;
    switch (new Date().getDay()) {
      case 1:
        today = "mon";
        break;
      case 2:
        today = "tue";
        break;
      case 3:
        today = "wed";
        break;
      case 4:
        today = "thu";
        break;
      case 5:
        today = "fri";
        break;
      case 6:
        today = "sat";
        break;

      case 0:
        today = "sun";
        break;
    }
   

    for (let cafe of data) {
      const tr = document.createElement("tr");
      tr.classList.add("tr-box");
        
      const rating_td = document.createElement("td");
      rating_td.classList.add("tb-rating");
      let rating = document.createElement("span");
      rating.innerText = scoreRender(cafe.rating);
      if (cafe.rating === 0) {
        rating = document.createElement("img");
        rating.src = "../static/icons/help-circle_w_20.png";
      }

      rating.style.color = getValueColor(cafe.rating);
      rating_td.append(rating);

      const name_td = document.createElement("td");
      name_td.classList.add("tb-name");
      const cafe_link = document.createElement("a");
      cafe_link.innerText = cafe.name;
      cafe_link.href = `/shop/${cafe.id}`;
      name_td.append(cafe_link);

      const price_td = document.createElement("td");
      price_td.classList.add("tb-price");
      let price = document.createElement("span");
      price.innerText = scoreRender(cafe.price);
      if (cafe.price === 0) {
        price = document.createElement("img");
        price.src = "../static/icons/help-circle_w_20.png";
      }
      price.style.color = getValueColor(cafe.price);
      price_td.append(price);

      const wifi_td = document.createElement("td");
      wifi_td.classList.add("tb-wifi");
      let wifi = document.createElement("span");
      wifi.innerText = scoreRender(cafe.wifi);
      if (cafe.wifi === 0) {
        wifi = document.createElement("img");
        wifi.src = "../static/icons/help-circle_w_20.png";
      }
      wifi.style.color = getValueColor(cafe.wifi);
      wifi_td.append(wifi);

      const vaca_td = document.createElement("td");
      vaca_td.classList.add("tb-vaca");
      let vaca = document.createElement("span");
      vaca.innerText = scoreRender(cafe.vacancy);
      if (cafe.vacancy === 0) {
        vaca = document.createElement("img");
        vaca.src = "../static/icons/help-circle_w_20.png";
      }
      vaca.style.color = getValueColor(cafe.vacancy);
      vaca_td.append(vaca);

      const drinks_td = document.createElement("td");
      drinks_td.classList.add("tb-food");
      let drinks = document.createElement("span");
      drinks.innerText = scoreRender(cafe.drinks);
      if (cafe.drinks === 0) {
        drinks = document.createElement("img");
        drinks.src = "../static/icons/help-circle_w_20.png";
      }
      drinks.style.color = getValueColor(cafe.drinks);
      drinks_td.append(drinks);

      const quiet_td = document.createElement("td");
      quiet_td.classList.add("tb-quiet");
      let quiet = document.createElement("span");
      quiet.innerText = scoreRender(cafe.quiet);
      if (cafe.quiet === 0) {
        quiet = document.createElement("img");
        quiet.src = "../static/icons/help-circle_w_20.png";
      }
      quiet.style.color = getValueColor(cafe.quiet);
      quiet_td.append(quiet);

      const comfort_td = document.createElement("td");
      comfort_td.classList.add("tb-comfort");
      let comfort = document.createElement("span");
      comfort.innerText = scoreRender(cafe.comfort);
      if (cafe.comfort === 0) {
        comfort = document.createElement("img");
        comfort.src = "../static/icons/help-circle_w_20.png";
      }
      comfort.style.color = getValueColor(cafe.comfort);
      comfort_td.append(comfort);

      const mrt_td = document.createElement("td");
      mrt_td.classList.add("tb-mrt");
      let mrt = document.createElement("span");
      mrt.innerText = cafe.transport;

      if (cafe.transport === null) {
        mrt = document.createElement("img");
        mrt.src = "../static/icons/help-circle_w_20.png";
      }
      mrt_td.append(mrt);

      const open_td = document.createElement("td");
      open_td.classList.add("tb-open");
      let open = document.createElement("span");
      let day = JSON.parse(cafe.open_hours);
      day = JSON.parse(day);
      if (day !== null) {
        open.innerText = day[today];
      } else {
        open = document.createElement("img");
        open.src = "../static/icons/help-circle_w_20.png";
      }

      open_td.append(open);

      const limited_time_td = document.createElement("td");
      limited_time_td.classList.add("tb-limited_time");
      let limited_time = document.createElement("span");
      limited_time.innerText = scoreRender(cafe.limited_time);
      if (cafe.limited_time === null) {
        limited_time = document.createElement("img");
        limited_time.src = "../static/icons/help-circle_w_20.png";
      }
      limited_time.style.color = getValueColor(cafe.limited_time);

      limited_time_td.append(limited_time);

      const meal_selling_td = document.createElement("td");
      meal_selling_td.classList.add("tb-mealing");
      let meal_selling = document.createElement("span");
      meal_selling.innerText = scoreRender(Boolean(cafe.meal_selling));
      if (cafe.meal_selling === null) {
        meal_selling = document.createElement("img");
        meal_selling.src = "../static/icons/help-circle_w_20.png";
      }
      meal_selling.style.color = getValueColor(Boolean(cafe.meal_selling));
      meal_selling_td.append(meal_selling);

      tr.append(
        rating_td,
        name_td,
        price_td,
        wifi_td,
        vaca_td,
        drinks_td,
        quiet_td,
        comfort_td,
        limited_time_td,
        meal_selling_td,
        open_td,
        mrt_td
      );
      const link = document.createElement("a");
      link.href = `/shop/${cafe.id}`;
      link.append(tr);
      cityListTbody.append(link);
    }
  }


  if (result.nextPage !== null) {
    cityListPage = result["nextPage"];
  }

  if (cityListTbody.innerHTML === "") {
    const nodata = document.createElement("h3");
    nodata.innerText = `沒有此城市的咖啡店`;
    nodata.style.color = "#666666";
    cityListPage.append(nodata);
  }
  isfetching = false;
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

cityListSearch();


resetBtn.addEventListener('click',()=>{
    cityListPage = 0;
    fKeyword = "";
    fRating = 0;
    fPrice = 0;
    fWifi = 0;
    fVaca = 0;
    fDrinks = 0;
    fQuiet = 0;
    fComfort = 0;
    fLimted_time = "";
    fMeal_selling = "";
    cityListTbody.innerText = "";
    cityListSearch()
})
const options = {
  rootMargin: "0px 0px 200px 0px",
  threshold: 0.5,
};
let callback = ([entry]) => {
  if (entry.isIntersecting) {
    if (!isfetching) {
      cityListSearch();
    }
  }
};

// 設定觀察對象：告訴 observer 要觀察哪個目標元素
const footer = document.querySelector("#footer-p");
// 製作鈴鐺：建立一個 intersection observer，帶入相關設定資訊
let observer = new IntersectionObserver(callback, options);
// // 設定觀察// 觀察目標元素
observer.observe(footer);






const filterForm = document.querySelector("form");
filterForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  
  cityListPage = 0;
  cityListTbody.innerText = "";

  fKeyword = document.querySelector('input[name="keyword"]').value;
  fRating = document.querySelector('select[name="rating"]').value;
  fPrice = document.querySelector('select[name="price"]').value;
  fWifi = document.querySelector('select[name="wifi"]').value;
  fVaca = document.querySelector('select[name="vacancy"]').value;
  fDrinks = document.querySelector('select[name="drinks"]').value;
  fQuiet = document.querySelector('select[name="quiet"]').value;
  fComfort = document.querySelector('select[name="comfort"]').value;
  fLimted_time = document.querySelector('select[name="limted_time"]').value;
  fMeal_selling = document.querySelector('select[name="meal_selling"]').value;
  cityListSearch();
});

const filterKeyword = document.querySelector('input[name="keyword"]');
const filterRating = document.querySelector('select[name="rating"]');
const filterPrice = document.querySelector('select[name="price"]');
const filterWifi = document.querySelector('select[name="wifi"]');
const filterVaca = document.querySelector('select[name="vacancy"]');
const filterDrinks = document.querySelector('select[name="drinks"]');
const filterQuiet = document.querySelector('select[name="quiet"]');
const filterComfort = document.querySelector('select[name="comfort"]');
const filterlimted_time = document.querySelector('select[name="limted_time"]');
const filtermeal_selling = document.querySelector(
  'select[name="meal_selling"]'
);
filterRating.addEventListener("change", async (e) => {
  e.preventDefault();
  filter();
});
filterPrice.addEventListener("change", async (e) => {
  e.preventDefault();
  filter();
});

filterWifi.addEventListener("change", async (e) => {
  e.preventDefault();
  filter();
});
filterVaca.addEventListener("change", async (e) => {
  e.preventDefault();
  filter();
});
filterDrinks.addEventListener("change", async (e) => {
  e.preventDefault();
  filter();
});
filterQuiet.addEventListener("change", async (e) => {
  e.preventDefault();
  filter();
});

filterComfort.addEventListener("change", async (e) => {
  e.preventDefault();
  filter();
});
filterlimted_time.addEventListener("change", async (e) => {
  e.preventDefault();
  filter();
});
filtermeal_selling.addEventListener("change", async (e) => {
  e.preventDefault();

  filter();
});







function filter() {
  cityListPage = 0;
  cityListTbody.innerText = "";
  fKeyword = document.querySelector('input[name="keyword"]').value;
  fRating = document.querySelector('select[name="rating"]').value;
  fPrice = document.querySelector('select[name="price"]').value;
  fWifi = document.querySelector('select[name="wifi"]').value;
  fVaca = document.querySelector('select[name="vacancy"]').value;
  fDrinks = document.querySelector('select[name="drinks"]').value;
  fQuiet = document.querySelector('select[name="quiet"]').value;
  fComfort = document.querySelector('select[name="comfort"]').value;
  fLimted_time = document.querySelector('select[name="limted_time"]').value;
  fMeal_selling = document.querySelector('select[name="meal_selling"]').value;
  cityListSearch();
}
