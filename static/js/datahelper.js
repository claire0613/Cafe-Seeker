function getValueColor(value) {
    if (value === true||value==='yes') return '#0c72df';
    if (value==='maybe') return 'orange';
    if (value === false||value==='no') return '#ff3262';
    if (value !== null && value !=='') {
     
      if (value >= 5) return '#0c72df';
      if (value >= 4) return 'rgb(0, 213, 0)';
      if (value >= 3) return 'rgb(194, 201, 0)';
      if (value >= 2) return 'orange';
      if (value >= 1) return 'red';
      if (value >= 0) return 'grey';
    }
    return 'grey';
  }


function scoreRender(value,option){

    if(value === true||value==='yes'){
      return '是'
    }
    else if(value === false||value==='no'){
      return '否'
    }
    else if(value === 'maybe'&& option==='socket'){
      return '看座位'
    }
    else if(value === 'maybe'&& option==='limited_time'){
      return '看情況'
    }
    else  if (value!==null && value !=0 && value !==''){

      value = value.toFixed(1);
      return value+ ' ★'
  }
 
    else{
        return ''

    }
}

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
export {getValueColor,scoreRender,star}