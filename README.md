# Dailymotion Video Downloader & Google Drive Uploader

This Python script downloads videos from a Dailymotion user's account and uploads them to Google Drive using the Google Drive API.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system
- Required Python packages installed: `requests`, `youtube_dl`, `google-api-python-client`
  You can install these packages using pip:


- Google Cloud Platform (GCP) service account credentials with access to the Google Drive API. Download the JSON file containing your service account credentials and place it in the `credentials` folder.

## Usage

1. Update the following variables in the script:
 - `path_to_your_credentials`: Path to the folder containing your GCP service account credentials.
 - `your_parent_folder_id`: ID of the Google Drive folder where you want to upload the videos.
 - `userName`: Dailymotion username from which you want to download videos.

2. Run the script:
 
3. The script will download videos from the specified Dailymotion user's account, upload them to Google Drive, and remove the downloaded files after uploading.

## Notes

- This script downloads videos from a Dailymotion user's account, so make sure you have the necessary permissions to download these videos.
- Ensure that your Google Drive quota is sufficient to accommodate the uploaded videos.
- For large video collections, consider running the script on a server or using a task scheduler to automate the process.
