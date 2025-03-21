def filter_nondigits(data: list) -> list:
    """
    INSERT DOCSTRING HERE
    """
    filtered = []
    for str in data:
        str = str.strip()
        if (str.isdigit()):
            filtered.append(int(str))

    return filtered
        


