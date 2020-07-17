import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import time
#import xlwt

pd.set_option("display.max_rows", 1000)
pd.set_option("display.max_columns", 1000)
df = pd.read_csv(r"")
#df = pd.read_csv("csuser__csuser__eam2__search2_1594859881_9778.csv")
#df = df.drop(columns=["UserSid_readable", "fEnd", "fStart"])

def user(username):
    cg = df.User_Name.values
    num_genres = pd.DataFrame(np.array(cg).reshape(username, 1))
    a = str(pd.value_counts(num_genres[0]))
    f = open("" + time.strftime('%Y_%m_%d') + ".txt", "w", encoding="utf-8")
    f.write(a)
    f.close()

def host(hostname):
    cg = df.Host_Name.values
    num_genres = pd.DataFrame(np.array(cg).reshape(hostname, 1))
    a = str(pd.value_counts(num_genres[0]))
    f = open("" + time.strftime('%Y_%m_%d') + ".txt", "w", encoding="utf-8")
    f.write(a)
    f.close()

if __name__ == '__main__':
    column = int(input("columns："))
    if type(column) is int:
        user(column)
        host(column)
        print(time.strftime('%Y_%m_%d_%H_%M_%S'))
    else:
        print("please input number.")
