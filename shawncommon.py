def PWToDC(PW):
    Frequency = 400
    Period = 1/Frequency
    return (PW/Period) * 0.0001

def PowerToDC(Power):
    # We use PW range from 1000-2000
    return PWToDC(1000+1000*Power)