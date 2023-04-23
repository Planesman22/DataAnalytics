def PWToDC(PW):
    Frequency = 400
    Period = 1/Frequency
    return int((PW/Period) * 0.000001 * 65535)

def PowerToDC(Power):
    # We use PW range from 1000-2000

    return PWToDC(1000+(1000*Power))



