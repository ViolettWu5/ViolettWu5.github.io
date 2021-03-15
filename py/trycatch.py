import urllib.request as request
import json
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Get data
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

with request.urlopen(src) as response:
    rawData = json.load(response)

results = rawData["result"]["results"]
resultsLen = len(results)
itemArr = [""] * resultsLen

i = 0
for data in results:
    stitle = data["stitle"]
    longitude = data["longitude"]
    latitude = data["latitude"]
    urlStr = data["file"]
   
    httpStr = "http://"
    indexOfSecondHttp = urlStr.find(httpStr, len(httpStr) - 1, len(urlStr))
    
    if indexOfSecondHttp == -1:  
        url = httpStr
    else:
        url = urlStr[0:indexOfSecondHttp]
    # 存進array: 景點名稱,經度,緯度,圖檔網址
    itemArr[i] = stitle + "," + longitude + "," + latitude + "," + url
    i += 1

with open("data.txt", "w", encoding="utf-8") as file:
    i = 0
    for item in itemArr:
        if i == resultsLen - 1:
            file.write(item)  
        else:
            file.write(item + "\n")
        i += 1
