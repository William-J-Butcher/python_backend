"""Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию o содержимом в виде объектов namedtuple.
Каждый объект хранит:
- имя файла без расширения или название каталога,
- расширение, если это файл,
- флаг каталога, 
- название родительского каталога.
B процессе сбора сохраните данные в текстовый файл используя логирование. Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки c передачей параметров."""

import os
import logging
import argparse
from collections import namedtuple

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent_dir'])

def gather_info(directory):
    logging.info(f"Gathering information about directory: {directory}")
    info_list = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            name, extension = os.path.splitext(item)
            info_list.append(FileInfo(name, extension, False, os.path.basename(directory)))
        elif os.path.isdir(item_path):
            info_list.append(FileInfo(item, '', True, os.path.basename(directory)))
    return info_list

def save_to_file(info_list, file_path):
    logging.info(f"Saving information to file: {file_path}")
    with open(file_path, 'w') as f:
        for info in info_list:
            f.write(f"Name: {info.name}, Extension: {info.extension}, Is Dir: {info.is_dir}, Parent Dir: {info.parent_dir}\n")

def main():
    parser = argparse.ArgumentParser(description='Directory Information Gatherer')
    parser.add_argument('directory', help='Path to the directory')
    parser.add_argument('output_file', help='Path to the output file')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        info_list = gather_info(args.directory)
        save_to_file(info_list, args.output_file)
        logging.info("Information gathered and saved successfully")
    except Exception as e:
        logging.error(f"Error gathering information: {str(e)}")

if __name__ == '__main__':
    main()

# запустить этот скрипт можно из командной строки, передавая параметры, например:
# python directory_info_gatherer.py /path/to/directory /path/to/output/file.txt
# В этом примере собираем информацию о содержимом директории /path/to/directory и сохраняем ее в файл /path/to/output/file.txt. 
