from flask import Flask,request,render_template
from dataclasses import dataclass

server = Flask(__name__)

@dataclass
class Video:
    name:str
    duration:int
    count_likes:int


@dataclass
class Card:
    name:str
    text:str
    count_likes:int


video_list = [
    Video(
        name="Black Sabbath - Paranoid",
        duration=3,
        count_likes=10,    
    )
]

cards = [
    Card(
        name="Паста про жаренный суп",
        text="Мой батя делает вообще адовые блюда",
        count_likes=10,
    )
]

@server.get("/videos")
def get_videos():
    return render_template("index.html",videos=video_list)

@server.get("/posts")
def get_posts():
    return render_template("posts.html",posts=cards)

@server.post("/videos/add")
def add_video():
    video = Video(
        name=request.json["name"],
        duration=request.json["duration"],
        count_likes=request.json["count_likes"],
    )
    video_list.append(video)
    print(video_list)
    return "Видео добавлено"

if __name__=='__main__':
    server.run()