# Importando as bibliotecas utlizadas nessa etapa da análise
import numpy as np
import pandas as pd
import yfinance as yf
import os 
from datetime import date

bovespa = yf.download("^bvsp", start="2014-01-01", end=date.today())

try:    
   bovespa.to_csv(f'/download/bovespa_{date.today()}.csv')

except OSError as error:
    print(error)

finally:
    os.mkdir("/download", )
    bovespa.to_csv(f'/download/bovespa_{date.today()}.csv')

    