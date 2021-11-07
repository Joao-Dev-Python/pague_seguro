import json,requests
from constants import permissions
from constants import urls
from constants import body
from DB import db




class PixModel:
    def __init__(self):
        #Auth para pegar token de acesso
        self.d = db.DB()
        self.ACESS_TOKEN = self.auth(body.cob_data).get("access_token")
    def auth(self,data):
        r = requests.post(url=urls.auth_url,
                          data = json.dumps(data) ,
                          headers = {'content-type': 'application/json',
                                    'Authorization':  permissions.BASIC_CREDENTIAL},
                                    cert=permissions.CERTIFICATES)
        return json.loads(r.text)
       
    def check_cob(self,txid):
      
      r = requests.get(urls.check_cob_url+txid,
      headers={'content-type': 'application/json',
                                    'Authorization': f"Bearer {self.ACESS_TOKEN}"},
                                    cert= permissions.CERTIFICATES)
      response = json.loads(r.text)
      if(r.status_code == 200 or r.status_code == 201):
         self.d.update(id= response.get("devedor").get("nome"),field=response)
         pass
          
          
      return response

      
    
    
           








   
        

