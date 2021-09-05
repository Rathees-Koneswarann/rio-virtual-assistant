import os

os.system('reg add "HKEY_CURRENT_USER/Control Panel/Desktop" /v Wallpaper /t REG_SZ /d  C:/Users/user/Downloads/wp2871529-best-wallpapers-for-hacker.jpg /f')
os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")