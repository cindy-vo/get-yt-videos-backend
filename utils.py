# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import googleapiclient.discovery
import googleapiclient.errors
from settings import Settings

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
settings = Settings()

def temp_function():

    youtube = googleapiclient.discovery.build(
        'youtube', 'v3', developerKey=settings.API_KEY)

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id="Ks-_Mh1QhMc"
    )
    response = request.execute()

    print(response)
temp_function()