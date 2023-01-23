import pandas as pd

from .indicator_base import PlotableIndicator
from .utils import fillna


class SimpleMovingAverage(PlotableIndicator):

    def __init__(self, window, fillna=None, name=None):
        super().__init__(f'SMA-{window}' if name is None else name)
        self.window = window
        self.name = name
        self.fillna = fillna

    def process(self, time_series):
        self.data = time_series.close.rolling(self.window).mean()
        fillna(self.data, self.fillna)
        return self.data
