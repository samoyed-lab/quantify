from functools import wraps

from .simple_moving_average import SimpleMovingAverage


class TimeSeriesAnalysisFacet:
    """
    A facet that exposes all analysis operations, indicators and
    actions for a `TimeSeries`.
    """

    def __init__(self, time_series):
        self.time_series = time_series
        self.SimpleMovingAverage = self.facet_wrap(SimpleMovingAverage)

    def facet_wrap(self, cls):

        #@wraps(cls)
        def constructor(register=True, *args, **kwargs):
            instance = cls(*args, **kwargs)
            if register:
                instance.register(self.time_series)

            return instance.process(self.time_series)

        return constructor
