from pprint import pprint
import json
import requests
import sys
import os


class YandexDisk:

    def __init__(self, token):
        self.token = token
    
    
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()
    
    
    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")




    


if __name__ == '__main__':

  
    # Задача 2

    TOKEN = ""
    print(os.getcwd())
    path = 'temp/test.txt'
    ya = YandexDisk(token=TOKEN)
    print("Текущая деректория:", os.getcwd())
    path_to_file = os.path.join(os.getcwd(),'test.txt')
    

    ya.upload_file_to_disk(path_to_file,'test.txt')











    
    


