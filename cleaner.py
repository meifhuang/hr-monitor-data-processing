def filter_nondigits(data: list) -> list:
    """
    This function takes a list of strings and returns a new list with strings converted to integers and non-digit characters filtered out. 

    Args: 
        data (list): list of heart rate data that has to be cleaned 

    Returns:
        list: list of heart rate data that only contain valid digits
    """
    
    filtered = []
    for x in data:
        x = x.strip()
        if (x.isdigit()):
            filtered.append(int(x))

    return filtered
        


