import pandas as pd


class TimeSeries:
    """
    The TimeSeries class represents the record of a security's
    price over a period of time. It is created as the basis for
    most technical
    """

    def __init__(
        self, open, close, high, low, date=None, data=None
    ):
        """
        Initializes a TimeSeries object with stock price information.
        If `data` is set (to a Pandas data frame), then `open`, `close`,
        `high`, `low`
        """

        if data is None: # input as array-like
            self.open = pd.Series(open, dtype='float64')
            self.close = pd.Series(close, dtype='float64')
            self.high = pd.Series(high, dtype='float64')
            self.low = pd.Series(low, dtype='float64')

            self.date = pd.Series(date) if date is not None else None

            series = [self.open, self.close, self.high, self.low]
            if date is not None: series.append(self.date)
            lengths = [len(i) for i in series]

            if len(set(lengths)) != 1:
                raise ValueError(
                    'The length of `open`, `close`, `high`, `low` (and `date`, if'
                    f' applicable) should be the same, instead got {lengths}'
                )

        else:
            for k, v in {
                'open': open, 'close': close, 'high': high, 'low': low
            }.items():
                if type(v) != str:
                    raise TypeError(f'Type of "{k}" must be a string, got "{type(v)}"')

            self.open = data[open].copy()
            self.close = data[close].copy()
            self.high = data[high].copy()
            self.low = data[low].copy()

            if date is None:
                self.date = None
            else:
                self.data = data[date].copy()

    def plot():
        pass
