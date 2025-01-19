const mrtStations = {
    "Songshan": { "Nanjing Sanmin": 1 },
    "Nanjing Sanmin": { "Songshan": 1, "Taipei Arena": 1 },
    "Taipei Arena": { "Nanjing Sanmin": 1, "Nanjing Fuxing": 1 },
    "Nanjing Fuxing": { "Taipei Arena": 1, "Songjiang Nanjing": 1 },
    "Songjiang Nanjing": { "Nanjing Fuxing": 1, "Zhongshan": 1 },
    "Zhongshan": { "Songjiang Nanjing": 1, "Ximen": 1 },
    "Ximen": { "Zhongshan": 1, "Xiaonanmen": 1 },
    "Xiaonanmen": { "Ximen": 1, "Chiang Kai-shek Memorial Hall": 1 },
    "Chiang Kai-shek Memorial Hall": { "Xiaonanmen": 1, "Guting": 1 },
    "Guting": { "Chiang Kai-shek Memorial Hall": 1, "Taipower Building": 1 },
    "Taipower Building": { "Guting": 1, "Gongguan": 1 },
    "Gongguan": { "Taipower Building": 1, "Wanlong": 1 },
    "Wanlong": { "Gongguan": 1, "Jingmei": 1 },
    "Jingmei": { "Wanlong": 1, "Dapinglin": 1 },
    "Dapinglin": { "Jingmei": 1, "Qizhang": 1 },
    "Qizhang": { "Dapinglin": 1, "Xindian City Hall": 1, "Xiaobitan": 1 },
    "Xiaobitan": { "Qizhang": 1 },
    "Xindian City Hall": { "Qizhang": 1, "Xindian": 1 },
    "Xindian": { "Xindian City Hall": 1 }
};
function findAndPrint(messages, currentStation) {
    let closestFriend = null;
    let minDistance = Infinity;

    //計算兩站間的距離
    function stationDistance(start, end) {
        if (start === end) return 0;
        let visited = new Set();
        let queue = [[start, 0]]; // [currentStation, distance]

        while (queue.length > 0) {
            let [station, distance] = queue.shift();

            if (station === end) return distance;

            visited.add(station);

            for (let neighbor in mrtStations[station]) {
                if (!visited.has(neighbor)) {
                    queue.push([neighbor, distance + mrtStations[station][neighbor]]);
                }
            }
        }
        return Infinity;
    }

    function stationName(message) {
        for (let station in mrtStations) {
            if (message.includes(station)) {
                return station;
            }
        }
        return null;
    }

    for (let [friend, message] of Object.entries(messages)) {
        let station = stationName(message);
        if (station) {
            let distance = stationDistance(currentStation, station);
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
