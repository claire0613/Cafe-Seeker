const loadmore = document.querySelector(".load-more");
const content = document.querySelector("content");
const keywordform = document.querySelector("#keywordform");
let page = 0;


async function cityLoad() {
  
  let cityBlockApi = `api/city?page=${page}`;
  if (page == null) {
    return;
  }
  const response = await fetch(cityBlockApi, {
    method: "GET"
  });
  const result = await response.json();
  const data = result.data;
  for (let city of data) {
    let box = document.createElement("div");
    box.classList.add("city-box");
    let name = document.createElement("div");
    name.classList.add("cityname");
    name.innerText = city.city_tw;
    let nav = document.createElement("div");
    nav.classList.add("navigation");

    let cityLink = document.createElement("a");
    cityLink.href = `/rank/${city.city}`;

    let cityLinkImg = document.createElement("img");
    cityLinkImg.src = "../static/icons/ranking.png";

    let cityList = document.createElement("a");
    cityList.href = `/${city.city}/list`;

    let cityListImg = document.createElement("img");
    cityListImg.src = "../static/icons/list.svg";

    cityLink.append(cityLinkImg, (cityLinkImg.innerText = "排名"));
    cityList.append(cityListImg, (cityListImg.innerText = "清單"));

    nav.append(cityLink, cityList);
    box.append(name, nav);
    content.append(box);
  }
  page = result.nextPage;

}

loadmore.addEventListener("click", () => {
  loadmore.classList.add("hide");
  cityLoad();
});

cityLoad();

function keyFormSubmit(e) {
  e.preventDefault();
  let inputKeyword = document.querySelector('input[name="keyword"]').value;

  location.replace(`/search?page=0&keyword=${inputKeyword}`);
}

keywordform.addEventListener("submit", keyFormSubmit);


///

let keypage = 0;
let keyword = '';
let search_times = 0;
let public_name_scroll = true;
let public_keyword_page = 0;
const keySearchApi = `api/search?keyword=${keyword}&page=${keypage}`;
// keywordform.addEventListener("input", function(){
//     let value = this.value;

// });
async function get_keyword(keyword, keypage) {
  try {
    let response = await fetch(`/api/search?keyword=${keyword}&page=${keypage}`);
    let data = await response.json();
    return data
  } catch (message) {
    console.log(`${message}`);
    throw Error('Fetching was not ok!!.');
  }
};

let key_input = document.querySelector('input[name="keyword"]')

key_input.addEventListener("input", function () {
  //註冊搜尋keywordinput
  let value = this.value;
  if (value.length === 0) {
    let input_area = document.querySelector("#keywordform");

    if (document.querySelector(".search-result")) {
      input_area.removeChild(document.querySelector(".search-result"))
    };
    public_name_scroll = true;
    public_keyword_page = 0;
  } else {

    public_name_scroll = true;
    public_keyword_page = 0;
    let search_promise = get_keyword(value, public_keyword_page);
    search_promise.then((result) => {
      if (document.getElementById("result_name").value.length !== 0) {
        let next_page = result["nextPage"];
        public_keyword_page = next_page;
        renderSearch(result.data);
      }

    });
  }
})







function renderSearch(data) {
  let input_area = document.querySelector("#keywordform");
  if (document.querySelector(".search-result")) {
    input_area.removeChild(document.querySelector(".search-result"))
  };
  let div = document.createElement('div');
  div.classList.add('search-result')
  let ul = document.createElement("ul");
  ul.classList.add("ul");
  for (let i = 0; i < data.length; i++) {
    let li = create_search_li(data[i]);
    ul.appendChild(li);
  };
  ul.addEventListener("scroll", function () { //註冊滑動載入事件
    if (this.scrollHeight - this.scrollTop <= this.clientHeight) {
      if (public_name_scroll && public_keyword_page) {
        public_name_scroll = false;
        let keyword = document.querySelector('input[name="keyword"]').value;
        let promise = get_keyword(keyword, public_keyword_page);
        promise.then((result) => {
          public_name_scroll = true;
          let next_page = result["nextPage"];
          public_keyword_page = next_page;
          let ul = document.querySelector(".ul");
          for (let i = 0; i < result.data.length; i++) {
            let li = create_search_li(result.data[i]);
            ul.appendChild(li);
          };
        });
      }
    };
  });
  div.appendChild(ul);
  input_area.appendChild(div)
}

function create_search_li(result) {
  let li = document.createElement("li");
  li.appendChild(document.createTextNode(result["name"]));
  li.setAttribute("result_name", result["name"])
  li.classList.add("name-item-li");
  //按下去的時候鎖定名字,存在全域變數,
  li.addEventListener("click", function () {
    click_name(this);
    


  })
  return li
}


//按下去選的name
function click_name(result) {
  let input_area = document.querySelector("#keywordform");
  let clikc_name = document.querySelector("#result_name");
  let input_result = document.querySelector('input[name="keyword"]');
  input_result.value = result.textContent;
  console.log(result.textContent)
  if (document.querySelector(".search-result")) {
    input_area.removeChild(document.querySelector(".search-result"))
  };



}