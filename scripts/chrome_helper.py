import subprocess
import platform
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent


def install_chrome():
    os_name = platform.system()

    if os_name not in ['Darwin', 'Linux']:
        raise ValueError(f"Unsupported operating system: {os_name}")

    if os_name == 'Darwin':
        try:
            print('Downloading chrome for MacOs. Please wait.')
            subprocess.run(["curl", "-o", "/tmp/chrome.zip", "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/"
                                          "117.0.5938.92/mac-arm64/chrome-mac-arm64.zip"])

            # TODO: only for mac users - after downloading chrome we should
            #  1. cd into f"{project_root}/binaries/chrome-mac-arm64
            #  2. sudo xattr -cr Google\ Chrome\ for\ Testing.app
            #  without this actions we can't start chrome

            subprocess.run(["unzip", "/tmp/chrome.zip", "-d", f"{project_root}/binaries"])

        except Exception:
            print("Can't download Chrome. ")
            sys.exit(1)

        finally:
            print('Deleting zip chrome folder')
            subprocess.run(["rm", "-rf", "/tmp/chrome.zip"])

    if os_name == "Linux":
        try:
            print('Downloading chrome for Linux. Please wait.')
            subprocess.run(["curl", "-o", "/tmp/chrome.zip", "https://edgedl.me.gvt1.com/edgedl/chrome/"
                                          "chrome-for-testing/117.0.5938.92/linux64/chrome-linux64.zip"])
            subprocess.run(["sudo", "unzip", "/tmp/chrome.zip", "-d", f"{project_root}/binaries"])
        except Exception:
            print("Can't download Chrome. ")
            sys.exit(1)

        finally:
            print('Deleting zip chrome folder')
            subprocess.run(["rm", "-rf", "/tmp/chrome.zip"])


install_chrome()
