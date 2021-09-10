import requests
from pprint import pprint
from time import sleep
from tqdm import tqdm
import json


def find_photos(vk_id):
    photos_dict = {}
    token_vk = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
    URL = "https://api.vk.com/method/photos.get"
    params = {
        'album_id': 'profile',
        'photo_sizes': 1,
        "access_token": token_vk,
        "user_id": vk_id,
        'v': '5.131',
        'extended': 1
    }
    res = requests.get(URL, params=params).json()
    for photo in res['response']['items']:

        sizes_list = photo['sizes']
        photos_dict[f"{photo['likes']['count']}.jpg"] = [sizes_list[-1]['url'], sizes_list[-1]['type']]
    return photos_dict


class YaUploader():
    def __init__(self, token: str):
        self.token = token

    def add_folder(self, vk_id):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': vk_id,
            'overwrite': 'true'
        }
        response = requests.put(upload_url, params=params, headers=headers)

        return vk_id

    def _get_upload_link_and_upload(self, name, link,folder):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

        params = {
            'path': f"{YaUploader.add_folder(self,folder)}/{name}",
            'url': link,
            'overwrite': 'true'
        }
        response = requests.post(
            upload_url,
            params=params,
            headers=headers

        )

        print(response.status_code)

        if response.status_code == 202:
            print("Success! ")

        else:
            print('нельзя загрузить')


def transform_to_json(photos_dict):
    # d = {'photos': [{1й словарь}, {2й словарь}, ]}

    d = {'photos': []}
    for key, value in photos_dict.items():
        inf_dict = {'filename': key, 'size': value[1]}
        d['photos'].append(inf_dict)
    with open("output.json", 'w') as file:
        json.dump(d, file)


if __name__ == "__main__":
    if True:
        vk_id = input("Введите id Вконтакте: ")
        token_vk = "958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008"
        URL = "https://api.vk.com/method/users.get"
        params = {
            "access_token": token_vk,
            "user_id": vk_id
        }
        response = requests.get(URL, params=params)
        if response.status_code != 200:
            print('Проверьте Vk id: ')
    # 552934290
    # token = input("Введите токен для Я.Диска: ")
        else:
            photos = find_photos(vk_id)
            token = ""
            uploader = YaUploader(token)
            transform_to_json(photos)
            for key, value in tqdm(photos.items()):
                uploader.add_folder(vk_id)
                uploader._get_upload_link_and_upload(key, value[0],vk_id)
                sleep(1)
