import pandas as pd
import plotly.graph_objects as go

from .register import register_indicator
from .indicator_base import PlotableIndicator
from .utils import fillna


@register_indicator
class ExponentialMovingAverage(PlotableIndicator):

    def __init__(self, window, fillna=False, name=None):
        super().__init__(f'EMA-{window}' if name is None else name)
        self.window = window
        self.fillna = fillna

    def process(self, time_series):
        self.data = time_series.close.ewm(
            span=self.window,
            min_periods = 0 if self.fillna else self.window
        ).mean()
        fillna(self.data, self.fillna)
        return self.data

    def plot(self, time_series):
        fig = go.Scatter(x=time_series.date, y=self.data, name=self.name)
        return fig
