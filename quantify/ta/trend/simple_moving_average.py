import pandas as pd
import plotly.graph_objects as go

from .indicator_base import PlotableIndicator
from .utils import fillna


class SimpleMovingAverage(PlotableIndicator):

    def __init__(self, window, fillna=None, name=None):
        super().__init__(f'SMA-{window}' if name is None else name)
        self.window = window
        self.fillna = fillna

    def process(self, time_series):
        self.data = time_series.close.rolling(self.window).mean()
        fillna(self.data, self.fillna)
        return self.data

    def plot(self, time_series):
        fig = go.Scatter(x=time_series.date, y=self.data, name=self.name)
        return fig
