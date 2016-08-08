import math
def round_up_to_nearest(num, base=5):
    '''round_up_to_nearest rounds up to the nearest 5 or whatever int you set as base.

    Contact:
    robtheoceanographer@gmail.com
    '''
    return int(math.ceil(num / float(base))) * base
