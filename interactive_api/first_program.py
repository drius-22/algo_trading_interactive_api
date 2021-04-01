
from ib_insync import *

# def main():
    
    

ib = IB()
ib.connect('127.0.0.1', 7496, clientId=1)   # clientId is relative to how many user I create 

contract = Forex('EURUSD')
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)


print(" -- END --")

df = util.df(bars)
print(df)


# if __name__ =="__main__":
#     main()