from mongoengine import *
from mlab import *
import json
from flask import Flask,request

app = Flask(__name__)

class Post(Document):
    title = StringField()
    content = StringField()

post1 = {
    "title" : "Good day",
    "content" : "I met a girl. She had black eyes and loves dog"
}


post2 = {
    "title" : "Bad day",
    "content" : "I met a gay"
}

print(post1["title"])
print(post1["content"])

posts = [post1,post2]

@app.route('/')
def main():
    return json.dumps(posts)

@app.route('/addpost',methods=["POST"])
def addost():
    args = request.form
    title_value = args["title"]
    content_value = args["content"]
    new_post = {"title":title_value,
                "content":content_value
                }
    posts.append(new_post)
    print(title_value,content_value)
    return  "OK"


if __name__ == '__main__':
    mlap_connect
    app.run()
