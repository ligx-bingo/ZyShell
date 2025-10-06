import zyshcfg
import os
import socket
hostname = socket.gethostname()
username = os.getlogin()
config = zyshcfg.getcfg()
version = config["version"]
language = config["language"]
text = zyshcfg.gettext(language)
defaulttext = zyshcfg.gettext("Chinese")
workpath = config["DefaultWorkPath"]
print(text["welcome"].format(version=version))
isRun = True