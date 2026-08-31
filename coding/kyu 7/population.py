def nb_year(p0, percent, aug, p):
    cnt_yrs = 1
    while(p0 < p):
        p0 = (p0 * (1 + percent * 0.01)) + aug
        if p0 < p:
            cnt_yrs += 1
        else:
            break
    
    return cnt_yrs

def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 = int(p0 * (1 + percent / 100) + aug)
        years += 1
    return years
#ОТ цхатГПТ