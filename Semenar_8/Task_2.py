# Напишите функцию,
# которая в бесконечном цикле запрашивает имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

# {
#     level: {
#         id: name,
#         ...
#     },
#     ...
# }

def uniq_id(data: dict, id: str) -> bool:
    for item in data.values():
        if id in item.keys():
            return False
    return True


def add_user(fname: str) -> None:
    fname += '.json'
    while True:
        id = input('id: ')
        name = input('name: ')
        level = input('level: ')

        try:
            with open(fname, 'r', encoding='UTF-8') as fr:
                new_dict: dict = json.load(fr)
        except FileNotFoundError:
            new_dict: dict = {str(i): {} for i in range(1, 8)}

        if uniq_id(new_dict, id):
            new_dict[level].update({id: name})
        else:
            print('не уникальный id')
            continue

        with open(fname, 'w', encoding='UTF-8') as fw:
            json.dump(new_dict, fw, indent=2)


if __name__ == '__main__':
    add_user(fname='users')