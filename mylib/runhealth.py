from random import choices
import pandas as pd

df = pd.read_csv('fetal_health.csv')

# randomly select 10 numbers
def random_num(df):

    random_number = choices(range(0,df.shape[0]), k=10)

    return random_number
# return a list of fetal health status
def health_generator(df):
    """Returns back random health fetal status"""

    num = random_num(df)
    health = df.iloc[num, 21]
    return list(health.values[:10])
