import platform
import sys

def detect_os():
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()

    print(f"Operating System: {os_name}")
    print(f"OS Version: {os_version}")
    print(f"OS Release: {os_release}")

    # Additional information (optional)
    print(f"Platform: {sys.platform}")
    print(f"Architecture: {' '.join(platform.architecture())}")

detect_os()
