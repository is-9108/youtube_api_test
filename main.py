from apiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyDqZZK_zsS-zoJd7ybGI1cjmlwRqFFENzE'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


search_response = youtube.search().list(
    part='id,snippet',
    #検索したい文字列を指定
    q='dbd',
    #視聴回数が多い順に取得
    # order='viewCount',
    # type='video',
).execute()

search_response

for sr in search_response.get('items',[]):
    print(sr['snippet']['title'])
    print(sr['snippet']['channelTitle'])
