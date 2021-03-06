const cafe_id = document.URL.split("/").at(-1);
const shopName = document.querySelector(".shop-name");

const wifiSpan = document.querySelector("#wifi-span");
const vacaSpan = document.querySelector("#vaca-span");
const priceSpan = document.querySelector("#price-span");
const quietSpan = document.querySelector("#quiet-span");
const comfortSpan = document.querySelector("#comfort-span");
const foodSpan = document.querySelector("#food-span");
const drinksSpan = document.querySelector("#drinks-span");
const viewSpan = document.querySelector("#view-span");
const toiletsSpan = document.querySelector("#toilets-span");
const speedSpan = document.querySelector("#speed-span");
const scoreCount = document.querySelector("#score-count");
const singleSelling = document.querySelector("#single-span");
const limitedTime = document.querySelector("#limited-span");
const dessertSpan = document.querySelector("#dessert-span");
const sockettSpan = document.querySelector("#socket-span");
const mealSpan = document.querySelector("#meal-span");
const standingSpan = document.querySelector("#standing-span");
const musicSpan = document.querySelector("#music-span");
const outsideSpan = document.querySelector("#outside-span");
const cashSpan = document.querySelector("#cash-span");
const animalsSpan = document.querySelector("#animals-span");

const monSpan = document.querySelector("#mon-span");
const tueSpan = document.querySelector("#tue-span");
const wedSpan = document.querySelector("#wed-span");
const thuSpan = document.querySelector("#thu-span");
const friSpan = document.querySelector("#fri-span");
const satSpan = document.querySelector("#sat-span");
const sunSpan = document.querySelector("#sun-span");

const webLink = document.querySelector("#web-link");
const mrtSpan = document.querySelector("#mrt-span");
const addressLink = document.querySelector("#address-link");
const phoneSpan = document.querySelector("#phone-span");
const imgDiv = document.querySelector(".image");
const msgDiv = document.querySelector(".msg");




import { getValueColor, scoreRender } from "./datahelper.js";
async function shopInit() {
  const shopApi = `/api/shop/${cafe_id}`;
  const response = await fetch(shopApi, { method: "GET" });
  const result = await response.json();

  if (result.data) {
    const rating_his = result.rating_his;
    const data = result.data;
    shopName.innerText = data.name;
    wifiSpan.innerText = scoreRender(rating_his.wifi);
    wifiSpan.style.color = getValueColor(rating_his.wifi);
    vacaSpan.innerText = scoreRender(rating_his.vacancy);
    vacaSpan.style.color = getValueColor(rating_his.vacancy);
    priceSpan.innerText = scoreRender(rating_his.price);
    priceSpan.style.color = getValueColor(rating_his.price);
    quietSpan.innerText = scoreRender(rating_his.quiet);
    quietSpan.style.color = getValueColor(rating_his.quiet);
    comfortSpan.innerText = scoreRender(rating_his.comfort);
    comfortSpan.style.color = getValueColor(rating_his.comfort);
    foodSpan.innerText = scoreRender(rating_his.food);
    foodSpan.style.color = getValueColor(rating_his.food);
    drinksSpan.innerText = scoreRender(rating_his.drinks);
    drinksSpan.style.color = getValueColor(rating_his.drinks);
    viewSpan.innerText = scoreRender(rating_his.view);
    viewSpan.style.color = getValueColor(rating_his.view);
    toiletsSpan.innerText = scoreRender(rating_his.toilets);
    toiletsSpan.style.color = getValueColor(rating_his.toilets);
    if (result.score_count === 0) {
      scoreCount.innerText = `??????????????????`;
    } else {
      scoreCount.innerText = `?????????????????? ${result.score_count} ???????????????`;
    }

    if (data.speed != 0 && data.speed) {
      speedSpan.innerText = data.speed.toFixed(1);
    }
    
    singleSelling.innerText = scoreRender(data.single_selling);
    singleSelling.style.color = getValueColor(data.single_selling);
    limitedTime.innerText = scoreRender(data.limited_time,'limited_time');
    limitedTime.style.color = getValueColor(data.limited_time);
    dessertSpan.style.color = getValueColor(data.dessert_selling);
    dessertSpan.innerText = scoreRender(data.dessert_selling);
    sockettSpan.style.color = getValueColor(data.socket);
    sockettSpan.innerText = scoreRender(data.socket,'socket');
    mealSpan.style.color = getValueColor(data.meal_selling);
    mealSpan.innerText = scoreRender(data.meal_selling);
    standingSpan.style.color = getValueColor(data.standing_tables);
    standingSpan.innerText =scoreRender(data.standing_tables);
    musicSpan.style.color = getValueColor(data.music);
    musicSpan.innerText = scoreRender(data.music);
    outsideSpan.style.color = getValueColor(data.outdoor_seating);
    outsideSpan.innerText = scoreRender(data.outdoor_seating);
    cashSpan.innerText = scoreRender(data.cash_only);
    cashSpan.style.color = getValueColor(data.cash_only);
    animalsSpan.innerText = scoreRender(data.animals);
    animalsSpan.style.color = getValueColor(data.animals);
    if (result.open_hours) {
      const open_Hr = result.open_hours;
      monSpan.innerText = open_Hr.mon;
      tueSpan.innerText = open_Hr.tue;
      wedSpan.innerText = open_Hr.wed;
      thuSpan.innerText = open_Hr.thu;
      friSpan.innerText = open_Hr.fri;
      satSpan.innerText = open_Hr.sat;
      sunSpan.innerText = open_Hr.sun;
    }

    webLink.innerText = data.website ? data.website : data.facebook;
    webLink.href = data.website ? data.website : data.facebook;

    mrtSpan.innerText = data.transport;
    addressLink.innerText = data.address;
    if (data.address !== null) {
      addressLink.href = `https://www.google.com/maps/place/${data.address}`;
    }

    phoneSpan.innerText = data.telephone;
    const msgContent = result.message;
    if (msgContent !== null) {
      msgDiv.innerText = "";
      for (let msg of msgContent) {
        if (msg !== null) {
          const msgBox = document.createElement("form");
          msgBox.classList.add("msg-box");
          const userBox = document.createElement("div");
          userBox.classList.add("user-box");
          const userName = document.createElement("div");

          userName.innerText = msg.user_name;
          const ImgContainer = document.createElement("div");
          ImgContainer.classList.add("img-container");
          const userImg = document.createElement("img");
          userImg.src = msg.user_avatar;
          ImgContainer.append(userImg);
          userBox.append(ImgContainer, userName);
          //deletion icon
          if (msg.now_user === msg.user_id) {
            const deleteBtn = document.createElement("Button");
            const deleteicon = document.createElement("img");
            deleteicon.src = "/static/icons/icon_delete.png";
            deleteBtn.type = "submit";
            deleteBtn.classList.add("delete-icon");
            deleteBtn.append(deleteicon);
            msgBox.append(deleteBtn);
          }
          //msg id (invisible)
          const msgId = document.createElement("input");
          msgId.style.display = "none";
          msgId.classList.add("msgId");
          msgId.value = msg.msg_id;
          const content = document.createElement("span");
          content.innerText = msg.msg_content;
          content.classList.add("content");

          const favorDiv = document.createElement("div");
          favorDiv.classList.add("msgfavor-div");

          const favorBtn = document.createElement("button");
          favorBtn.classList.add("favor-btn");
          favorBtn.value = msg.msg_id;
          const favorIcon = document.createElement("img");
          if (msg.is_favor) {
            favorIcon.src = "/static/icons/heart-fill.png";
          } else {
            favorIcon.src = "/static/icons/heart-emt.png";
          }
          const likeCount = document.createElement("span");
          likeCount.innerText = msg.like_count;
          favorBtn.append(favorIcon);
          favorDiv.append(favorBtn, likeCount);
          const time = document.createElement("span");
          time.classList.add("time");
          time.innerText = msg.create_time;
          msgBox.append(userBox, msgId, content, favorDiv, time);
          msgDiv.append(msgBox);
        }
      }
    }

    //?????????????????????
    const msgdeletform = document.querySelectorAll("form.msg-box");
    msgdeletform.forEach((form) => {
      form.addEventListener("submit", deleteMsg);
    });

    const msgfavor = document.querySelectorAll(".msgfavor-div");
    msgfavor.forEach((msg) => {
      
      msg.addEventListener("click", favorMsg);
    });

    const imgUrl = result.photo_url;

    if (imgUrl !== null) {
      imgDiv.innerText = "";
      for (let i = imgUrl.length - 1; i >= 0; i--) {
        let container = document.createElement("div");
        
        container.classList.add("img-container");
        let img = document.createElement("img");
        imgUrl[i] = encodeURI(imgUrl[i]);
        img.src = imgUrl[i];
        container.append(img);
        imgDiv.append(container);
      }
    }
  }else{
      // location.assign('/404')
  }

  //????????????check????????????
  const photoBtnCover = document.querySelector(".upload-cover");
  const photoBtnCoverFake = document.querySelector(".upload-cover-fake");

  if (!result.is_login) {
    photoBtnCover.classList.add("hidden");
    photoBtnCoverFake.classList.remove("hidden");
    photoBtnCoverFake.addEventListener("click", () => {
      locatio.assign("/login");
    });
  } else {
    photoBtnCover.classList.remove("hidden");
    photoBtnCoverFake.classList.add("hidden");
  }
}

shopInit();

const cafeFavorApi = `/api/shop/favor`;
async function cafeFavorInit() {
  const response = await fetch(cafeFavorApi + `?cafe_id=${cafe_id}`, {
    method: "GET",
  });
  const result = await response.json();

  if (result.data) {
    const cafeFavorIcon = document.querySelector("#cafe-favor-icon");
    const cafeFavorCount = document.querySelector("#favor-count");
    cafeFavorCount.innerText = "";
    if (result.is_favor) {
      cafeFavorIcon.src = "/static/icons/heart-fill.png";
    } else {
      cafeFavorIcon.src = "/static/icons/heart-emt.png";
    }
   
    if (result.count === 0) {
      cafeFavorCount.innerText = `??????????????????`;
    } else {
      cafeFavorCount.innerText = `??????????????????????????? ${result.count} ???`;
    }
  }
}
//shop favor ?????????
cafeFavorInit();
async function favorCafe(e) {
  e.preventDefault();
  const response = await fetch(userApi, { method: "GET" });
  const result = await response.json();
  if (result.data) {
    fetch(cafeFavorApi + `?cafe_id=${cafe_id}`)
      .then((cafeFres) => cafeFres.json())
      .then((cafeFresult) => {
        if (cafeFresult.is_favor) {
          fetch(cafeFavorApi, {
            method: "DELETE",
            body: JSON.stringify({ cafe_id: cafe_id }),
            headers: new Headers({
              "Content-Type": "application/json",
            }),
          })
            .then((favorres) => favorres.json())
            .then((favorResult) => {
              cafeFavorInit();
            });
        } else {
          fetch(cafeFavorApi, {
            method: "POST",
            body: JSON.stringify({ cafe_id: cafe_id }),
            headers: new Headers({
              "Content-Type": "application/json",
            }),
          })
            .then((favorres) => favorres.json())
            .then((favorResult) => {
              cafeFavorInit();
            });
        }
      });
  } else {
    location.assign("/login");
  }
}

async function browse() {
  const response = await fetch(`/api/shop/view/${cafe_id}`, {
    method: "POST",
  });
  const result = await response.json();
}

browse();

//???????????????
const cafefavorBtn = document.querySelector(".favor");
cafefavorBtn.addEventListener("click", favorCafe);

const ratingUserBtn = document.querySelector(".rating-btn");
ratingUserBtn.addEventListener("click", async (e) => {
  const response = await fetch(userApi, { method: "GET" });
  const result = await response.json();
  if (result.data) {
    location.assign(`/rating/${cafe_id}`);
  } else {
    location.assign("/login");
  }
});

const photoUploadApi = `/api/photo/upload`;
const photoBtn = document.querySelector("#upload-input");
const msgPage = document.querySelector(".msg-page");
const modifiedMsg = document.querySelector("#modified-msg");
async function initPhoto() {
  const response = await fetch(photoUploadApi + `?cafe_id=${cafe_id}`, {
    method: "GET",
  });
  const result = await response.json();
  const imgUrl = result.photo_url_list;

  if ((imgUrl !== null) & (imgUrl !== [])) {
    imgDiv.innerText = "";
    const photoMsg = document.querySelector("#photo-msg");
    for (let i = imgUrl.length - 1; i >= 0; i--) {
      let container = document.createElement("div");
      container.classList.add("img-container");
      let img = document.createElement("img");
      imgUrl[i] = encodeURI(imgUrl[i]);
      img.src = imgUrl[i];
      container.append(img);
      imgDiv.append(container);
    }
    
    photoMsg.innerText = "????????????";
    photoMsg.style.color = "blue";
    msgPage.classList.add('hidden')
    setTimeout(() => {
      photoMsg.innerHTML = "";
    }, 2500);
  }
}

photoBtn.addEventListener("change", (e) => {
  fetch(userApi)
    .then((res) => res.json())
    .then((result) => {
      if (result.data) {
        const formData = new FormData();
        for (let i = 0; i < e.target.files.length; i++) {
          formData.append("file[]", e.target.files[i]);
         
        }
        formData.append("cafe_id", cafe_id);
        const option = {
          method: "POST",
          body: formData,
        };
        msgPage.classList.remove('hidden')
        modifiedMsg.innerHTML="?????????..."
        fetch(photoUploadApi, option)
          .then((photores) => photores.json())
          .then((uploadResult) => {
            const photoMsg = document.querySelector("#photo-msg");
            if (uploadResult.data) {
            
              initPhoto();
              
            } else {
              msgPage.classList.add('hidden')
              photoMsg.innerText = "????????????";
              photoMsg.style.color = "red";
              setTimeout(() => {
                photoMsg.innerHTML = "";
              }, 2500);
            }
          });
        e.target.value = "";
      } else {
        
        location.assign("/login");
      }
    });
});

const messageApi = `/api/message`;
const msgFavorApi = `/api/message/favor`;
const msgForm = document.querySelector(".msg-form");

msgForm.addEventListener("submit", (e) => {
  e.preventDefault();
  fetch(userApi)
    .then((res) => res.json())
    .then((result) => {
      if (result.data) {
        const msg_content = document.querySelector("#message").value;
        let data = {
          cafe_id: cafe_id,
          msg_content: msg_content,
        };
        fetch(messageApi, {
          method: "POST",
          headers: new Headers({ "Content-Type": "application/json" }),
          body: JSON.stringify(data),
        })
          .then((msgres) => msgres.json())
          .then((msgRessult) => {
            if (msgRessult.data) {
              shopInit();
            }
          });
        document.querySelector("#message").value = "";
      } else {
        location.assign("/login");
      }
    });
});

// ??????message
function deleteMsg(e) {
  e.preventDefault();
  const msgId = this.querySelector("input.msgId").value;

  fetch(messageApi, {
    method: "DELETE",
    body: JSON.stringify({ msg_id: msgId }),
    headers: new Headers({
      "Content-Type": "application/json",
    }),
  })
    .then((res) => res.json())
    .then((result) => {
      shopInit();
    });
}

// ??????message
function favorMsg(e) {
  e.preventDefault();
  fetch(userApi)
    .then((res) => res.json())
    .then((result) => {
      if (result.data) {
        let msgId = this.querySelector(".favor-btn").value;
        
        fetch(msgFavorApi + `?msg_id=${msgId}`)
          .then((msgres) => msgres.json())
          .then((msgresult) => {
            if (msgresult.data) {
              fetch(msgFavorApi, {
                method: "DELETE",
                body: JSON.stringify({ msg_id: msgId }),
                headers: new Headers({
                  "Content-Type": "application/json",
                }),
              })
                .then((favorres) => favorres.json())
                .then((favorResult) => {
                  shopInit();
                });
            } else {
              fetch(msgFavorApi, {
                method: "POST",
                body: JSON.stringify({ msg_id: msgId, cafe_id: cafe_id }),
                headers: new Headers({
                  "Content-Type": "application/json",
                }),
              })
                .then((favorres) => favorres.json())
                .then((favorResult) => {
                  shopInit();
                });
            }
          });
      } else {
        location.assign("/login");
      }
    });
}
