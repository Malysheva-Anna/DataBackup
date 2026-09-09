import requests
import json


class CatAPI:
    cat_base_url = 'https://cataas.com'

    def get_cat_image(self, text):
        url = f'{self.cat_base_url}/cat/says/{text}'
        response = requests.get(url)

        return response.content


class YandexDisk:
    yd_base_url = 'https://cloud-api.yandex.net'
    folder_name = 'FPYARZ-TRF-158'

    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}

    def create_folder(self):
        url = f'{self.yd_base_url}/v1/disk/resources'

        requests.put(
            url,
            headers=self.headers,
            params={'path': self.folder_name}
        )

    def file_exists(self, file_name):
        url = f'{self.yd_base_url}/v1/disk/resources'

        response = requests.get(
            url,
            headers=self.headers,
            params={'path': f'{self.folder_name}/{file_name}'}
        )

        return response.status_code == 200

    def get_upload_link(self, file_name):
        url = f'{self.yd_base_url}/v1/disk/resources/upload'

        response = requests.get(
            url,
            headers=self.headers,
            params={'path': f'{self.folder_name}/{file_name}'}
        )

        return response.json()['href']

    def upload_file(self, file_data, upload_link):
        requests.put(
            upload_link,
            data=file_data
        )

    def get_download_link(self, file_name):
        url = f'{self.yd_base_url}/v1/disk/resources/download'

        response = requests.get(
            url,
            headers=self.headers,
            params={'path': f'{self.folder_name}/{file_name}'}
        )

        return response.json()['href']

    def download_file(self, file_name):
        download_link = self.get_download_link(file_name)

        response = requests.get(download_link)

        return response.content


class JsonData:
    def __init__(self):
        self.data = {}

    def add_file(self, file_name, file_size):
        self.data[file_name] = file_size

    def load(self, json_data):
        self.data = json.loads(json_data)

    def to_json(self):
        return json.dumps(self.data)


def main():
    text = input("Введите текст для картинки: ")
    token = input("Введите ваш токен: ")

    file_name = f'{text}.jpg'

    cat_api = CatAPI()
    yd = YandexDisk(token)
    json_data = JsonData()

    image = cat_api.get_cat_image(text)

    yd.create_folder()

    upload_link = yd.get_upload_link(file_name)
    yd.upload_file(image, upload_link)

    file_size = len(image)

    if yd.file_exists('info.json'):
        existing_json = yd.download_file('info.json')
        json_data.load(existing_json)

    json_data.add_file(file_name, file_size)

    json_upload_link = yd.get_upload_link('info.json')
    yd.upload_file(json_data.to_json(), json_upload_link)


main()