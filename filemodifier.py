from os import path, sep, get_terminal_size
from glob import iglob  # 'iglob' is better for when your working with huge directories
from tqdm import (
    tqdm,
)  # 'tqdm' is just a progress bar module. run `pip install tqdm` first
from colorama import Fore  # colorama is just for pretty terminal output


def display_banner():
    dispMessage = "Made by ddev01 | Banner by Kiwifruit"
    banner = """██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ███████╗██╗██╗     ███████╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ██╔════╝██║██║     ██╔════╝
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    █████╗  ██║██║     █████╗
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██╔══╝  ██║██║     ██╔══╝
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ██║     ██║███████╗███████╗
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝╚══════╝╚══════╝

██████╗ ███████╗███╗   ██╗ █████╗ ███╗   ███╗███████╗██████╗
██╔══██╗██╔════╝████╗  ██║██╔══██╗████╗ ████║██╔════╝██╔══██╗
██████╔╝█████╗  ██╔██╗ ██║███████║██╔████╔██║█████╗  ██████╔╝
██╔══██╗██╔══╝  ██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗
██║  ██║███████╗██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

"""

    if (maxBannerLen := len(max(banner))) > get_terminal_size().columns:
        banner = "Python File Renamer\nMake the terminal bigger to see the ascii art.\n"
        banner += dispMessage.replace(
            " | Banner by Kiwifruit", " | Banner (hidden) by Kiwifruit"
        )
    else:
        banner += dispMessage.center(maxBannerLen, " ")

    print(banner)


# I used to make a project similar to this, and I also
# wrote a func similar to this
def dissect_file(file: str) -> tuple[str, str]:
    file = file.split(sep)[-1]
    filename, _, extension = file.partition(".")


dissect_file("HelloWorld")
