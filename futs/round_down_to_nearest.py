def round_down_to_nearest(num, base=5):
    '''round_down_to_nearest rounds down to the nearest 5 or whatever int you set as base.

    Contact:
    robtheoceanographer@gmail.com
    '''
    return num - (num%base)
