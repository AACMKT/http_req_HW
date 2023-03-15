import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        request = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=request)
        link_info = response.json()

        """Метод загружает файлы по списку file_list на яндекс диск"""

        href = link_info.get("href")
        upload = requests.put(href, data=open(file_path, 'rb'))
        upload.raise_for_status()
        if upload.status_code == 201:
            print("File is successfully uploaded to Yandex_Disc")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'TestFileYD.txt'
    token = ''
    uploader = YaUploader(token)
    uploader.upload(path_to_file)
