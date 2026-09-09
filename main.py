# Текст картинки также должен являться названием файла на Яндекс.Диске
# Сохранить json файл с информацией о размере файла картинки в json-файл

# Выходные данные:
# json-файл с информацией по загруженным файлам
# Измененный Я.диск, куда добавились фотографии




import requests


class CatAPI:
    cat_base_url = 'https://cataas.com'

    def get_cat_image(self, text):
        url = f'{self.cat_base_url}/cat/says/{text}'
        response = requests.get(url)
        return response.content


class YandexDisk:
    yd_base_url = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}       #заготовили заголовок для запросов

    def create_folder(self, folder_name):
        url = f'{self.yd_base_url}/v1/disk/resources'

        requests.put(
            url,
            headers=self.headers,
            params={'path': folder_name}
        )


#
#     def get_upload_link(self, disk_path):
#         pass
#
#     def upload_file(self, local_path, disk_path):
#         pass



def main():
    text = input("Введите текст для картинки: ")
    token = input("Введите ваш токен: ")

    cat_api = CatAPI()
    yd = YandexDisk(token)

    # image = cat_api.get_cat_image(text)
    # cat_api.save_image(image, filename)

    yd.create_folder('FPYARZ-TRF-158')
    # yd.upload_file(filename, disk_path)

main()