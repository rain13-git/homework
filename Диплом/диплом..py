import requests
import os
from pprint import pprint


def find_photos():
    photos_dict = {}
    photos_list_for_dict = []
    inf_list = []
    token_vk = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
    URL =  "https://api.vk.com/method/photos.get"
    params = {
        'album_id':'profile',
        'photo_sizes': 1,
        "access_token": token_vk,
        "user_id": 552934290,
        'v':'5.131',
        'extended': 1
    }
    res = requests.get(URL, params=params).json()
    # pprint(res)

    for photo in res['response']['items']:
        listt = photo['sizes']
        photos_list = []
        photos_dict[f"{photo['likes']['count']}.txt"] = listt[-1]['url']
        inf_for_each = []
        inf_dict = {}
        inf_dict['file_name'] = f"{photo['likes']['count']}.txt"
        inf_dict['size'] = listt[-1]['type']
        inf_for_each.append(inf_dict)
        photos_list_for_dict.append(inf_for_each)
    with open('14.txt' ,'w') as file_14txt:
        file_14txt.write(f"{photos_list_for_dict[0]}")
    with open('7.txt', 'w') as file_7txt:
        file_7txt.write(f"{photos_list_for_dict[1]}")
    with open('4.txt', 'w') as file_4txt:
        file_4txt.write(f"{photos_list_for_dict[2]}")
    with open('5.txt', 'w') as file_5txt:
        file_5txt.write(f"{photos_list_for_dict[4]}")

    return photos_dict

class YaUploader():
    def __init__(self, token: str):
        self.token = token


    def _get_upload_link(self):
        list_for_keys = list()
        for keys in find_photos().keys():
            list_for_keys.append(keys)
            upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
            headers = {'Content-Type': 'application/json',
                       'Authorization': f'OAuth {self.token}'}
            params = {'path': keys, 'overwrite':'true'}
            response = requests.get(upload_url, headers=headers, params=params)

            if response.status_code == 200:
                href = response.json()['href']
                return href

            pprint(response.json()['href'])
            return ''
    def upload(self, file_path: str):
        self.href = self._get_upload_link()

        if self.href:
            response = requests.put(self.href, data=open(file_path, "rb"))
            response.raise_for_status()

            if response.status_code == 201:
                print("Success! ")

        else:
            print('нельзя загрузить')










if __name__ == "__main__" :
    find_photos()
    # id = input("Введите id пользователя VK: ")
    # token = input("Введите токен для Я.Диска: ")
    for keys in find_photos().keys():
        folder_path = os.getcwd()
        path_to_file = f"{folder_path}/{keys}"

        token = "AQAAAAAm01XcAADLW6GikyrnJkfiqQqS_F5dSgw"
        uploader = YaUploader(token)
        uploader._get_upload_link()
        result = uploader.upload(path_to_file)

