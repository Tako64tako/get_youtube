from googleapiclient.discovery import build
import re

def get_video_id(url):
    # YouTube URLからビデオIDを抽出するための正規表現
    video_id_match = re.match(r".*v=([^&]*)", url)
    if video_id_match:
        return video_id_match.group(1)
    else:
        raise ValueError("無効なYouTube URLです")

def get_video_details(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()
    return response

if __name__ == "__main__":
    youtube_url = input("YouTubeビデオURLを入力してください: ")
    api_key = input("YouTube Data APIキーを入力してください: ")

    try:
        video_id = get_video_id(youtube_url)
        video_details = get_video_details(video_id, api_key)
        print(video_details)
    except Exception as e:
        print(f"エラーが発生しました: {e}")

