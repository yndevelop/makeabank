#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:21:19 2021

@author: user
"""

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")
            
    def statement(self):
        print("Account Balance: ${}".format(self.balance))
        
class Current(Account):
    def __init__(self, name, balance):
        super().__init_(name, balance, min_balance = -1000)
        
    def __str__(self):
        return "{}'s Current Acount : Balance ${}".format(self.name, self.balance)
    
class Savings(Accounts):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
        
    def __str__(self):
        return "{}'s Savings Acount : Balance ${}".format(self.name, self.balance)
        