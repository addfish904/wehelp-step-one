mrt_stations = [
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
]

mrt_connections = {
    "Qizhang": ["Xiaobitan"]
}

def find_and_print(messages, current_station):
    closest_friend = None
    min_distance = float('inf')

    def station_name(message):
        for station in mrt_stations:
            if station in message:
                return station
        return None

    def station_distance(station1, station2):
        index1 = mrt_stations.index(station1)
        index2 = mrt_stations.index(station2)
        return abs(index1 - index2)

    for friend, message in messages.items():
        station = station_name(message)
        if station:
            distance = station_distance(station, current_station)
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
