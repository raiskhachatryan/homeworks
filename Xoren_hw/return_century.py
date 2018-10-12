year = int(input("input! "))

def year_century(year):
    century = (year-1) // 100 + 1
    return century

print(year_century(year), 'century')




