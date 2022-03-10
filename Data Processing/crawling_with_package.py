# * Google, 360 ~ 380개가 최대로 보임.
from google_images_download import google_images_download

# from urllib.parse import quote_plus

response = google_images_download.googleimagesdownload()


# kewords = ["종이 클립", "스틱 커피", "열쇠 -목걸이 -팔찌 -순금"]
# kewords = ["스틱형 +식품", "열쇠 키 -도어락 -스마트키 -만능열쇠 -목걸이"]
kewords = ["room key", "house key"]

# creating list of arguments
for keword in kewords:
    arguments = {
        "keywords": keword,
        "limit": 1000,
        "print_urls": True,
        "chromedriver": "chromedriver",
    }

    paths = response.download(arguments)
    # print(paths)


# # * Bing, 정말 2000개의 이미지가 검색되는지는 모르겠지만, 중복으로 갯수를 채우는 듯하므로 중복 제거할 것.
import os
from bing_image_downloader import downloader


# query_string : String to be searched.
# limit : (optional, default is 100) Number of images to download.
# output_dir : (optional, default is 'dataset') Name of output dir.
# adult_filter_off : (optional, default is True) Enable of disable adult filteration.
# force_replace : (optional, default is False) Delete folder if present and start a fresh download.
# timeout : (optional, default is 60) timeout for connection in seconds.
# verbose : (optional, default is True) Enable downloaded message.

# kewords = ["Beer", "Berry", "Top", "Bird", "Butterfly"]

for query_string in kewords:
    limit = 1000  # - len(os.listdir("./downloads/" + query_string))
    downloader.download(query_string, limit=limit, output_dir="downloads")
