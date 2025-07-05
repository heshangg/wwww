import os
import requests
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def authenticate():
    secret_path = os.getenv("GOOGLE_SECRET_PATH", "client_secrets.json")
    flow = InstalledAppFlow.from_client_secrets_file(secret_path, SCOPES)
    credentials = flow.run_console()
    return credentials.token

def like_video(access_token, video_id):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "id": video_id,
        "rating": "like"
    }
    response = requests.post("https://www.googleapis.com/youtube/v3/videos/rate", headers=headers, params=params)
    print(f"Status: {response.status_code} - Response: {response.text}")

if __name__ == "__main__":
    token = authenticate()
    video_id = input("Enter YouTube video ID to like: ").strip()
    like_video(token, video_id)
