function getNumber(index){
    let A = Math.floor((index)/3);
    let B = (index)%3;
    let result;
    if (B===1){
        result = 7*A+4;
    }else if(B===2){
        result = 7*A+8;
    }else{
        result = 7*A;
    }
    console.log(result)
}

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
