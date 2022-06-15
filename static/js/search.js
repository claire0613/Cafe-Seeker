let search_page = document.URL.split("&")[0].split("=").at(-1);
const keyword = document.URL.split("=").at(-1);
const keySearchContent = document.querySelector("content");
const keySearchApi = `api/search?keyword=${keyword}&page=${search_page}`;
const searchWord = document.querySelector("#search-word");
const searchTotal = document.querySelector("#search-total");
const ITEM_PER_PAGE = 8;
import {
  star
} from "./datahelper.js";
let pagination = document.querySelector("#pagination");
// let pageNavigation=document.querySelector('.page-navigation');

function check_point(point) {
  if (point - 5 == 0) {}
}

async function keySearch() {
  searchWord.innerText = `搜尋關鍵字 : ${decodeURI(keyword)}`;

  if (search_page == null) {
    return;
  }

  const response = await fetch(keySearchApi, {
    method: "GET"
  });
  const result = await response.json();
  const data = result.data;


  searchTotal.innerText = `共找到 ${result.totalCount} 間咖啡廳`;
  for (let cafe of data) {
    let box = document.createElement("div");
    box.classList.add("cafe-box");
    let link = document.createElement("a");
    link.href = `/shop/${cafe.id}`;

    let img = document.createElement("img");
    if (cafe.photo_url) {
      let url = encodeURI(cafe.photo_url);
      img.src = url;
      img.alt = "no pic";
      box.append(img);
    }

    let name = document.createElement("div");
    name.classList.add("cafe-name");
    name.innerText = cafe.name;
    let card1 = document.createElement("div");
    card1.classList.add("card-one");
    card1.innerText = cafe.area;
    let card2 = document.createElement("div");
    card2.classList.add("card-two");
    if (cafe.drinks !== 0) {
      star("咖啡", cafe.drinks, card2);
    } else {
      star("咖啡", 0, card2);
    }
    let card3 = document.createElement("div");
    card3.classList.add("card-three");
    let wifiImg = document.createElement("img");
    wifiImg.src = "../static/icons/wifi_20_w 1.png";
    if (cafe.wifi !== 0) {
      star(wifiImg, cafe.wifi, card3);
    } else {
      star(wifiImg, 0, card3);
    }

    box.append(name, card1, card2, card3);
    link.append(box);
    keySearchContent.append(link);
  }

  if (result.nextPage !== null) {
    getTotalPages(result.totalPage, search_page);
  }else{
    getTotalPages(result.totalPage, result.totalPage);
  }
}

// //pagination 監聽器
// pagination.addEventListener('click', event => {
//     keySearch()
//   })

//計算總共頁數
async function getTotalPages(totalPage, search_page) {
  let totalPages = totalPage % ITEM_PER_PAGE;
  let nowpage = parseInt(search_page);
  let pageItemContent = "";
  let prePage = nowpage - 1;

  let nextpage = nowpage + 3;

  //pre-log
  if (nowpage == 0) {
    pageItemContent += `
        <li class="disabled">
            <span>«</span>
        </li>`;
  } else {
    pageItemContent += `
        <li class="page-item">
            <a class="page-link" href="/search?page=${prePage}&keyword=${keyword}" id="previous">
            «
            </a>
        </li>`;
  }
  //prepage
  if (nowpage - 3 > 3) {
    for (let i = 0; i < 2; i++) {
      pageItemContent += `
              <li class="page-item">
                <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${
        i + 1
      }</a>
              </li>
            `;
    }
    pageItemContent += `
                    <li class="disabled">
                        <span>...</span>
                    </li>`;
    for (let i = nowpage - 3; i < nowpage; i++) {
      pageItemContent += `
                <li class="page-item">
                <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${
        i + 1
      }</a>
                </li>
            `;
    }
  } else {
    for (let i = 0; i < nowpage; i++) {
      pageItemContent += `
                <li class="page-item">
                <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${
        i + 1
      }</a>
                </li>
            `;
    }
  }
  //now

  pageItemContent += `
                    <li class="active">
                        <span>${nowpage + 1}</span>
                    </li>`;

  if (nowpage + 3 < totalPage) {
    for (let i = nowpage + 1; i < nowpage + 4; i++) {
      pageItemContent += `
                <li class="page-item">
                  <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${
        i + 1
      }</a>
                </li>
              `;
    }
    pageItemContent += `
          <li class="disabled">
              <span>...</span>
          </li>`;
  } else {
    for (let i = nowpage + 1; i < totalPage+1; i++) {
      pageItemContent += `
                <li class="page-item">
                  <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${
        i + 1
      }</a>
                </li>
      
              `;
    }
  }


  if(nowpage===totalPage){
    pageItemContent += `
        <li class="disabled">
            <span>»</span>
        </li>`;
  }else{
    pageItemContent += ` 
    <li class="page-item">
    <a class="page-link" href="/search?page=${
      nowpage + 1
    }&keyword=${keyword}" id="previous">
    »
    </a>
    </li>`;

  }

  pagination.innerHTML = pageItemContent;
}

keySearch();