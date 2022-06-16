const userPhoto = document.querySelector("#user-photo");
const modityPhoto=document.querySelector(".modity-photo")
const userNameAuto = document.querySelector(".username-auto");
const userEmail = document.querySelector("#email");
const userNameSave = document.querySelector(".username-save");
const userNameEdit = document.querySelector(".username-edit");
const userNameEditIcon = document.querySelector("#username-edit-icon");
const userNameSaveIcon = document.querySelector("#username-save-icon");
const userNameCancleIcon = document.querySelector("#username-cancle-icon");
const modifiedMsg = document.querySelector("#modified-msg");
const msgPage = document.querySelector(".msg-page");

const memberRightBtn = document.querySelector("#rightbtn");
const memberleftBtn = document.querySelector("#leftbtn");
const memberpageError = document.querySelector(".error-msg");
const favorDiv=document.querySelector('.favor-div');
const photoDiv=document.querySelector('.photo-div');
const cafeDeleteBtn=document.querySelector('cafe-delete-icon')
const photoDeleteBtn=document.querySelector('photo-delete-icon')
const photoUserUpload=document.querySelector('#photo-upload-input')

let publicFavorScroll = true;
let publicFavorPage=0;
let publicPhotoScroll = true;
let publicPhotoPage=0;
msgPage.classList.remove('hidden')
modifiedMsg.innerHTML="Loading ..."
async function getMemberInfo() {

  favorDiv.innerText='';
  photoDiv.innerText='';
  publicFavorPage=0
  publicPhotoPage=0;
  const response = await fetch(userApi);
  const result = await response.json();

  if (result.data) {
    setTimeout(()=>{
      msgPage.classList.add('hidden')
      
    },1500)
    userPhoto.src =  result.data.avatar;
    userNameAuto.innerHTML = result.data.username;
    userEmail.innerHTML = result.data.email;
    let cafepromise=mebCafeFavorFetch(publicFavorPage)
    let photopromise=mebPhotoFetch(publicFavorPage)
    
    
    cafepromise.then((result)=>{
      
      let next_page = result["nextPage"];
      publicFavorPage = next_page;
      publicFavorScroll = true;
      renderCafe(result.data)
     
    })
    photopromise.then((result)=>{
      
      let next_page = result["nextPage"];
      publicPhotoPage = next_page;
      publicPhotoScroll = true;
      renderPhoto(result.data)
  
    })
 

    
  } else {
    location.replace("/");
  }
}
//初始畫面
getMemberInfo();
photoUserUpload.addEventListener('change',async(e)=>{
  const formData = new FormData();
  const response = await fetch(userApi);
  const result = await response.json();
  if(result.data){
    formData.append("file", e.target.files[0]);
    const option = {
      method: "POST",
      body: formData,
    };
    const uploadres = await fetch('/api/member/userphoto',option);
    const uploadResult = await uploadres.json();
    if (uploadResult){
      getMemberInfo();
      modifiedMsg.innerHTML='更新成功';
      msgPage.classList.remove('hidden')
      setTimeout(()=>{
        
        msgPage.classList.add('hidden')
        

      },2000)
    }else{
      msgPage.classList.remove('hidden')
      modifiedMsg.innerHTML="更新失敗"
      setTimeout(()=>{
        msgPage.classList.add('hidden')
        
      },2000)
    }
  }

})







async function cafeFavorDelete(e){
 
  const cafe_id=this.value


        
        
 
  const cafeFavorApi = `/api/shop/favor`;
  const response=await fetch(cafeFavorApi,{
    method: "DELETE",
    body: JSON.stringify({ cafe_id: cafe_id }),
    headers: new Headers({
      "Content-Type": "application/json",
    })
  });
  const result=await response.json();
  if(result){
    
    const target=e.target;
    let favorDelbox=target.parentElement.parentElement
    favorDelbox.style.display="none"

  }
   
  
}


async function photoDelete(e){
  const photo_id=this.value
  const photoFavorApi = `/api/photo/upload`;
  const response=await fetch(photoFavorApi,{
    method: "DELETE",
    body: JSON.stringify({ photo_id: photo_id }),
    headers: new Headers({
      "Content-Type": "application/json",
    })
  });
  const result=await response.json();
  if(result){
     
    const target=e.target;
    let photDelbox=target.parentElement.parentElement
    photDelbox.style.display="none"
    
  }
   
  
}




//cafe收藏fetch
async function mebCafeFavorFetch(publicFavorPage){
try {
  const mebCafeFavorApi=`/api/member/favor?page=${publicFavorPage}`
  const response = await fetch(mebCafeFavorApi);
  const result = await response.json();
 
  
  return result
} catch (message) {
  console.log(`${message}`);
  throw Error('Fetching was not ok!!.');
} 
}


//cafe收藏view
async function renderCafe(data) {
    favorDiv.innerText=''
   
    createCafe(data)
    const cafefavor = document.querySelectorAll(".cafe-delete-icon");
    cafefavor.forEach((favor) => {
     
      favor.addEventListener("click", cafeFavorDelete);
    });
    
    favorDiv.addEventListener("scroll", function () { 
//註冊滑動載入事件

      if (this.scrollHeight - this.scrollTop -5<= this.clientHeight) {
        
        if (publicFavorScroll && publicFavorPage) {
          publicFavorScroll = false;
          let promise = mebCafeFavorFetch(publicFavorPage);
          promise.then((result) => {
            publicFavorScroll = true;
            let next_page = result["nextPage"];
            publicFavorPage = next_page;
            createCafe(result.data)
            const cafefavor = document.querySelectorAll(".cafe-delete-icon");
            cafefavor.forEach((favor) => {
           
              favor.addEventListener("click", cafeFavorDelete);
            });
         
           
          });
        }
      };
    });
    

  }


//cafe收藏view helper
async function createCafe(data){
  for (let cafe of data){
   
    const cafeBox=document.createElement('div')
    cafeBox.classList.add('favor-box')
    const imgLink = document.createElement("a");
    imgLink.href=`/shop/${cafe.id}`
    imgLink.classList.add("img-container");
    
    const img = document.createElement("img");
    if (cafe.photo_url) {
      let url = encodeURI(cafe.photo_url);
      img.src = url;
  
    }else{
      let comment=document.createElement('div')
      comment.classList.add('comment')
      
      imgLink.append(comment);
    }
    imgLink.append(img);
   
    const name=document.createElement('div')
    name.innerText=cafe.name;
    
    const deleteBtn = document.createElement("Button");
    const deleteicon = document.createElement("img");
    deleteicon.src = "/static/icons/icon_delete.png";
    deleteBtn.type = "submit";
    deleteBtn.classList.add("cafe-delete-icon");
    deleteBtn.value =cafe.id;
    deleteBtn.append(deleteicon);
    cafeBox.append(imgLink,name,deleteBtn);
    favorDiv.append(cafeBox)

}

}





//photo紀錄fetch
async function mebPhotoFetch(data){
  try {
    const mebPhotoApi=`/api/member/photo?page=${publicPhotoPage}`
    const response = await fetch(mebPhotoApi);
    const result = await response.json();
    return result
  } catch (message) {
    console.log(`${message}`);
    throw Error('Fetching was not ok!!.');
  } 
}
//photo紀錄 view
async function renderPhoto(data) {
  photoDiv.innerText='';
  createPhoto(data)
  const photoBox = document.querySelectorAll(".photo-delete-icon");
  photoBox.forEach((pic) => {
    pic.addEventListener("click", photoDelete);
  });
  photoDiv.addEventListener("scroll", function () { 
//註冊滑動載入事件

    if (this.scrollHeight - this.scrollTop -5<= this.clientHeight) {
     
      if (publicPhotoScroll && publicPhotoPage) {
       
        publicPhotoScroll = false;
        let promise = mebPhotoFetch(publicPhotoPage);
        promise.then((result) => {
         
          publicPhotoScroll = true;
          let next_page = result["nextPage"];
          publicPhotoPage = next_page;
          createPhoto(result.data)
          const photoBox = document.querySelectorAll(".photo-delete-icon");
          photoBox.forEach((pic) => {
            pic.addEventListener("click", photoDelete);
          });
       
         
        });
      }
    };
  });

}

//photo紀錄 view-helper
async function createPhoto(data){
  for (let photo of data){
    
    const photoBox=document.createElement('div')
    photoBox.classList.add('photo-box')
    const imgLink = document.createElement("a");
    imgLink.href=`/shop/${photo.cafe_id}`
    imgLink.classList.add("img-container");

    const img = document.createElement("img");
    let url = encodeURI(photo.photo_url);
    img.src = url;
    imgLink.append(img);
   
    const name=document.createElement('div')
    name.innerText=photo.cafe_name;
    const photo_name=photo.photo_name.split('_')[1]
   
    const photoName=document.createElement('div')
    photoName.innerText=photo_name;
    const time=document.createElement('div')
    time.innerText=photo.create_time
    
    const deleteBtn = document.createElement("Button");
    const deleteicon = document.createElement("img");
    deleteicon.src = "/static/icons/icon_delete.png";
    deleteBtn.type = "submit";
    deleteBtn.classList.add("photo-delete-icon");
    deleteBtn.value =photo.photo_id;
    deleteBtn.append(deleteicon);

    photoBox.append(imgLink,name,photoName,time,deleteBtn);
    photoDiv.append(photoBox)

}
}




//更新userInfo


userNameEditIcon.addEventListener("click",()=>{
  userNameSave.classList.add('hide');
  userNameEdit.classList.remove('hide');
 

})
userNameSaveIcon.addEventListener('click',async(e)=>{
  const newName=document.querySelector('#newName').value.trim()
  const data={
      "newName":newName,
      "pwd":null
  }
  const option={
      method: 'POST',
      headers: new Headers({
          'Content-Type': 'application/json'
        }),
      body: JSON.stringify(data)
  }
  const response= await fetch('/api/user/update',option);
  const promise=await response.json();
  const result=await promise;
  if (result.ok){
      modifiedMsg.innerHTML="更新成功"
      userNameSave.classList.remove('hide');
      userNameEdit.classList.add('hide');
      userNameAuto.innerHTML=newName;
      msgPage.classList.remove('hidden')
      setTimeout(()=>{
        
        msgPage.classList.add('hidden')
        

      },2000)
  }else{
    msgPage.classList.remove('hidden')
    modifiedMsg.innerHTML="更新失敗"
    setTimeout(()=>{
      msgPage.classList.add('hidden')
      
    },2000)
  }
})

userNameCancleIcon.addEventListener('click',()=>{
  userNameSave.classList.remove('hide');
  userNameEdit.classList.add('hide');
})


