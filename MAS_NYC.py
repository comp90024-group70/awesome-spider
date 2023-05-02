from mastodon import Mastodon, StreamListener
import json

MASTODON_ACCESS_TOKEN="YS52bryI99dSIx7Gwxww_7D7UD31P8P1rQbmxF22YmU"
# mastodon = Mastodon(api_base_url='https://mastodon.online', access_token = os.environ['MASTODON_ACCESS_TOKEN'])
mastodon = Mastodon(api_base_url='https://mastodon.online', access_token = MASTODON_ACCESS_TOKEN)
mastodon.retrieve_mastodon_version()
mastodon.status("109666136628267939")["content"]

m = Mastodon(
        api_base_url=f'https://masto.nyc',
        # access_token=os.environ['MASTODON_ACCESS_TOKEN']
        access_token = MASTODON_ACCESS_TOKEN
    )

class Listener(StreamListener):
    def on_update(self, status):
        data = json.dumps(status, indent=2, sort_keys=True, default=str, ensure_ascii=False)
        # print(data)
        with open("MAS_NYC.json", "a") as outfile:
            outfile.write(data)
            outfile.write("\n")
m.stream_public(Listener())