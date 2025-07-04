def is_leap_year(year):
    # this program returns the year type - leap or not
    # 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True        
    return False
