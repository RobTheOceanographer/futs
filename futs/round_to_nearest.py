def round_to_nearest(num, base=5):
    '''round_to_nearest rounds to the nearest 5 or whatever int you set as base in the normal way.

    Contact:
    robtheoceanographer@gmail.com
    '''
    return int(base * round(float(num)/base))
