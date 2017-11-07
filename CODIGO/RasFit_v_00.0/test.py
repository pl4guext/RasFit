#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
from app.utils import color
from app.utils import file_manager





if __name__ == "__main__":

    users = file_manager.read_csv_dict("users.csv")
    file_manager.save_csv_dict("prueba.csv", users)

