# /cat/:tag/says/:text	Will return a random cat with a :tag and saying :text
# https://cataas.com/cat/cute/says/hello

# Название папки должно совпадать с названием вашей группы в Нетологии
# Текст картинки также должен являться названием файла на Яндекс.Диске
# Сохранить json файл с информацией о размере файла картинки в json-файл

# Входные данные:
# Пользователь вводит:
# Текст для картинки
# Токен с Полигона Яндекс.Диска. Важно: Токен публиковать в github не нужно!

# Выходные данные:
# json-файл с информацией по загруженным файлам
# Измененный Я.диск, куда добавились фотографии




import requests

class YandexDisk:             #Работает с API Яндекс-диска
    def __init__(self, token):
        pass

    def create_folder(self, folder_name):
        pass

    def get_upload_link(self, disk_path):
        pass

    def upload_file(self, local_path, disk_path):
        pass

    def file_exists(self, disk_path):
        pass


class CatAPI:    #Работает с API сайта с котами
    def get_cat_image(self, text):
        pass

    def save_image(self, image_data, filename):
        pass


def main():
    cat_api = CatAPI()
    yd = YandexDisk(token)

    image = cat_api.get_cat_image(text)
    cat_api.save_image(image, filename)

    yd.create_folder(folder_name)
    yd.upload_file(filename, disk_path)

main()