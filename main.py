import zyshcfg
import shell

config = zyshcfg.getcfg()
version = config["version"]
language = config["language"]
text = zyshcfg.gettext(language)
defaulttext = zyshcfg.gettext("Chinese")
print(text["welcome"].format(version=version))
isRun = True
workpath = config["DefaultWorkPath"]
while isRun:
    input_text = input(config["cmd-prefix"].format(workpath=workpath))
    errcode = shell.shell_exec(input_text)
    errmsg = shell.shell_errormessage(errcode).format(status=errcode,cmd0=input_text.split()[0])
    print(errmsg)
