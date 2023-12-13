import requests as r
from DiscordUser import DiscordUser
from dotenv import load_dotenv
import os


class Discord:
    def __init__(self):
        load_dotenv()
        TOKEN_BOT = os.getenv("TOKEN_DISCORD")
        
        self.headers = {
            "Authorization": f"Bot {TOKEN_BOT}",
            "Content-Type": "application/json",
        }

        res = r.get(
            "https://discord.com/api/v10/users/@me",
            headers=self.headers,
        )

        if res.status_code == 200:
            user_info = DiscordUser(res.json())
            self.send_message(os.getenv("CHANNEL_COMMAND"), "Success connect to Discord!")
        else:
            print("Failed to connect Discord!")
            print(res.json())

    def send_message(self, channel_id: int, content: str) -> bool:
        res = r.post(
            f"https://discord.com/api/v10/channels/{channel_id}/messages",
            headers=self.headers,
            json={
                "content": content,
            },
        )

        if res.status_code == 200:
            return True
        else:
            print(res.json())
            return False
