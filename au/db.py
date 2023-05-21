import couchdb
from uuid import uuid4
import os

COUCHDB_DOMAIN = os.environ.get("COUCHDB_DOMAIN", "172.26.131.154")
COUCHDB_USER = os.environ.get("COUCHDB_USER", "admin")
COUCHDB_PASSWORD = os.environ.get("COUCHDB_PASSWORD", "wza7626222")
COUCHDB_SERVER = f'http://{COUCHDB_DOMAIN}:5984'
server = couchdb.Server(COUCHDB_SERVER)
server.resource.credentials = (COUCHDB_USER, COUCHDB_PASSWORD)


def save_data(data: dict):
    if "mastodon" not in server:
        db = server.create("mastodon")
    else:
        db = server["mastodon"]
    res = {"username": data["account"]["acct"], "content": data["content"],
           "created_at": data["created_at"].strftime("%Y-%m-%d %H:%M:%S"), "_id": uuid4().hex}
    db.save(res)
