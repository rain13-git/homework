import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        params = {"path": "file.txt", "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)

        if response.status_code == 200:
            href = response.json()['href']
            return href

        print(response.json()['message'])
        return ''

    def upload(self, file_path: str):

        href = self._get_upload_link()
        print(href)
        if href:
            response = requests.put(href, data=open(file_path, "rb"))
            response.raise_for_status()

            if response.status_code == 201:
                print("Success! ")

        else:
            print('нельзя загрузить')


if __name__ == '__main__':
    token = "AQAAAAAm01XcAADLW6GikyrnJkfiqQqS_F5dSgw"
    folder_path = os.getcwd()
    path_to_file = f"{folder_path}/file.txt"
    uploader = YaUploader(token)
    print(uploader.upload(path_to_file))
    # result = uploader.upload(path_to_file)