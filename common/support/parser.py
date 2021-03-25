# -*- coding: utf-8 -*-

from optparse import OptionParser
from common.settings import version

main_text = "Развлекательная программа по вселенной Slay the Spire"

parser = OptionParser(usage=main_text, version="Версия комплекса: " + version )

parser.add_option(
    "-b", 
    "--run_backend", 
    action="store_true", 
    dest="run_backend", 
    help="Запуск сервера backend", 
    default=False
)

parser.add_option(
    "-f", 
    "--run_frontend", 
    action="store_true", 
    dest="run_frontend", 
    help="Запуск сервера frontend", 
    default=False
)

parser.add_option(
    "-c", 
    "--create_tables", 
    action="store_true", 
    dest="create_tables", 
    help="Создание таблиц по работе с данными", 
    default=False
)

parser.add_option(
    "-d", 
    "--drop_tables", 
    action="store_true", 
    dest="drop_tables", 
    help="Удаление таблиц по работе с данными", 
    default=False
)

parser.add_option(
    "-e", 
    "--upload_data", 
    action="store_true", 
    dest="create_data", 
    help="Загрузка полезной информации в базу данных", 
    default=False
)