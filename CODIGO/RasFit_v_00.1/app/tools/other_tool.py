#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime




def calc_IMC(weigth, height):
    IMC = weigth/(height**2)

    return IMC



def today():
    today = datetime.date.today()

    return today



def calculate_days(old_date):
    today = datetime.date.today()
    tmp = old_date.split("-")
    tmp_day = datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2]) )
    diff = today - tmp_day 

    return diff.days