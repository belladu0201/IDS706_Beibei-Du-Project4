from random import choices

def random_num(df):

    random_number = choices(range(0,df.shape[0]), k=1)

    return random_number

def health_generator(df):
    """Returns back random health fetal status"""

    num = random_num(df)
    health = df.iloc[num, 21]
    return health.values[0]
