import shell
import init
while init.isRun:
    input_text = input(init.config["cmd-prefix"].format(workpath=init.workpath))
    errcode = shell.shell_exec(input_text)
    errmsg = shell.shell_errormessage(errcode).format(status=errcode, cmd0=input_text.split()[0])
    print(errmsg)
