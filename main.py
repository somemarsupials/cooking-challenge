import sys
import pandas

sys.path.append('source')

import ingredients
import unpack

limit = 0
convert = 0

for arg in sys.argv:
    if 'limit=' in arg:
        limit = int(arg.split('=')[1])
    elif 'convert=' in arg:
        convert = int(arg.split('=')[1])

if 'generate' in sys.argv:
    i = ingredients.Ingredients(unpack.unpack('train.json'), convert)
    df = i.vectorise(limit)
    i.save('data/train.csv')
elif 'open' in sys.argv:
    df = pandas.read_csv('data/train.csv')
