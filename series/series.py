def slices(series, length):
    if len(series) == 0:
        raise ValueError("series is empty")
    if length < 1:
        raise ValueError("slice length is less than 1")
    if length > len(series):
        raise ValueError("slice length is too large")
    return [
        series[i:i+length]
        for i in range(0, len(series) - length + 1)
    ]
