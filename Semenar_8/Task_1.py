# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию,
# которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
import json


def txt_to_json(input_filename: str,
                output_filename: str):

    with open(input_filename, 'r') as f:
        data = f.read().split('\n')[:-1]
    data = [{i.split()[0].capitalize():
             float(i.split()[1])} for i in data]

    with open(output_filename, 'w') as res:
        json.dump(data, res, indent=4)


if __name__ == '__main__':
    txt_to_json('result.txt', 'output.json')

