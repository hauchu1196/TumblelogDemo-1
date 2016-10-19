import json
from flask import Flask

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run()
