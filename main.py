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


class CatAPI:
    cat_base_url = "https://cataas.com/"

    def get_cat_image(self, text):
        url = f'{self.cat_base_url}/cat/says/{text}'
        response = requests.get(url)
        return response


# class YandexDisk:
#     def __init__(self, token):
#         pass
#
#     def create_folder(self, folder_name):
#         pass
#
#     def get_upload_link(self, disk_path):
#         pass
#
#     def upload_file(self, local_path, disk_path):
#         pass



def main():
    text = input("Введите текст для картинки: ")

    # cat_api = CatAPI()            #создали объект класса
    # yd = YandexDisk(token)        #создали объект класса
    #
    # image = cat_api.get_cat_image(text)
    # cat_api.save_image(image, filename)
    #
    # yd.create_folder(folder_name)
    # yd.upload_file(filename, disk_path)

main()