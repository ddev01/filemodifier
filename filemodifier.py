from os import get_terminal_size
from pathlib import Path
from colorama import Fore


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


if __name__ == "__main__":
    try:
        display_banner()

        while True:
            path = input(f"Enter Path\n[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] ")
            mode = int(
                input(
                    f"Batch Rename or Change Extension [1 for Batch Rename, 0 for Change Extension]:\n[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] "
                ).strip()
            )
            path_to_scan = Path(path).absolute()

            if int(
                input(
                    f"Program will scan in {Fore.LIGHTMAGENTA_EX}{path_to_scan!s}{Fore.RESET}. Are you sure? [1 for yes, 0 for no]\n[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] "
                ).strip()
            ):
                break
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTRED_EX}\nProgram Closed by User")
