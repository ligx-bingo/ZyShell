import zyshcfg
import shell

config = zyshcfg.getcfg()
version = config["version"]
language = config["language"]
text = zyshcfg.gettext(language)
print(text["welcome"].format(version=version))
isRun = True
workpath = config["DefaultWorkPath"]
while isRun:
    input_text = input(config["cmd-prefix"].format(workpath=workpath))
    shell.shell_exec(input_text)
