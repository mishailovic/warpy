from threading import Thread

import proxyscrape
from proxyscrape import get_proxyscrape_resource

from config import REFERRER_ID
from warp import Warp

resource_name = get_proxyscrape_resource("socks5")
collector = proxyscrape.create_collector("default", resources=resource_name)


def register_warp():
    try:
        proxy = collector.get_proxy()
        proxy_string = f"{proxy.type}://{proxy.host}:{proxy.port}"

        warp = Warp({"http": proxy_string, "https": proxy_string})
        print(warp.register(REFERRER_ID))
    except Exception:
        pass


while True:
    Thread(target=register_warp).start()
