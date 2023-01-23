class PlotableIndicator:
    """
    Represents an indicator that belongs to a time series.
    
    `PlotableIndicator#register(time_series)` should be called
    automatically if initialized through the `create` facet of a
    `TimeSeries`.

    When created by a `TimeSeriesAnalysisFacet`, the order of
    operation on this object would be:
        1. __init__()
        2. register() (with the associate instance of `TimeSeries`)
        3. process()
    When invoked naturally, `process()` can be invoked to directly
    compute the result of analyzing with this indicator.
    """

    def __init__(self, name):
        self.name = name

    def register(self, time_series):
        time_series.register_indicator(self.name, self)

    def process(self, time_series):
        raise NotImplemented

    def plot(self, fig):
        raise NotImplemented
