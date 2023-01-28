from functools import wraps

from .register import ALL_FACET_INDICATORS
from .simple_moving_average import SimpleMovingAverage
from .exponential_moving_average import ExponentialMovingAverage


class TimeSeriesAnalysisFacet:
    """
    A facet that exposes all analysis operations, indicators and
    actions for a `TimeSeries`.
    """

    def __init__(self, time_series):
        self.time_series = time_series

        for indicator in ALL_FACET_INDICATORS:
            print(indicator.__name__)
            setattr(self, indicator.__name__, self.facet_wrap(indicator))
            
        # self.SimpleMovingAverage = self.facet_wrap(SimpleMovingAverage)
        # self.ExponentialMovingAverage = self.facet_wrap(ExponentialMovingAverage)

    def facet_wrap(self, cls):

        @wraps(cls)
        def constructor(*args, **kwargs):
            register = kwargs.get('register', True)
            kwargs.pop('register', None)

            instance = cls(*args, **kwargs)
            if register:
                instance.add_to(self.time_series)

            return instance.process(self.time_series)

        return constructor
