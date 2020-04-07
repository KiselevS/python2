#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

class Document(object):
    def __init__ (self, number = None):
        self.__number = number
        self.__created = datetime.now()

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        self.__number = new_number

    @property
    def created(self):
        return self.__created

    def show(self):
        print(40*'=')
        print(f'Документ № {self.number}')
        print(f'  Создан: {self.created}')
        print(40*'=')