import urllib.request as request
import json
import csv

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

with request.urlopen(src1) as response:
    data1 = json.load(response)

districts = ["中正區", "萬華區", "中山區", "大同區", "大安區", "松山區", "信義區", "士林區", "文山區", "北投區", "內湖區", "南港區"]
spots_dict = {}

#資料1
for item in data1["data"]["results"]:
    serial_no = item["SERIAL_NO"]
    spotTitle = item["stitle"]
    latitude = item["latitude"]
    longitude = item["longitude"]
    images = item["filelist"].split("http")
    address = item["info"]
    district = next((d for d in districts if d in address), "未知區")

    spots_dict[serial_no] = {
        "title": spotTitle,
        "district": district,
        "longitude": longitude,
        "latitude": latitude,
        "images": ["http" + img for img in images if img][0],
        "mrt": "",
    }

#資料2
with request.urlopen(src2) as response:
    data2 = json.load(response)

mrt_dict = {}

for item in data2["data"]:
    serial_no = item["SERIAL_NO"]
    mrt_name = item["MRT"]
    
    if serial_no in spots_dict:
        spots_dict[serial_no]["mrt"] = mrt_name
        if mrt_name not in mrt_dict:
            mrt_dict[mrt_name] = []
        mrt_dict[mrt_name].append(spots_dict[serial_no]["title"])

with open("spot.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["景點名稱", "地區", "經度", "緯度", "圖片URL"])
    for spot in spots_dict.values():
        writer.writerow([spot["title"], spot["district"], spot["longitude"], spot["latitude"], spot["images"]])

with open("mrt.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["捷運站名稱"] + [f"景點名稱{i}" for i in range(1, 11)])
    for mrt_station, spots in mrt_dict.items():
        writer.writerow([mrt_station] + spots[:10])
