from mastodon import Mastodon, StreamListener
import json
import db

MASTODON_ACCESS_TOKEN = "98RXCXLmcxkfciRAwMvo7l2qmBCSf5CpY-ljwX210hQ"
# mastodon = Mastodon(api_base_url='https://mastodon.online', access_token = os.environ['MASTODON_ACCESS_TOKEN'])
mastodon = Mastodon(api_base_url='https://mastodon.online', access_token=MASTODON_ACCESS_TOKEN)
mastodon.retrieve_mastodon_version()
mastodon.status("109666136628267939")["content"]

m = Mastodon(
    api_base_url=f'https://mastodon.au',
    client_id="qMkLnKkrT3Y5uWu8hXu9AsHyel4Oa7K2A1r06eq3Fg8",
    client_secret="qmOu1yGg1T24uTzFhB3XoPnrDOcjJFE01OQVJGsiWt4",
    # access_token=os.environ['MASTODON_ACCESS_TOKEN']
    access_token=MASTODON_ACCESS_TOKEN
)

class Listener(StreamListener):
    def on_update(self, status):
        # data = json.dumps(status, indent=2, sort_keys=True, default=str, ensure_ascii=False)

        db.save_data(status)
        # print("save success")
        # with open("example-mastodon.json", "a") as outfile:
        #     outfile.write(data)
        #     outfile.write("\n")

print("start crawling")
m.stream_public(Listener())
