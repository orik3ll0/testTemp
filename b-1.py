import pandas as pd
import numpy as np
from decimal import *

field = ["A", "B", "C", "D"]
fieldData = [
    [Decimal('6025'), Decimal('9135')],
    [Decimal('302276'), 'NaN'],
    [Decimal('200'), Decimal('-3000')],
    [Decimal('3500'), '']
]

df = pd.DataFrame(fieldData, index=[field], columns=['2017', '2018'])

# as values
print(df[["2017", "2018"]].astype(str).values.max(axis=1))

# as table
print(df.astype(str).max(axis=1, skipna=True))

# main table
print(df)
