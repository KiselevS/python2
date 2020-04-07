#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import docs
from decimal import Decimal
import pickle

class Application(object):

    def __init__(self):
        self.__current_document = None
        self.__no_doc = {
            '1': ( 'Создать накладную', self.create_nakl ),
            'V': ( 'Создать счет-фактуру', self.create_invoice ), 
            '7': ( 'Загрузить из файла', self.load_doc ),
        }
        self.__with_nakladnaya = {
            '2': ( 'Добавить позицию', self.add_pos_to_nakl ),
            '3': ( 'Показать', self.current_doc_show ),
            '4': ( 'Сменить номер документа', self.change_number ),
            '5': ( 'Cохранить в файл', self.save_current_doc ),
            '6': ( 'Уничтожить документ', self.kill_current_doc ),
            'A': ( 'Добавить адрес доставки', self.set_address ),
        }
        self.__with_invoice = {            
            '3': ( 'Показать', self.current_doc_show ),
            '4': ( 'Сменить номер документа', self.change_number ),
            '5': ( 'Cохранить в файл', self.save_current_doc ),
            '6': ( 'Уничтожить документ', self.kill_current_doc ),
        }

    def available_commands(self):
        if self.__current_document is None:
            return self.__no_doc
        elif isinstance ( self.__current_document, docs.Nakladnaya ):
            return self.__with_nakladnaya
        elif isinstance ( self.__current_document, docs.Invoice ):
            return self.__with_invoice
        else:
            raise NotImplementedError('Unknown document type')

    def user_actions_sequence(self):
        while True:
            cmd = self.available_commands()
            for symbol, contents in cmd.items():
                print(f'{symbol} - {contents[0]}')
            print('0 - Завершить работу')
            action = input(': ').strip()
            if action == '0':
                break
            elif action in cmd:
                yield cmd[action][1] #ссылка на функцию обработчик команды пользователя
            else:
                print('<неизвестная команда>')

    def create_nakl(self):
        num = input('Номер: ')
        self.__current_document = docs.Nakladnaya (number=int(num) )

    def create_invoice(self):
        num = input('Наименование: ')
        self.__current_document = docs.Invoice( number = int(num))

    def add_pos_to_nakl(self):
        title = input('Наименование ').strip()
        quantity = input('Количество ').strip()
        price = input('Цена ').strip()
        summa = input('Сумма ').strip()
        quantity = int(quantity)
        if price == '':
            price = None
        else:
            price = Decimal(price)
        if summa == '':
            summa = None
        else:
            summa = Decimal(summa).quantize(Decimal('0.01'))
        self.__current_document.add_pos(title, quantity, price, summa)

    def change_number(self):
        number = input('Новый номер: ').strip()
        self.__current_document.number = int(number)

    def set_address(self):
        addr = input('Адрес доставки: ').strip()
        self.__current_document.address = addr

    def current_doc_show(self):
        self.__current_document.show()

    def kill_current_doc(self):
        self.__current_document = None

    def save_current_doc(self):
        filepath = input('Файл: ').strip()
        with open(filepath, 'wb') as trg:
            pickle.dump(self.__current_document, trg, fix_imports=False)

    def load_doc(self):
        filepath = input('Файл: ').strip()
        with open(filepath, 'rb') as src:
            self.__current_document = pickle.load(src, fix_imports=False)
    
    def run(self):
        for action_fync in self.user_actions_sequence():
            action_fync()