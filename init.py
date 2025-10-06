import zyshcfg
import os
import socket
config = zyshcfg.getcfg()
if os.getuid() == 0:
    idchar = config["RootCharacter"]
else:
    idchar = config["UserCharacter"]
hostname = socket.gethostname()
username = os.getlogin()
version = config["version"]
language = config["language"]
text = zyshcfg.gettext(language)
defaulttext = zyshcfg.gettext("Chinese")
workpath = config["DefaultWorkPath"]
print(text["welcome"].format(version=version))
isRun = True