import pandas as pd


class TimeSeries:
    """
    The TimeSeries class represents the record of a security's
    price over a period of time. It is created as the basis for
    most technical analysis functions.
    """

    def __init__(
        self, open, close, high, low, date=None, volume=None, data=None
    ):
        """
        Initializes a TimeSeries object with stock price information.
        If `data` is set (to a Pandas data frame), then `open`, `close`,
        `high`, `low` are strings indicating the columns of opening price,
        closing price, highest price and lowest price respectively. If
        `data` is not set, then `open`, `close`, `high` and `low` are
        treated like equal-length array-like containing a sequence of
        price data respective to their name.

        :param open: An array-like (or column index into `data`) of data
        points representing the opening price for each day.
        :param close: An array-like (or column index into `data`) of data
        points representing the closing price for each day.
        :param high: An array-like (or column index into `data`) of data
        points representing the highest price for each day.
        :param low: An array-like (or column index into `data`) of data
        points representing the lowest price for each day.
        :param date: An optional array-like (or column index into `data`)
        of dates.
        :param volume: An optional array-like (or column index into `data`)
        of dates.
        """

        if data is None: # input as array-like
            self.open = pd.Series(open, dtype='float64')
            self.close = pd.Series(close, dtype='float64')
            self.high = pd.Series(high, dtype='float64')
            self.low = pd.Series(low, dtype='float64')

            self.date = pd.Series(date) if date is not None else None
            self.volume = pd.Series(volume) if volume is not None else None

            sizes = {
                'open': self.open.size,
                'close': self.close.size,
                'high': self.high.size,
                'low': self.low.size
            }

            if date is not None: sizes['date'] = self.date.size
            if volume is not None: sizes['volume'] = self.volume.size

            if len(set(sizes.values())) != 1:
                raise ValueError(
                    'The length of `open`, `close`, `high`, `low` (and `date '
                    'and `volume`, if applicable) should be the same, instead'
                    f' got {sizes}'
                )

        else:
            for k, v in {
                'open': open, 'close': close, 'high': high, 'low': low
            }.items():
                if type(v) != str:
                    raise TypeError(f'Type of `{k}` must be a string, got {type(v)}')

            self.open = data[open].copy()
            self.close = data[close].copy()
            self.high = data[high].copy()
            self.low = data[low].copy()

            self.date = None if date is None else data[date].copy()

    def plot():
        pass
