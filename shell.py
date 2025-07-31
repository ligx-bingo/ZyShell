import init
import cmd.helper

def shell_exec(input_text: str) -> int:
    command = shell_format(input_text)
    command = command.split()
    match (command[0]):
        case "help":
            statu = cmd.helper.run(command,init.language)
        case "exit":
            init.isRun = False
            statu = 0
        case _:
            statu = -1
    return statu


def shell_format(input_text: str) -> str:
    return input_text.format(workpath=init.workpath)


def shell_errorid(statu: int) -> str:
    match statu:
        case 0:
            return "NoError"
        case -1:
            return "CmdNotFound"
        case _:
            return "UnknownError"


def shell_checkerrorid(errid: str) -> bool:
    if errid in init.text:
        return True
    else:
        return False


def shell_errormessage(statu: int) -> str:
    errorid = shell_errorid(statu)
    if shell_checkerrorid(errorid):
        return init.text[errorid]
    else:
        return init.defaulttext[errorid]
