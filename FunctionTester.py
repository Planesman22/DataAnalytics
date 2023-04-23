def PWToDC(PW):
    Frequency = 400
    Period = 1/Frequency
    return (PW/Period) * 0.0001

def PowerToDC(Power):
    return PWToDC(1000+1000*Power)

print(PowerToDC(0.0))
