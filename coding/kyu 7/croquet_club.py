def open_or_senior(data):
    output = list()
    for each in data:
        if each[0] < 55 or each[1] <= 7:
            output.append("Open")
        else:
            output.append("Senior")
    
    return output

def croquet_club_lc(data):
    return["Senior" if age >= 55 and handicap >= 8 else "Open" for (age,handicap) in data]