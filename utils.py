from config import *
from models import Account

def get_string(text:str, lang:str) -> str:
    "Return The Test In LangugaE String"
    try:
        result = translator(text, lang)
        return result
    except:
        return text



def generate_unique_code():
    "Write An Algorithm To Generate A 6 Digit Code"
    pass




class DbClient():

    def get_collection(self, name:str):
        "Returns The Collections Document (Query by - name)"
        res = client['mafiambot_db'][name]
        return res

    def get_account(self, user_id):
        "Get Account Object"
        result = collection.find_one({ 'userId' : user_id }) #Checker
        if result == None:
            return None 

        #Get Obj
        res = Account.from_json(result)
        import pdb; pdb.set_trace()
        return res

    
    def save_account(self, account: Account):
        "Saves Account Object To MongoDb"

        collection = self.get_collection("accounts")

        #Write To Collection
        result = collection.find_one({ 'userId' : account.user_id }) #Checker
        data = account.to_dict()

        if result == None:
            collection.insert_one(data)
            return True

        return False


    def update_account(self, user_id:int, data:object) -> bool:
        "Update A Certain Account"

        user = get_account(user_id)
        
        if user == None:
            return False

        collection.update_one({
            'userId' : user_id
        }, {
            "$set": data
        })
        return True



db_client = DbClient()