import pandas as pd
import numpy as np
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

# from matplotlib.backends.backend_agg import FigureCanvas
# from datetime import date
from math import ceil
# from matplotlib.figure import Figure
# not needed for mpl >= 3.1
# from matplotlib.backends.backend_agg import FigureCanvas
df = pd.DataFrame

