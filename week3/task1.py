import urllib.request as request
import json
import csv

src1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
src2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"

# 下載景點資料
with request.urlopen(src1) as response:
    data1 = json.load(response)

# 台北市的行政區列表
districts = ["中正區", "萬華區", "中山區", "大同區", "大安區", "松山區", "信義區", "士林區", "文山區", "北投區", "內湖區", "南港區"]

# 存景點資訊的字典
spots_dict = {}

# 解析資料1
for item in data1["data"]["results"]:
    serial_no = item["SERIAL_NO"]  # 這個 SERIAL_NO 會用來匹配第二份資料
    spotTitle = item["stitle"]
    latitude = item["latitude"]
    longitude = item["longitude"]
    images = item["filelist"].split("http")
    address = item["info"]
    district = next((d for d in districts if d in address), "未知區")

    # 存入字典，key 為 serial_no
    spots_dict[serial_no] = {
        "title": spotTitle,
        "district": district,
        "longitude": longitude,
        "latitude": latitude,
        "images": ["http" + img for img in images if img][0],  # 取得第一張圖片
        "mrt": "",  # 之後再補上 MRT
    }

# 下載 MRT 資料
with request.urlopen(src2) as response:
    data2 = json.load(response)

# 儲存 MRT 對應的景點
mrt_dict = {}

# 解析資料2
for item in data2["data"]:
    serial_no = item["SERIAL_NO"]
    mrt_name = item["MRT"]
    
    if serial_no in spots_dict:
        # 更新景點的 MRT 資訊
        spots_dict[serial_no]["mrt"] = mrt_name

        # 整理 MRT 對應的景點資訊
        if mrt_name not in mrt_dict:
            mrt_dict[mrt_name] = []
        mrt_dict[mrt_name].append(spots_dict[serial_no]["title"])

# 輸出 spot.csv
with open("spot.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["景點名稱", "地區", "經度", "緯度", "圖片URL"])
    for spot in spots_dict.values():
        writer.writerow([spot["title"], spot["district"], spot["longitude"], spot["latitude"], spot["images"]])

# 輸出 mrt.csv
with open("mrt.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["捷運站名稱"] + [f"景點名稱{i}" for i in range(1, 11)])  # 預留 10 個景點名稱欄位
    for mrt_station, spots in mrt_dict.items():
        writer.writerow([mrt_station] + spots[:10])  # 每站最多列出 10 個景點
