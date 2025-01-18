function func(...data){
    // 1. 判斷名字有幾個字
    let middlename = data.map(name => {
        if(name.length === 2 || name.length === 3){
            return name[1];
        }else if(name.length === 4 || name.length === 5){
            return name[2];
        }else{
            return null;
        }
    })
    // 2. 計算每個字出現的次數
    let count ={}
    for (let char of middlename) {
        if (char) {
            count[char] = (count[char] || 0) + 1;
        }
    }
    //3. 找出有唯一中間字的完整姓名
    for (let name of data) {
        let middle;
        if (name.length === 2 || name.length === 3) {
            middle = name[1];
        } else if (name.length === 4 || name.length === 5) {
            middle = name[2];
        }
        if (count[middle] === 1) {
            console.log(name);
            return;
        }
    }
    // 4. 如果沒有唯一的中間字，輸出「沒有」
    console.log("沒有");
}

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安