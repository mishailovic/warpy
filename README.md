[RU](/README_RU.md) | [EN](/README.md)

# Warpy

## Simple tool to add GBs to your Cloudflare WARP+ account

### Configuration

Edit `REFERRER_ID` in [config.py](/config.py) with your WARP id.

`Where can I get my WARP id?`

<details>

<summary>Windows</summary>

![Windows-1](https://i.imgur.com/0II785o.png)

![Windows-2](https://i.imgur.com/SCoiHuJ.png)
</details>

<details>

<summary>Android</summary>

![Android-1](https://i.imgur.com/yuGbDwu.png)

![Android-2](https://i.imgur.com/liPIM31.png)

![Android-3](https://i.imgur.com/WOjsd4y.png)

![Android-4](https://i.imgur.com/O9cbMMt.png)

</details>

### Installation

#### Linux

```text
// debian-based
apt install python3 python3-pip

// arch-based
pacman -Sy python

git clone https://github.com/mishailovic/warpy
cd warpy

pip3 install -r requirements.txt
python3 main.py
```

#### Windows

- [Download Python](https://www.python.org/downloads/)
- [Download repo](https://github.com/mishailovic/warpy/archive/refs/heads/main.zip) and unpack it
- From folder of downloaded repo run cmd/powershell and excute following:
- `py -m pip install -r requirements.txt`
- Launch with - `py main.py` or by double-clicking on main.py
