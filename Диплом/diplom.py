import requests
from pprint import pprint
from time import sleep
from tqdm import tqdm
import json

class Vkphotos():

    def find_photos(self, vk_id, count,  token_vk="" ):
        photos_dict = {}

        if type(vk_id) is int:
            URL = "https://api.vk.com/method/photos.get"
            params = {
                'album_id': 'profile',
                'photo_sizes': 1,
                "access_token": token_vk,
                "user_id": vk_id,
                'v': '5.131',
                'extended': 1,
                'count': count
            }
            res = requests.get(URL, params=params).json()
            for photo in res['response']['items']:
                sizes_list = photo['sizes']
                photos_dict[f"{photo['likes']['count']}_{photo['date']}.jpg"] = [sizes_list[-1]['url'], sizes_list[-1]['type']]
            print("search has ended")
        else:
            id_from_numbers = None
            URL = "https://api.vk.com/method/users.get"
            params = {
                'user_ids': vk_id,
                'v':'5.131',
                "access_token": token_vk
            }
            response = requests.get(URL, params=params).json()
            # print(response)
            try:
                if response['response']:
                    for vk_id_for_photo in response['response']:
                        id_from_numbers = vk_id_for_photo['id']
                        print("id has received")
            except KeyError:
                print("Проверьте vk id")
            URL = "https://api.vk.com/method/photos.get"
            params = {
                'album_id': 'profile',
                'photo_sizes': 1,
                "access_token": token_vk,
                "user_id": id_from_numbers,
                'v': '5.131',
                'extended': 1,
                'count': count
            }
            res = requests.get(URL, params=params).json()
            for photo in res['response']['items']:
                sizes_list = photo['sizes']
                photos_dict[f"{photo['likes']['count']}_{photo['date']}.jpg"] = [sizes_list[-1]['url'], sizes_list[-1]['type']]
            print("search has ended")

        return photos_dict


class YaUploader():
    def __init__(self,token: str):
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

    def _upload(self, name, link,folder):
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

# я хотел вызвать фунцкию и передать ей "info", т.к "info" содержит как token_vk так token_Ya
# def function_call(token_vk, token_Ya):
#     pass

if __name__ == "__main__":
    # begemot_korovin
    # по этому фрагменту хотел достать содержимое файла и его использовать
    # with open('tokens.txt', "r") as file:
    #     info = file.read()
    # print(S)
    # function_call(S)

    token_Ya = ""

    if True:
        vk_id = input('Введите vk id: ')
        count = int(input("Введите кол-во записей для загрузки: "))
        photos = Vkphotos().find_photos(vk_id, count)
        Vkphotos().find_photos(vk_id, count)
        uploader = YaUploader(token_Ya)
        transform_to_json(photos)
        for key, value in tqdm(photos.items()):
            uploader.add_folder(vk_id)
            uploader._upload(key, value[0],vk_id)
            sleep(1)
