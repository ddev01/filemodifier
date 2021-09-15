# Table of Contents
- [Table of Contents](#table-of-contents)
- [File Modifier](#file-modifier)
- [How to Use](#how-to-use)
  - [For Windows 10 Users](#for-windows-10-users)
  - [For Unix (MacOS, Linux) & Windows 7 Users](#for-unix-macos-linux--windows-7-users)
    - [Option One: VM's](#option-one-vms)
    - [Option Two: Download Python](#option-two-download-python)
- [Changelog](#changelog)
- [To Do](#to-do)
- [Contribute](#contribute)

# File Modifier
This script can change all file extensions from files in a directory. Run the script and drag any file onto the script window and press enter or manually enter a path.

Examples:
- "C:\Users\Admin\Desktop\New folder\jeg.png"
- C:\Users\Admin\Desktop\New folder\jeg.png
- C:\Users\Admin\Desktop\New folder\

<sub>*(yes, forward and backward slashes work, even on Windows)*</sub>

If you want to rename the files enter a name. The script will name the files with numbers like `name1.txt`, `name2.txt` and so on. If you don't want to rename the files just leave this empty and press enter.

Enter any file extension you wish the apply to all the files in this directory Example: txt, png, jpeg, py and so on.
# How to Use
## For Windows 10 Users
- Download the program from the [releases tab](https://github.com/ddev01/filemodifier/releases)
- Run the program
## For Unix (MacOS, Linux) & Windows 7 Users
### Option One: VM's
- Download [VirtualBox](https://www.virtualbox.org/)
- Get a Windows 10 ISO
- Follow the setup
- Follow the [guide for Windows 10 users](#for-windows-10-users)
### Option Two: Download Python
**This Option is for Unix Users Only. Python 3 is not supported on Windows 7**
- Download [Python](https://www.python.org/downloads/) *(Python 3.9x probably works best)*
- Follow the [contribution guide](#contribute), minus the last two steps


# Changelog
- [x] Added Support for Unix
- [x] Added Color for the terminals that support them
- [x] Added an ASCII Banner that only shows if the terminal is big enough
- [x] Added Driver Code (`if __name__ == '__main__'` kind of stuff for Python)
- [x] Improved `input()`s

# To Do
- [ ] Filters (hopefully even regex filters)
- [ ] Executables for Linux and MacOS (Aside from the python script itself, I'd like a way to make a linux executable, like Node.JS' `pkg` package, which builds a Windows, Mac, and Linux executable)
# Contribute
Looking to contribute? Here are the steps:
- Make a fork
- Run the following command:
    ```
    pip install -r requirements.txt
    ```
- `pip` should download the repo's requirements (pathlib and colorama)
- Edit the files
- Make a commit in your fork
- Open a pull request. [ddev](https://github.com/ddev01) should be able to see your changes and choose to merge or not
