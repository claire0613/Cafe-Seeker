// export async function getTotalPages(search_page) {

//     let nowpage=parseInt(search_page);
//     let pageItemContent = ''
//     let prePage=nowpage-1;
    
//     let nextpage= nowpage+3;
    
//     //pre-log
//     if (nowpage==0){
//         pageItemContent+=`
//         <li class="disabled">
//             <span>«</span>
//         </li>`
//     }else{
//         pageItemContent+=`
//         <li class="page-item">
//             <a class="page-link" href="/search?page=${prePage}&keyword=${keyword}" id="previous">
//             «
//             </a>
//         </li>`
//     }
//     //prepage
//     if (nowpage-3>3){

//         for (let i = 0; i < 2; i++){
//             pageItemContent += `
//               <li class="page-item">
//                 <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${i + 1}</a>
//               </li>
//             `
//         }
//         pageItemContent+=`
//                     <li class="disabled">
//                         <span>...</span>
//                     </li>`
//         for (let i = nowpage-3; i < nowpage; i++){
//             pageItemContent += `
//                 <li class="page-item">
//                 <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${i + 1}</a>
//                 </li>
//             `
//         }
//     }else{
//         for (let i = 0; i < nowpage; i++){
//             pageItemContent += `
//                 <li class="page-item">
//                 <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${i + 1}</a>
//                 </li>
//             `
//         }
//     }
//     //now

//         pageItemContent+=`
//                     <li class="active">
//                         <span>${nowpage+1}</span>
//                     </li>`

//     if(nowpage+3<totalPage){
//         for (let i = nowpage+1; i < nowpage+4; i++){
//             pageItemContent += `
//                 <li class="page-item">
//                   <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${i + 1}</a>
//                 </li>
//               `
//           }
//           pageItemContent+=`
//           <li class="disabled">
//               <span>...</span>
//           </li>`
//     }else{
//         for (let i = nowpage+1; i < totalPage; i++) {
//             pageItemContent += `
//                 <li class="page-item">
//                   <a class="page-link" href="/search?page=${i}&keyword=${keyword}">${i + 1}</a>
//                 </li>
      
//               `
//           }
//     }


//     pageItemContent +=` 
//         <li class="page-item">
//         <a class="page-link" href="/search?page=${nowpage+1}&keyword=${keyword}" id="previous">
//         »
//         </a>
//         </li>`
//     pagination.innerHTML = pageItemContent
//   }
   

