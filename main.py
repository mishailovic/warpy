from threading import Thread, get_ident

import proxyscrape
from proxyscrape import get_proxyscrape_resource
from rich.console import Console

from config import REFERRER_ID
from warp import Warp

c = Console()

resource_name = get_proxyscrape_resource("socks5")
collector = proxyscrape.create_collector("default", resources=resource_name)


def register_warp(ident: int):
    try:
        proxy = collector.get_proxy()
        proxy_string = f"{proxy.type}://{proxy.host}:{proxy.port}"
        warp = Warp({"http": proxy_string, "https": proxy_string})
        if warp.register(REFERRER_ID):
            c.print(f"[green b][W#{ident}][/] Successfully added 1GB")
    except:
        pass


def worker():
    ident = get_ident()
    while True:
        register_warp(ident)


def main():
    workers = int(c.input("[green]Workers [1024] >[/] ") or 1024)
    with c.status("Starting workers..."):
        for _ in range(workers):
            Thread(target=worker).start()


main()
