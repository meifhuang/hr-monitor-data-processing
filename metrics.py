def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    average = 0
    if (len(data) > 0):
        print(len(data))
        for num in data:
            average += num
        average /= len(data)
        return round(average,2)
    return data

def maximum(data: list) -> float:
    """
    Find the maximum value of the list

    Args:
        data (list): list of integers representing heart rate samples

    Returns:
        float: a floating point value representing the maximum value of the list
    """
    if (len(data) > 0):
        max = data[0]
        for num in data:
            if (num > max):
                max = num
        return round(max,2)
    return data

def variance(data: list) -> float:
    """
    Calculate population variance

    Args:
        data (list): list of integers representing heart rate samples

    Returns:
        float: a floating point value representing the population variance
    """
    if (len(data) > 0): 
        avg = average(data)
        variance = 0
        for num in data:
            variance += (num - avg) ** 2
        variance /= len(data)
        return round(variance,2)
    return data

def standard_deviation(data: list) -> float:
    """
    Calculate the population standard deviation

    Args: 
        data (list): list of integers heart rate samples

    Returns:
        float: a floating point value representing the population standard deviation 
    """
    std = 0
    if (len(data) > 0):
        std = variance(data)
        std = std ** (1/2)
        return round(std,2)
    return data

