
import requests
from pprint import pprint
import os
current = os.getcwd()
folder = 'HTTP_requests'
file_name = 'Test2.txt'

class Yandex:
    host = 'https://cloud-api.yandex.net/'
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        uri = 'v1/disk/resources/files'
        url = self.host + uri
        headers = self.get_headers()
        params = {'limit': 2, 'media_type': 'image'}
        response = requests.get(url, headers=headers, params=params)
        pprint(response.json())
        pprint(response.status_code)
    
    def create_folder(self):
        uri = 'v1/disk/resources/'
        url = self.host + uri
        params = {'path': '/test_folder/'}
        response = requests.put(url, headers=self.get_headers(), params=params)
        pprint(response.json())
        pprint(response.status_code)

    def get_upload_link(self, disk_file_name):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/test_folder/{disk_file_name}'}
        response = requests.get(url, headers=self.get_headers(), params=params)
        return response.json()['href']
        

    def upload_from_pc(self, local_file_name, disk_file_name):
        upload_link = self.get_upload_link(disk_file_name)
        response = requests.put(upload_link, headers=self.get_headers(), data=open(local_file_name, 'rb'))
        print(response.status_code)
        if response.status_code == 201:
            print("Success")

    def upload_from_internet(self, file_url, file_name):
        uri = 'v1/disk/resources/upload/'
        url = self.host + uri
        params = {'path': f'/test_folder/{file_name}', 'url': file_url}
        response = requests.post(url, headers=self.get_headers(), params=params)
        print(response.status_code)
        if response.status_code == 202:
            print("Success")

if __name__ == '__main__':
    TOKEN = ''
    ya = Yandex(TOKEN)
    full_path = os.path.join(current, folder, file_name)
    # file_url = "https://proprikol.ru/wp-content/uploads/2020/12/kartinki-rik-i-morti-27.jpg"
    # ya.get_files_list()
    # ya.create_folder()
    # ya.get_upload_link('first_test.txt')
    # ya.upload_from_internet(file_url, 'Rick.jpg')
    ya.upload_from_pc("Test2.txt", "Test2.txt")



