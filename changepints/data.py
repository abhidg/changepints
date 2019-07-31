# Reads PINTS functional testing data
import pandas as pd

class ChangePintsData:
    """PINTS Changepoint data reader

    This reads timeseries data, does the necessary conversion
    to datetime format, and returns a dataframe.
    """
    def __init__(self, source):
        df = pd.read_csv(source, header=None, names=[
            'year', 'month', 'day',
            'hour', 'minutes', 'seconds',
            'commit', 'score'])
        df['date'] = df.year.map(str) + '-' \
            + df.month.map(str) + '-' \
            + df.day.map(str) + 'T' \
            + df.hour.map(str) + ':' \
            + df.minutes.map(str) + ':' \
            + df.seconds.map(str)
        df['date'] = pd.to_datetime(df['date'])
        self.data = df[['date', 'commit', 'score']]
