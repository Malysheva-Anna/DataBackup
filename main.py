# Сохранить json файл с информацией о размере файла картинки в json-файл


import requests


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



    def get_upload_link(self, file_name):
        url = f'{self.yd_base_url}/v1/disk/resources/upload'

        response = requests.get(
            url,
            headers=self.headers,
            params={'path': f'{self.folder_name}/{file_name}'}
        )

        return response.json()['href']

    def upload_file(self, image_data, upload_link):
        requests.put(
            upload_link,
            data=image_data
        )


def main():
    text = input("Введите текст для картинки: ")
    token = input("Введите ваш токен: ")

    file_name = f'{text}.jpg'
    cat_api = CatAPI()
    yd = YandexDisk(token)

    image = cat_api.get_cat_image(text)

    yd.create_folder()

    upload_link = yd.get_upload_link(file_name)

    yd.upload_file(image, upload_link)

main()