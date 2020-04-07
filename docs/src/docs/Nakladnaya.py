#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
from .NakPos import NakPos
from .Document import Document


class Nakladnaya(Document):

    def __init__(self, number=None):
        '''
            @TODO: сделать возможность генерации номеров по умолчанию,
            если номер не был задан пользователем.
            дата отправки
            дата фактической отправки
        '''
        # добавить метод подписать и переменную self.__sing, подписать можно только корректные доки (good = true), попытка подписать плохую накл считается ошибкой (выбросить исклчение NotImplementedError).
        # подписанная накладная не подлежит исправлению
        # копию проекта в гит
        # номер рабочего места + передача по сети
        super().__init__(number)
        self.__address = None
        self.__positions = []

    @property
    def good(self):
        if self.__address is None:
            return False
        if len(self.__positions) == 0:
            return False
        #return all( ( p.good for p in self.__positions ) )
        for p in self.__positions:
            if not p.good:
                return False
        return True

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address
        
    @property
    def itogo(self):
        s = (x.summa for x in self.__positions )
        return sum(s)

    def add_pos(self, *args, **kwargs):        
        pos = NakPos(*args, **kwargs)
        self.__positions.append(pos)
            
    def show(self):
        print(40*'=')
        print(f'Накладная № {self.number}')
        ct = self.created.strftime('%d.%m.%Y %H:%M')
        print(f'  Создана: {ct}')
        if self.address is not None:
            print(f'  Адрес доставки: {self.address}')
        print(40*'-')
        for k, pos in enumerate(self.__positions, 1):
            print(f'{k:2}. {pos}')
        print(f'Итого: {self.itogo:7.2f}')
        print(40*'=')
        if not self.good:
            print ('***** Плохая накладная *****')