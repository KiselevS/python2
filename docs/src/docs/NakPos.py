#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NakPos(object):
    def __init__(self, title, quantity = 1, price = None, summa = None):
        self.__title = title
        self.__quantity = quantity
        self.__price = price
        self.__summa = summa
        # self.__good = good

    @property
    def good(self):
        if self.__price is None:
            return self.__summa is not None
        return self.quantity * self.price == self.summa

    @property
    def title(self):
        return self.__title

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        #Записать в журнал приложения, что позиция изменилась
        self.__quantity = new_quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def summa(self):
        if self.__summa is not None:
            return self.__summa
        summa = self.quantity * self.price
        return summa

    @summa.setter
    def summa(self, new_summa):
        self.__summa = new_summa
    
    @summa.deleter
    def summa(self):
        self.__summa = None

    def __str__(self):
        if self.__price is None:
            return f'{self.title:15} {self.quantity:2}  ---  {self.summa:6.2f}'
        else:
            return f'{self.title:15} {self.quantity:2} {self.price:5.2f} {self.summa:6.2f}'