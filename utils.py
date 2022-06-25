from config import *

def get_string(text:string, lang:string) -> string:
    "Return The Test In LangugaE String"
    try:
        result = translator.translate(text, lang)
        return result
    except:
        return text