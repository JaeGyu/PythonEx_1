from flask import Flask, jsonify
import json


app = Flask(__name__)

class Url:
    def __init__(self, id, tags = []):
        self.id = id
        self.url = "http://sample.url"
        self.title = "sample url~~"
        self.date = "2017-04-01"
        self.tags = tags

    def to_json(self):
        tags = list(map(lambda x: x.to_json(), self.tags)) 
        return {
            "id":self.id,
            "url": self.url,
            "title": self.title,
            "tags" : tags,
            "date" : self.date
        }

class Tag:
    def __init__(self, tag_name, url = []):
        self.tag = tag_name
        self.url = url

    def to_json(self):
        return self.__dict__
    
    def set_url(self, url):
        self.url = url
    

@app.route("/")
def index():
    return "hello"

@app.route("/url")
def get_url():
    t1 = Tag("spring")
    tags = [t1]
    u = Url(1, tags)
    t1.set_url("abc")
    print(u.to_json())
    return jsonify(u.to_json())

if __name__ == "__main__":
    app.run()