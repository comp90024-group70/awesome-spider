import couchdb
from uuid import uuid4

COUCH_SERVER = "http://172.26.136.13:5984"
server = couchdb.Server(COUCH_SERVER)
server.resource.credentials = ("admin", "wza7626222")


def save_data(data: dict):
    if "mastodon" not in server:
        db = server.create("mastodon")
    else:
        db = server["mastodon"]
    res = {"username": data["account"]["acct"], "content": data["content"],
           "created_at": data["created_at"].strftime("%Y-%m-%d %H:%M:%S"), "_id": uuid4().hex}
    db.save(res)
