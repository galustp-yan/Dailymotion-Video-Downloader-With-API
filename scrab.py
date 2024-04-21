import requests
import youtube_dl
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os

# Path to your service account credentials file
path_to_your_credentials = "./credentials"
# ID of the Google Drive folder where you want to upload the videos
your_parent_folder_id = "1kVnWxmMGuf5Efkq_G8Dsud"
# Dailymotion username from which you want to download videos
userName = "jahaz1500"

# Dailymotion API URL
url = f"https://api.dailymotion.com/user/{userName}/videos?limit=100&page="

# Google Drive API authentication
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = f'{path_to_your_credentials}.json'
PARENT_FOLDER_ID = f"{your_parent_folder_id}"

def authenticate():
    # Authenticates using service account credentials
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_video(file_path):
    # Uploads video to Google Drive
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name' : uniq_video_title,
        'parents' : [PARENT_FOLDER_ID]
    }

    file = service.files().create(
        body=file_metadata,
        media_body=file_path
    ).execute()

# Lists to store video IDs and titles
video_id_list = []
video_title_list = []

# Fetch videos from Dailymotion
for i in range(1, 9):
    x = requests.get(f"{url}{i}")
    for j in x.json()["list"]:
        video_id_list.append("https://www.dailymotion.com/video/" + j["id"])
        video_title_list.append(j["title"])

# Process each video
for i in range(len(video_id_list)):
    video_url = video_id_list[i]
    uniq_video_title = video_title_list[i]
    uniq_video_path = os.path.abspath(uniq_video_title + ".mp4")

    # Download video using youtube_dl
    ydl_opts = {}
    ydl_opts.setdefault('outtmpl', uniq_video_title + '.mp4')

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Upload video to Google Drive
    upload_video(uniq_video_path)

    # Remove downloaded video file
    os.remove(uniq_video_path)
