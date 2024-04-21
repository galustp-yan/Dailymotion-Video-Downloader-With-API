import requests
import youtube_dl
import os

# List to store video URLs and titles
video_href_list = []
video_title_list = []

# Dailymotion username
userName = "jahaz1500"

# Dailymotion API URL
url = f"https://api.dailymotion.com/user/{userName}/videos?limit=100&page="

# Fetch video information from Dailymotion API
for i in range(1, 2):
    x = requests.get(f"{url}{i}")
    for j in x.json()["list"]:
        video_href_list.append("https://www.dailymotion.com/video/" + j["id"])
        video_title_list.append(j["title"])

# Select a video URL
video_url = video_href_list[6]

# Define options for youtube-dl 
ydl_opts = {}
ydl_opts.setdefault('outtmpl', video_title_list[6] + '.mp4')

# Download the selected video using youtube-dl
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# Print the absolute path of the downloaded video
print(os.path.abspath(video_title_list[6] + ".mp4"))
