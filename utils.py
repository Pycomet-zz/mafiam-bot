from config import *

def get_string(text:str, lang:str) -> str:
    "Return The Test In LangugaE String"
    try:
        result = translator.translate(text, lang)
        return result
    except:
        return text