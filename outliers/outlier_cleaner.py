#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    size = len(predictions)

    cleaned_data = []
    data = []


    for index in range(size):
        pred = predictions[index]
        age = ages[index][0]
        net_worth = net_worths[index][0]
        tup = ( age,net_worth, math.fabs(pred - net_worth) )
        #print tup
        data.append( tup )

    #print data

    data.sort(key=lambda tup: tup[2])

    cleaned_size = int(size * 0.9)
    cleaned_data = data[0:cleaned_size]


    

    return cleaned_data