import pandas as pd
import os

def getDB():

        bias    =   ""
        if os.getcwd()[:-2] != "DB":
                bias = "DB//"
        Result  =   pd.read_csv(bias + 'results.csv')
        Users   =   pd.read_csv(bias + 'users.csv')
        return Result, Users