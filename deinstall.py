from getpass import getuser
import os

os.remove("$POST_WIN32.pyw")
os.remove("winlock.pyw")

os.chdir(f"C:/Users/{getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/")
os.remove("SystemPlugins.bat")
