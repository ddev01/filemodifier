from os import get_terminal_size
from pathlib import Path
from colorama import Fore

DISPLAY_MESSAGE = "Made by ddev01 | Banner by Kiwifruit"


class WorkInProgress(NotImplemented):
    def __init__(self) -> None:
        super().__init__()


def display_banner():
    # 'Smart' banner display. Basically just hides the banner
    # if the termina window is too small for the banner to look good
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
        banner += DISPLAY_MESSAGE.replace(
            " | Banner by Kiwifruit", " | Banner (hidden) by Kiwifruit"
        )
    else:
        banner += DISPLAY_MESSAGE.center(maxBannerLen, " ")

    print(banner)


def str_can_be_int(obj: str):
    # Function to tell me if the string can be
    # converted into an int without problems
    try:
        # I think you can remove the assignment,
        # but its gonna stay there for now just
        # to make sure that it works
        obj = int(obj)
        return True
    except ValueError:
        return False


def scan_dir_verify(path_to_scan: str):
    prompt = input(
        f"Program will scan in {Fore.LIGHTMAGENTA_EX}{path_to_scan!s}{Fore.RESET}. Are you sure? [1 for yes, 0 for no]\n[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] "
    )
    output = str_can_be_int(prompt)

    if not output:
        return False

    if int(prompt):
        return True


def prompt(question: str):
    # Wrapper func for 'input'. Too tiring to make multiple 'input',
    # formatting it, then stripping it so i did this
    return input(f"{question}:[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] ").strip()


def get_path_and_mode():
    while True:
        path = prompt("Enter Path ")
        mode = prompt(
            "Batch Rename or Change Extension [1 for Batch Rename, 0 for Change Extension]:"
        )

        if str_can_be_int(mode) and scan_dir_verify(path):
            # Basically just returns (path, mode)
            return path, mode


def batch_rename_prompt():
    # Teehee its still work in progress. I dunno how to implement this yet
    raise WorkInProgress
    # print('Work in Progress')


def change_extension_prompt():
    extension = prompt("Enter Extension to rename to:")

    if "." in extension:
        # From the last period above. This should do something like
        # file.tar.gz -> gz
        extension = extension[extension.count(".") + 1 :]

    return extension


def list_files_in_dir(dir, pattern, recursive: bool = False):
    print(
        f"Listing files on {dir!r}. This could take a while if {dir!r} is a big directory"
    )
    return (
        [file for file in Path(dir).glob(pattern)]
        if not recursive
        else [file for file in Path(dir).rglob(pattern)]
    )


def main():
    # Main function. Calls like 80% of the functions
    # and more or less handles the big logic.
    # I'm trying to make sure that sourcery gives this function's
    # quality score stay above 80% - 90%
    try:
        display_banner()
        path, mode = get_path_and_mode()

        if mode:
            # TODO: Maybe add a way for this program to use
            #       glob patterns. Such Patterns can be
            #       tested at https://globster.xyz/
            output = batch_rename_prompt()
        else:
            extension = change_extension_prompt()
    except KeyboardInterrupt:
        print(f"{Fore.LIGHTRED_EX}\nProgram Closed by User")
    except WorkInProgress:
        print(f"{Fore.LIGHTRED_EX}\nFeature is Work In Progress")


if __name__ == "__main__":
    main()
