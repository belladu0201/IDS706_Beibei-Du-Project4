from random import choices
import pandas as pd

df = pd.read_csv('fetal_health.csv')

def random_num(df):

    random_number = choices(range(0,df.shape[0]), k=1)

    return random_number

def health_generator(df):
    """Returns back random health fetal status"""

    num = random_num(df)
    health = df.iloc[num, 21]
    return health.values[0]
