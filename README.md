# Get_Stock_Prices
Python scripts to scrape stock prices


## stock_soup.py
Webscrape yahoo/google for stock prices  
Runs in Python2.7 and Python 3.6  
  
    pip install BeautifulSoup4  
  
Writes/Reads data to stock_value.csv  
Can choose between google or yahoo, also set custom ticker symbols  

```
>python stock_soup.py -S Y -t GOOG AAPL GOLD
Alphabet Inc. (GOOG) 833.01 -1.56 (-0.19%)
Apple Inc. (AAPL) 144.06 -0.71 (-0.49%)
Randgold Resources Limited (GOLD) 89.26 -0.13 (-0.15%)
===== RESTART: stock_soup.py =====
Ford Motor Company (F) 11.25 -0.12 (-1.06%)
General Electric Company (GE) 30.01 -0.01 (-0.03%)
Alphabet Inc. (GOOGL) 850.87 -1.70 (-0.20%)
>python stock_soup.py -h
usage: stock_soup.py [-h] [-f FILE] [-s SITE] [-t TICKER [TICKER ...]]

webscrape yahoo/google for stock prices

optional arguments:
  -h, --help            show this help message and exit
  -f FILE               Alternative CSV file to save data to
  -s SITE               values: G(goole) or Y(yahoo)
  -t TICKER [TICKER ...]
                        Type list of Ticker Symbols
 ```
  
## ticker.py 
Read csv of stock values and display them in a rotating visual  

![ticker](https://github.com/twstewart42/Get_Stock_Prices/blob/master/ticker.PNG)  

    pip install pandas  
  
This is also Python2/3 compatibile.  
This was my first attempt at "graphics" in python and more of a fun project  

```
>python ticker.py -h
usage: ticker.py [-h] [-f FILE]

read csv of stock values and display them in a rotating visuals

optional arguments:
  -h, --help  show this help message and exit
  -f FILE     Alternative CSV file to read data from
  ```


