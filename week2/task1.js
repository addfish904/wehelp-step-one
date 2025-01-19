const mrtStations = [
    "Songshan",
    "Nanjing Sanmin",
    "Taipei Arena",
    "Nanjing Fuxing",
    "Songjiang Nanjing",
    "Zhongshan",
    "Ximen",
    "Xiaonanmen",
    "Chiang Kai-shek Memorial Hall",
    "Guting",
    "Taipower Building",
    "Gongguan",
    "Wanlong",
    "Jingmei",
    "Dapinglin",
    "Qizhang",
    "Xindian City Hall",
    "Xindian"
];

function findAndPrint(messages, currentStation) {
    let closestFriend = null;
    let minDistance = Infinity;

    //找到訊息中的站名
    function stationName(message) {
        for (let station of mrtStations) {
            if (message.includes(station)) {
                return station;
            }
        }
        return null;
    }
    //計算兩個站之間的距離
    function stationDistance(station1, station2) {
        let index1 = mrtStations.indexOf(station1);
        let index2 = mrtStations.indexOf(station2);
        return Math.abs(index1 - index2);
    }
    //判斷哪位朋友最近
    for (let [friend, message] of Object.entries(messages)) {
        let station = stationName(message);
        if (station) {
            let distance = stationDistance(station, currentStation);
            if (distance < minDistance) {
                minDistance = distance;
                closestFriend = friend;
            }
        }
    }
    if (closestFriend) {
        console.log(closestFriend);
    } 
}

const messages = {
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Leslie": "I'm at home near Xiaobitan station.",
    "Vivian": "I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian
