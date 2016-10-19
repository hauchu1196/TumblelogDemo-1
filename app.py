from mongoengine import *
from mlab import *
import json
from flask import *

app = Flask(__name__)

class Post(Document):
    title = StringField()
    content = StringField()

    def get_json(self):
        return {"title": self.title, 'content': self.content}


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
    posts = Post.objects
    return json.dumps([post.get_json() for post in posts])

@app.route('/addpost',methods=["POST"])
def addpost():
    args = request.form
    title_value = args["title"]
    content_value = args["content"]

    p = Post(title = title_value, content = content_value)
    p.save()


    return  jsonify({"code" : 1, "message" : "OK"})


if __name__ == '__main__':
    mlab_connect()
    app.run()
