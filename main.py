import shell
import init
while init.isRun:
    try:
        input_text = input(init.config["cmd-prefix"].format(workpath=init.workpath,username=init.username,hostname=init.hostname,root=init.root))
    except KeyboardInterrupt:
        print()
        exit(0)
    errcode = shell.shell_exec(input_text)
    errmsg = shell.shell_errormessage(errcode).format(status=errcode, cmd0=input_text.split()[0] if len(input_text) > 0 else "")
    print(errmsg)
