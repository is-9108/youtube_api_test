from apiclient.discovery import build


api_key = "AIzaSyDqZZK_zsS-zoJd7ybGI1cjmlwRqFFENzE"

def get_videos_search(keyword):
    youtube = build('youtube', 'v3', developerKey=api_key)
    youtube_query = youtube.search().list(q=keyword, part='id,snippet', maxResults=5)
    youtube_res = youtube_query.execute()
    return youtube_res.get('items', [])

keyword = input('検索キーワードを入力して下さい：')


result = get_videos_search(keyword)
for item in result:
    if item['id']['kind'] == 'youtube#video':
        print(item['snippet']['title'])
        print('https://www.youtube.com/watch?v=' + item['id']['videoId'])
