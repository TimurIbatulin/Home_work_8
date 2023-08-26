# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий

import json
import os

def direct_stat(direct_user: str):
    information_dir = os.walk(direct_user)
    file_json = {}
    print(type(file_json))
    count = 1
    for root, dirs, files in os.walk(direct_user):
        way_to = root
        *_, parent_folder = way_to.split('/')
        file_json.update({parent_folder:{}})
        if dirs != None:
            file_json[parent_folder].update({'folder':{}})
        number_in_folder = 1
        for dir in dirs:
            file_json [parent_folder]['folder'].update({f'{number_in_folder} name':dir})
            size = 0
            for ro, di, fi in os.walk(way_to):
                for f in fi:
                    size_way = os.stat(os.path.join(ro, f))
                    size += size_way.st_size
            file_json [parent_folder]['folder'].update({f'{number_in_folder} size': size})
            number_in_folder += 1
        if files != None:
            file_json[parent_folder].update({'file':{}})
        for fil in files:
            file_json [parent_folder]['file'].update({f'{number_in_folder} name': fil})
            file_size = os.stat(os.path.join(way_to, fil))
            file_json [parent_folder]['file'].update({f'{number_in_folder} size': file_size.st_size})
            number_in_folder += 1
    with open('JSON.json', 'w', encoding='utf-8') as f:
        json.dump(file_json, f, indent=4, ensure_ascii=False)
    print(file_json)


if __name__ == '__main__':
    direct_stat('/Users/timuribatulin/Downloads')

