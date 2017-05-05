#!/usr/bin/env python
###############################
## Program: ticker.py
## Author: Tom Stewart
## Description: read csv of stock values and display them in a rotating visual
## Version: 0.3
## Comments: not the cleanest, but my first attempt at "graphics"
##           'pip install pandas' best for timeseries data
##           This was a lot harder than I anticipated
##           python2 and python3 compatibility
##
################################

from future import standard_library
standard_library.install_aliases()
from builtins import str
from tkinter import *
import argparse
import pandas as pd
import datetime



###Global vars
ticker = Tk()
delay = 100
svar = StringVar()           
messages = []
####



def shift():
    '''shifts message across display'''
    shift.msg = shift.msg[1:] + shift.msg[:1]
    svar.set(shift.msg)
    ticker.after(delay, shift)

def readFromCSV(filename, day):
    '''reads values from csv, had to use pandas to match TODAY value'''
    lines = pd.read_csv(filename, parse_dates=[1],
                        header=None, usecols=[0, 1, 2, 3],
                        names=['date', 'name', 'price' , 'change'],
                        infer_datetime_format=1)
    df = pd.DataFrame(lines, columns= ['date', 'name', 'price' , 'change'])
    df['date'] = pd.to_datetime(df['date'])
    df.index = df['date']
    dft = df[day] # YYYY-MM-DD match
    for row in dft.itertuples(index=False, name='data'):
        #line = getattr(row, "name"), getattr(row, "price"), getattr(row, "change")
        linestr = (str(getattr(row, "date")) + " " + str(getattr(row, "name"))
                   + " " + str(getattr(row, "price")) + " " + str(getattr(row, "change")) + " ")
        messages.append(linestr)
    

def runLoop(filename):
    '''sets window format and gets messages for stream'''
    day = datetime.datetime.now().strftime('%Y-%m-%d')
    label = Label(ticker, textvariable=svar, 
                  height=3, width=40,
                  background='black', foreground='green' )
 
    readFromCSV(filename, day)
    shift.msg = str(messages) #this is ugly string(array[linestr])
    shift()
    label.pack()
    ticker.mainloop()


def main():
    '''interfaceing'''
    parser = argparse.ArgumentParser(description="read csv of stock values and display them in a rotating visuals")
    parser.add_argument('-f', dest='File', type=str, help='Alternative CSV file to read data from')
    args = parser.parse_args()
    if args.File is None:
        filename = 'stock_value.csv'
    else:
        filename = args.File

    #day = datetime.datetime.now().strftime('%Y-%m-%d')
    #print day
    runLoop(filename)



if __name__ == '__main__':
    main()
