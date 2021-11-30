import youtube_dl
import re
import random
import requests

all_urls = []

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s', 'quiet':True,})

def get_all_urls(url):
    urls = []
    with ydl:
        result = ydl.extract_info(url, download=False) #We just want to extract the info
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries']
            #loops entries to grab each video_url
            for item in video:
                urls.append(item['url'])
    return urls

def getPlaylistLinks(url: str) -> map:
    page_text = requests.get(url).text
    parser = re.compile(r"watch\?v=\S+?list=")
    playlist = set(re.findall(parser, page_text))
    playlist = map(
        (lambda x: "https://www.youtube.com/" + x.replace("\\u0026list=", "")), playlist
    )
    return [i for i in playlist]

playlist_urls = [
    "https://zingmp3.vn/playlist/XONE-Today-s-Hits-XONE-RADIO/68FB8B8O.html",
    "https://zingmp3.vn/album/Top-100-Bai-Hat-Nhac-Tre-Hay-Nhat-Various-Artists/ZWZB969E.html",
    "https://zingmp3.vn/album/Top-100-Pop-Au-My-Hay-Nhat-Various-Artists/ZWZB96AB.html",
    "https://zingmp3.vn/album/Top-100-Nhac-Tru-Tinh-Hay-Nhat-Various-Artists/ZWZB969F.html",
    "https://zingmp3.vn/album/Top-100-Nhac-Electronic-Dance-Au-My-Hay-Nhat-Various-Artists/ZWZB96C7.html",
    "https://zingmp3.vn/album/Hoa-Tau-V-Pop-Hoang-Rob-Vu-Dang-Quoc-Viet-An-Coong-Minh-Tam-Bui/6IIC8ZID.html",
    "https://zingmp3.vn/album/Hoa-Tau-Saxophone-Kenny-G-Jerry-Bergonzi-Chris-Botti-Boney-James/6IID9U9B.html",
    "https://zingmp3.vn/album/Hoa-Tau-Cello-Hauser-David-Darling-2Cellos-The-Piano-Guys/6IIC9CUF.html",
    "https://zingmp3.vn/album/Ken-Viet-Tran-Manh-Tuan-Quyen-Van-Minh-Xuan-Hieu-Le-Tan-Quoc/6IID9W68.html",
    "https://zingmp3.vn/album/Instrumental-Love-Songs-Kenny-G-Yiruma-Michael-Omartian-James-Galway/6IIDBCBB.html",
    "https://zingmp3.vn/album/Hoa-Tau-Guitar-Julian-Bream-Francis-Goya-Govi-Jesse-Cook/6IIDAEAF.html",
    "https://zingmp3.vn/album/Hoa-Tau-Piano-Ludovico-Einaudi-The-Piano-Guys-Glenn-Gould-Yiruma/6IID06BD.html",
    "https://zingmp3.vn/album/Hoa-Tau-Violin-Co-Dien-Joshua-Bell-Andre-Rieu-Jascha-Heifetz-Gil-Shaham/6IIDACUZ.html",
    "https://zingmp3.vn/album/Hoa-Tau-Violin-Hien-Dai-Joshua-Bell-Lindsey-Stirling-Hoang-Rob-Bond/6IIDBOWA.html",
    "https://zingmp3.vn/album/Hoa-Tau-Bat-Hu-Yanni-Richard-Clayderman-Kenny-G-Chet-Atkins/ZOBC0OFF.html",
    "https://zingmp3.vn/album/Hoa-Tau-Bolero-Hai-Phuong-Phuong-Thuy-Hoa-Tau/ZOFUB9ZI.html",
    "https://zingmp3.vn/album/Nhac-Phim-Khong-Loi-Hay-Nhat-Suzy-Ailee-AKMU-Eddy-Kim/ZOUUFWOC.html",
    "https://zingmp3.vn/album/DJ-Station-DJ-Snake-Selena-Gomez-Zedd-Ariana-Grande/676OF6OA.html"
]

youtube_urls = [
    'https://www.youtube.com/watch?v=VNdHd1asf9s',
    'https://www.youtube.com/watch?v=IGADP2i1ItQ',
    'https://www.youtube.com/watch?v=xPyCjiHIUVw&t=1344s',
    'https://www.youtube.com/watch?v=J1AD7yOInOs',
    'https://www.youtube.com/watch?v=i4Nn6Gx2Uv8',
    'https://www.youtube.com/watch?v=i4Nn6Gx2Uv8',
    "https://www.youtube.com/playlist?list=PLC2917B93A4BC35F4",
    "https://www.youtube.com/playlist?list=PLStP-_PrFZ0jilkK7GxNrBOC0KlGjDLOS",
    "https://www.youtube.com/playlist?list=PLRBp0Fe2GpglvwYma4hf0fJy0sWaNY_CL",
    "https://www.youtube.com/playlist?list=PL4fGSI1pDJn688ebB8czINn0_nov50e3A",
    "https://www.youtube.com/playlist?list=PL8A83124F1D79BD4F",
    "https://www.youtube.com/playlist?list=PL9kvoia9QAFhiIZLU2RJdWJS-aDCvxbL9",
    "https://www.youtube.com/playlist?list=PLlR_o1XmlePugi6qO7Pjfz6G3o89V6__C",
    "https://www.youtube.com/playlist?list=PLd-JGjCltpgBeIZHnMxhRafubqKfUZG3_",
    "https://www.youtube.com/watch?v=8qTvAEs-tTw&list=PL9kKQ7xjE8HO9xBZin_Kqnu8MCx-bJcyL",
    "https://www.youtube.com/playlist?list=PL3u2OPYgOJm1OS2C2BcLCSNNHl82OyuKJ",
    "https://www.youtube.com/playlist?list=PLd4nO0K8sr86EPsCSLdcZH8VsCLrk82Qf",
    "https://www.youtube.com/playlist?list=PL0fOnDVUOp53psjfFLKPq1ApsEIql6rzn",
    "https://www.youtube.com/playlist?list=PLzRKj0jD-GZaHPkYY2Z3vs3INg5PseIJs",
    "https://www.youtube.com/playlist?list=PLI4DZVYqSXKPofeqgttHUc0fv_poIpNM9"

]

for playlist_url in playlist_urls:
    print(playlist_url)
    all_urls += get_all_urls(playlist_url)

all_urls += [i for i in youtube_urls if "playlist?list" not in i]
for playlist_url in [i for i in youtube_urls if "playlist?list" in i]:
    print(playlist_url)
    all_urls += getPlaylistLinks(playlist_url)

random.shuffle(all_urls)
print("all_urls: ", all_urls)

with open("url.txt", "w") as f:
    f.write("\n".join(all_urls))
print("done!")
