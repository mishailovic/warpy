import string
from typing import Dict

import requests

from utils.string import generate_random_string


class Warp:
    def __init__(self, proxies: Dict[str, str]):
        self.session = requests.Session()
        self.session.headers = {"User-Agent": "okhttp/3.12.1"}
        self.session.proxies = proxies

        self.endpoint = f"https://api.cloudflareclient.com/v0{generate_random_string(chars=string.digits)}/"

    def register(self, referrer: str):
        response = self.session.post(
            self.endpoint + "reg", json={"referrer": referrer},
        ).json()

        return response["success"]
