import main


def shell_exec(input_text: str) -> int:
    command = shell_format(input_text)
    command = command.split()
    match (command[0]):
        case _:
            pass
    return 0


def shell_format(input_text: str) -> str:
    return input_text.format(workpath=main.workpath)
