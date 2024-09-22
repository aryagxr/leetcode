# 1732 Highest Altitude

def highestAlt(gain):
    altitude = []
    max_alt = 0
    altitude.append(0)
    for i in range(len(gain)):
        new_alt = altitude[i]+gain[i]
        altitude.append(new_alt)
        if altitude[i]> max_alt:
            max_alt = altitude[i]
        print(altitude)
        print(max_alt)
    if altitude[i+1]>max_alt:
        max_alt = altitude[i+1]

    return max_alt
    
    

print(highestAlt([44,-28,97,100,81]))
