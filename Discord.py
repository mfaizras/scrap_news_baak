import requests as r
from DiscordUser import DiscordUser


class Discord:
    def __init__(self):
        TOKEN_BOT = (
            "MTE4MjkyNTc2NzQzNzQ2MzYzMw.GjJgQh.Kk0ibZpYXqulO9RGYHC_7G1WC6htDLBYq5qZAw"
        )
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
            print(f"Success connect to {user_info.username}!")
        else:
            print("Error to connect DC")

    def send_message(self, channel_id: int, content: str) -> bool:
        results_chunk = split_content(content)
        # Print or use the resulting chunks as needed

        for i, chunk in enumerate(results_chunk):
            print(f"Chunk {i + 1}:", chunk)

    # res = r.post(
    #     f"https://discord.com/api/v10/channels/{channel_id}/messages",
    #     headers=self.headers,
    #     json={
    #         "content": teks,
    #     },
    # )

    # if res.status_code == 200:
    #     return True
    # else:
    #     print(res.json())
    #     return False
