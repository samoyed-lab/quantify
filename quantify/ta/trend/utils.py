def fillna(series, fillna):
    if fillna is not None:
        if fillna in {'backfill', 'bfill', 'pad', 'ffill'}:
            series.fillna(method=fillna, inplace=True)
        else:
            series.fillna(value=fillna, inplace=True)
            