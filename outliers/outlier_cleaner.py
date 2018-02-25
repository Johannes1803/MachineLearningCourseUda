#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    for i in range(0, len(predictions)):
        cleaned_data.append((ages[i], net_worths[i], abs(net_worths[i] - predictions[i])))

    cleaned_data = sorted(cleaned_data, key=lambda data: data[2])

    removeLength = int(len(cleaned_data)* 0.9)
    cleaned_data =  cleaned_data[: removeLength]
    
    return cleaned_data

