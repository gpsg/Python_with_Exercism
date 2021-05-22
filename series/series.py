def slices(series: str, length: int) -> list[str]:
    size = len(series)
    if length > size or length < 1:
        raise ValueError("Invalid Input")
    return [series[i:i + length] for i in range(size - length + 1)]
