#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    order = []
    for i, x in enumerate(predictions):
        val = abs(net_worths[i, 0] - predictions[i, 0])
        order.append(val)
    order.sort()
    max_val = order[80]
    print('maximum error value: {}'.format(max_val))  # max value of error

    clean = []
    for i in range(80):
        errors = abs(net_worths[i, 0] - predictions[i, 0])
        if errors <= max_val:
            clean.append((ages[i, 0], net_worths[i, 0], errors))
    #print(clean)

    return clean

