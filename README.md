# Warpy

## Утилита для накрутки гигабайтов в Cloudflare WARP+

### Конфигурация

В [config.py](/config.py) в переменной `REFERRER_ID` укажите свой Warp ID

`Где его взять?`

<details>

<summary>На Windows</summary>

![Windows-1](https://i.imgur.com/0II785o.png)

![Windows-2](https://i.imgur.com/SCoiHuJ.png)
</details>

<details>

<summary>На Android</summary>

![Android-1](https://i.imgur.com/yuGbDwu.png)

![Android-2](https://i.imgur.com/liPIM31.png)

![Android-3](https://i.imgur.com/WOjsd4y.png)

![Android-4](https://i.imgur.com/O9cbMMt.png)

</details>

### Установка на Linux

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

### Установка на Windows

- [Установите Python](https://www.python.org/downloads/)
- [Скачайте репозиторий](https://github.com/mishailovic/warpy/archive/refs/heads/main.zip) и распакуйте его в удобное для вас место
- В распакованной папке откройте cmd/powershell и выполните следующую команду
- `py -m pip install -r requirements.txt`
- Запуск - `py main.py` либо двойной клик по main.py
