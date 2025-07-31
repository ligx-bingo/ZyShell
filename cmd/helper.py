import os
def run(command: list,language: str) -> int:
    folderpath = "docs\\{}".format(language)
    if os.path.exists(folderpath):
        with open("{}\\index.txt".format(folderpath), "r", encoding="utf-8") as f:
            print(f.read())
    else:
        with open("docs\\Chinese\\index.txt", "r", encoding="utf-8") as f:
            print(f.read())
    return 0