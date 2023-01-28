ALL_FACET_INDICATORS = []

def register_indicator(indicator_class):
    """
    Registers an indicator for TimeSeries.

    After registration, an instance can be added via
    `TimeSeries.create.YourIndicator(*args, **kwargs)`.
    """

    ALL_FACET_INDICATORS.append(indicator_class)
