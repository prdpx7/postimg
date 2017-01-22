import requests
import base64
import os
import json
import sys
class Imgur(object):
    '''
    Anonymous image upload on imgur.com with cliend_id
    '''
    def __init__(self,img_path):
        self.img_path = os.path.expanduser(img_path)
        try:
            with open(self.img_path,'rb') as img:
                self.img_b64 = base64.b64encode(img.read())
        except Exception as file_exception:
            print file_exception
            sys.exit(1)
        #if client_id exist in env else use default
        self.client_id = os.environ.data['IMGUR_CLIENT_ID'] or '2b8986ab0193370'

    def upload(self):
        headers = {'Authorization':'Client-ID '+ self.client_id}
        data = {'image':self.img_b64}
        url = 'https://api.imgur.com/3/image'
        return json.loads(requests.post(url,headers=headers,data=data).text)


