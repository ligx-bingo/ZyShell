import json
def getcfg() -> dict:
    with open('config.json', 'r', encoding='utf-8') as f:
        cfg = json.load(f)
    return cfg

def gettext(lang : str) -> dict:
    with open('lang\\{}.json'.format(lang), 'r', encoding='utf-8') as f:
        text = json.load(f)
    return text