"""Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
Добавьте возможность запуска из командной строки. При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц. Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые, т.е не мая, а 5."""


import logging
import argparse
import datetime
import re

MONTHS = {
    '1': 'января', '2': 'февраля', '3': 'марта', '4': 'апреля', '5': 'мая', '6': 'июня',
    '7': 'июля', '8': 'августа', '9': 'сентября', '10': 'октября', '11': 'ноября', '12': 'декабря',
    'января': '1', 'февраля': '2', 'марта': '3', 'апреля': '4', 'мая': '5', 'июня': '6',
    'июля': '7', 'августа': '8', 'сентября': '9', 'октября': '10', 'ноября': '11', 'декабря': '12'
}

WEEKDAYS = {
    '1': 'понедельник', '2': 'вторник', '3': 'среда', '4': 'четверг', '5': 'пятница', '6': 'суббота', '7': 'воскресенье',
    'понедельник': '1', 'вторник': '2', 'среда': '3', 'четверг': '4', 'пятница': '5', 'суббота': '6', 'воскресенье': '7'
}

def parse_text(text):
    pattern = r'(\d+)-й\s+(\w+)\s+(\w+)'
    match = re.match(pattern, text)
    if match:
        day_num, weekday, month = match.groups()
        month_num = MONTHS[month]
        weekday_num = WEEKDAYS[weekday]
        return int(day_num), int(weekday_num), int(month_num)
    else:
        logging.error(f"Invalid input format: {text}")
        raise ValueError("Invalid input format")

def get_date(day_num, weekday_num, month_num):
    current_year = datetime.date.today().year
    for day in range(1, 32):
        try:
            date = datetime.date(current_year, month_num, day)
            if date.weekday() + 1 == int(weekday_num):
                return date
        except ValueError:
            pass
    logging.error(f"No date found for day {day_num} of week {weekday_num} in month {month_num}")
    raise ValueError("No date found")

def main():
    parser = argparse.ArgumentParser(description='Date Parser')
    parser.add_argument('text', nargs='?', default='', help='Input text')
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        day_num, weekday_num, month_num = parse_text(args.text)
        date = get_date(day_num, weekday_num, month_num)
        logging.info(f"Date: {date}")
        print(date)
    except Exception as e:
        logging.error(f"Error parsing text: {str(e)}")

if __name__ == '__main__':
    main()

# Вы можете запустить этот скрипт из командной строки, передавая параметры, например:
# python date_parser.py "1-й четверг ноября"

# В этом примере мы преобразуем текст "1-й четверг ноября" в дату в текущем году.