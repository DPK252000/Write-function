def is_leap(year):
    leap = False
    if year%4:
        return False
    elif year%100:
        return True
    elif year%400:
        return False
    else:
        return True

        """ Method 2 """
        def is_leap(year):
          leap = False
    
    # Write your logic here
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return leap
    if (year % 4 == 0):
        return True
    else:
        return False  
    
    return leap
year = int(input())
print(is_leap(year))