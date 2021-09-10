from os import chdir, path, sep, get_terminal_size, rename
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


# def reconstruct_file(file:tuple[str, str]) -> str:
#     return

# I used to make a project similar to this, and I also
# wrote a func similar to this
def dissect_file(file: str) -> tuple[str, str]:
    # breakpoint()
    file = file.split(sep)[-1]
    filename, _, extension = file.partition(".")
    exists = False
    if extension == "":
        extension = "File"
    if path.exists(file):
        exists = True

    return filename, extension, exists


if __name__ == "__main__":
    display_banner()

    while True:
        searchDirectory = path.abspath(
            input("Enter a directory to batch-rename:\n")
        ).replace(sep, "/")

        if path.isdir(searchDirectory):
            chdir(searchDirectory)
            break

    renameExtensions = f"Rename a certain filetype? (leave to rename every file in {searchDirectory!r})\n"

    renameTo = input("Enter Output name (index will be added)")

    for file in iglob("**", recursive=True):
        file = dissect_file(file)
        if file[2] and file[1] == renameExtensions:
            # [ ] Get Zero Offset
            rename(".".join(file[0:1]), "dummy")
