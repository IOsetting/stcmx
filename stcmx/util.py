
def format_frequency(val):
    if val > 1000000:
        return "%.6fMHz"%(val / 1000000)
    elif val > 1000:
        return "%.3fKHz"%(val / 1000)
    else:
        return "%dHz"%(val)