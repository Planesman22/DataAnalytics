def PWToDC(PW):
    Frequency = 400
    Period = 1/Frequency
    return (PW/Period) * 0.0001

print(PWToDC(1000))
