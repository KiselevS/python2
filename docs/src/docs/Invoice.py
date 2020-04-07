#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Document import Document

class Invoice(Document):
    def __init__(self, number=None):
        super().__init__(number)
        self.__contragent = None

    @property
    def contragent(self):
        return self.__contragent

    @contragent.setter
    def contragent(self, new_value):
        self.__contragent = new_value

    #написать функцию show для счета-фактуры
    