##/usr/bin/env python
#########################
## Script: stock_soup.py
## Author: Tom Stewart
## Description: webscrape yahoo/google for stock prices
## Version: 0.5
## Comments: pip install BeautifulSoup4
##           Writes/Reads data to stock_value.csv
##           Can choose between google or yahoo, also set custom ticker symbols to search
##           changed from urllib to requests module
##           python2 and python3 compatibility
##           Added NOSAVE option
##
########################
from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import time
import datetime
import csv
import argparse


def saveToCSV(localtime, name, price, change, filename):
    '''writes values to csv'''
    if filename == "NOSAVE":
        #print("Do not save to file")
        return filename
    else:
        with open(filename, 'a') as fi:
            wtr = csv.writer(fi, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            wtr.writerow([localtime, name, price, change])
        
        fi.close()

        return filename

def readFromCSV(filename):
    '''reads values from csv'''
    with open(filename, 'r') as fi:
        for line in fi:
            print(line)
    fi.close()


def getFromGoogle(symbols, localtime, filename):
    '''gets data from Google'''
    for i in symbols:
        head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        html = requests.get('https://www.google.com/finance?q=%s' % (i) ,   headers=head).content
        soup = BeautifulSoup(html, "html.parser")
        name = soup.find("div", class_="appbar-snippet-primary").text
        price = soup.find('span',class_='pr').span.text
        changev = soup.find('span',class_='ch bld').span.text
        changep = soup.find('span',class_='ch bld').span.findNext('span').text
        change = (str(changev) + str(changep))
        print(name, price, change)
        saveToCSV(localtime, name, price, change, filename)


def getFromYahoo(symbols, localtime, filename):
    '''Gets data from Yahoo'''
    for i in symbols:
        head = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        html = requests.get('https://finance.yahoo.com/quote/%s/options?p%s' % (i, i) ,   headers=head).content
        soup = BeautifulSoup(html, "html.parser")
        name = soup.find("h1", class_="D(ib) Fz(18px)").text
        price = soup.find('div',class_='D(ib) Fw(200) Mend(20px)').span.text
        change = soup.find('div',class_='D(ib) Fw(200) Mend(20px)').span.findNext('span').text
        print(name, price, change)
        saveToCSV(localtime, name, price, change, filename)

def main():
    '''setup options and run program'''
    parser = argparse.ArgumentParser(description="webscrape yahoo/google for stock prices", epilog='Ze data is ours!')
    parser.add_argument('-f', dest='File', type=str, help='Alternative CSV file to save data to')
    parser.add_argument('-x', dest='NoSave', action='store_true', help='Do NOT save values to csv')
    parser.add_argument('-s', dest='Site', type=str, choices=['G','Y'], help='values: G(goole) or Y(yahoo)')
    parser.add_argument('-t', dest='Ticker', nargs='+', type=str, help='Type list of Ticker Symbols')
   

    args = parser.parse_args()

    if args.Site is None:
        site = "Y"
    else:
        site = args.Site

    #localtime = time.asctime( time.localtime(time.time()))
    localtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    print(localtime)
    
    if args.File is None:
        filename = 'stock_value.csv'
    else:
        filename = args.File
    if args.NoSave is False:
        filename = filename
    else:
        filename = "NOSAVE"

    if args.Ticker is None:
        symbols = ('F', 'GE', 'GOOGL')
    else:
        symbols = args.Ticker
    
    if  site == "G" or site == "g" :
        getFromGoogle(symbols, localtime, filename)
    elif site == "Y" or site == "y" :
        getFromYahoo(symbols, localtime, filename)


    '''only need to uncomment this for testing'''
    #readFromCSV(filename):


if __name__ == '__main__':
    main()
