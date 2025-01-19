mrt_stations = {
    "Songshan": {"Nanjing Sanmin": 1},
    "Nanjing Sanmin": {"Songshan": 1, "Taipei Arena": 1},
    "Taipei Arena": {"Nanjing Sanmin": 1, "Nanjing Fuxing": 1},
    "Nanjing Fuxing": {"Taipei Arena": 1, "Songjiang Nanjing": 1},
    "Songjiang Nanjing": {"Nanjing Fuxing": 1, "Zhongshan": 1},
    "Zhongshan": {"Songjiang Nanjing": 1, "Ximen": 1},
    "Ximen": {"Zhongshan": 1, "Xiaonanmen": 1},
    "Xiaonanmen": {"Ximen": 1, "Chiang Kai-shek Memorial Hall": 1},
    "Chiang Kai-shek Memorial Hall": {"Xiaonanmen": 1, "Guting": 1},
    "Guting": {"Chiang Kai-shek Memorial Hall": 1, "Taipower Building": 1},
    "Taipower Building": {"Guting": 1, "Gongguan": 1},
    "Gongguan": {"Taipower Building": 1, "Wanlong": 1},
    "Wanlong": {"Gongguan": 1, "Jingmei": 1},
    "Jingmei": {"Wanlong": 1, "Dapinglin": 1},
    "Dapinglin": {"Jingmei": 1, "Qizhang": 1},
    "Qizhang": {"Dapinglin": 1, "Xindian City Hall": 1, "Xiaobitan": 1},
    "Xiaobitan": {"Qizhang": 1},
    "Xindian City Hall": {"Qizhang": 1, "Xindian": 1},
    "Xindian": {"Xindian City Hall": 1}
}

def find_and_print(messages, current_station):
    closest_friend = None
    min_distance = float('inf')

    def station_distance(start, end):
        if start == end:
            return 0
        visited = set()
        queue = [(start, 0)]

        while queue:
            station, distance = queue.pop(0)

            if station == end:
                return distance

            visited.add(station)

            for neighbor, dist in mrt_stations[station].items():
                if neighbor not in visited:
                    queue.append((neighbor, distance + dist))
        
        return float('inf')

    def station_name(message):
        for station in mrt_stations.keys():
            if station in message:
                return station
        return None

    for friend, message in messages.items():
        station = station_name(message)
        if station:
            distance = station_distance(current_station, station)
            if distance < min_distance:
                min_distance = distance
                closest_friend = friend

    if closest_friend:
        print(closest_friend)


messages = {
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Leslie": "I'm at home near Xiaobitan station.",
    "Vivian": "I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
find_and_print(messages, "Qizhang")  # print Leslie
find_and_print(messages, "Ximen")  # print Bob
find_and_print(messages, "Xindian City Hall")  # print Vivian