function getValueColor(value) {
    if (value === true||value==='yes'||value==='maybe') return '#0c72df';
    if (value === false||value==='no') return 'orange';
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


function scoreRender(value){

    if(value === true||value==='yes'){
      return '是'
    }
    else if(value === false||value==='no'){
      return '否'
    }
    else if(value === 'maybe'){
      return '看座位'
    }
    else  if (value!==null && value !=0){
      value = value.toFixed(1);
      return value+ ' ★'
  }
 
    else{
        return ''

    }
}
export {getValueColor,scoreRender}