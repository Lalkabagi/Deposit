n = int(input("Скільки гривень хочете вкласти:"))
years = int(input("На скільки років хочете вкласти:"))

for i in range(years):
    n += n*0.10

def bank(n,years):
    print(f"{n}")
    
print(bank(n,years))