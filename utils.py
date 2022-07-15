import os
from platform import platform


def clear_terminal() -> None:
    """
    clear terminal window

    return : `None`
    """

    user_platform = platform().lower()
    if "linux" in user_platform or "mac" in user_platform:
        os.system('clear')
    else:
        os.system('cls')
