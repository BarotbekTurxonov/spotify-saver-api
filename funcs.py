from requests import get
from bs4 import BeautifulSoup
from typing import List, Union


def get_id(url):
    main_url = f"https://api.fabdl.com/spotify/get?url={url}"
    res = get(main_url)
    if res.status_code != 200:
        return None
    else:
        js = res.json()
        if js is not None:
            track_id = js['result']['id']
            return [js['result']['gid'], track_id]


def get_down_link(id,track_id):
    main_url = f"https://api.fabdl.com/spotify/mp3-convert-task/{id}/{track_id}"
    res = get(main_url)
    if res.status_code != 200:
        return None
    else:
        js = res.json()
        if js is not None:
            return f"https://api.fabdl.com{js['result']['download_url']}"
        



def DownloadMusic(UrlList: Union[List[str], str]) -> List[str]:
    audio_urls = []

    if type(UrlList)!=list:
        return "required list"

    for i in UrlList:
        id_for_download = get_id(i)
        if id_for_download is not None:
            gid,track_id = id_for_download[0], id_for_download[1]
            download_link = get_down_link(gid,track_id)
            if download_link is not None:
                audio_urls.append(download_link)
    return audio_urls



