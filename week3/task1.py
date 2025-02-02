import urllib.request as request
import json
import csv

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

with request.urlopen(src1) as response:
    data1 = json.load(response)

with request.urlopen(src2) as response:
    data2 = json.load(response)

serial_to_district = {}
for item in data2["data"]:
    serial_no = item["SERIAL_NO"]
    address = item["address"]
    district = address.split("  ")[1][:3]
    serial_to_district[serial_no] = district

spots_dict = {}

#資料一
for item in data1["data"]["results"]:
    serial_no = item["SERIAL_NO"]
    spotTitle = item["stitle"]
    latitude = item["latitude"]
    longitude = item["longitude"]
    images = item["filelist"].split("http")
    image_url = f"http{images[1]}" if len(images) > 1 else ""

    #從資料二取得區域名稱
    district = serial_to_district.get(serial_no, "未知區")

    spots_dict[serial_no] = {
        "title": spotTitle,
        "district": district,
        "longitude": longitude,
        "latitude": latitude,
        "images": image_url,
        "mrt": "",
    }

mrt_dict = {}

#資料二
for item in data2["data"]:
    serial_no = item["SERIAL_NO"]
    mrt_name = item["MRT"]

    if serial_no in spots_dict:
        spots_dict[serial_no]["mrt"] = mrt_name
        if mrt_name not in mrt_dict:
            mrt_dict[mrt_name] = []
        mrt_dict[mrt_name].append(spots_dict[serial_no]["title"])

#spot.csv
with open("spot.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["景點名稱", "地區", "經度", "緯度", "圖片URL"])
    for spot in spots_dict.values():
        writer.writerow([spot["title"], spot["district"], spot["longitude"], spot["latitude"], spot["images"]])

#mrt.csv
with open("mrt.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["捷運站名稱"] + [f"景點名稱{i}" for i in range(1, 11)])
    for mrt_station, spots in mrt_dict.items():
        writer.writerow([mrt_station] + spots[:10])
