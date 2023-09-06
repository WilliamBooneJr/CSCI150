#Billy Boone
#CS150
#04/23/23
#This is a module that prompts for temperatures and performs
#different calculations. If it is run as main the test client will execute.

def far_to_c():
    far = float(input("Enter degrees Fahrenheit:"))
    c_degrees = (far - 32) * (5/9)
    return c_degrees

def c_to_far():
    c = float(input("Enter degrees Celsius:"))
    far_degrees = (c * (9/5)) + 32
    return far_degrees

def below_freez_f():
    lst = input("Enter list of Fahrenheit temperatures(seperate by comma):").split(',')
    
    freez_list = []
    for num in lst:
        if int(num) < 32:
            freez_list.append(int(num))
    return freez_list
            
    
def below_freez_c():
    lst = input("Enter list of Celsius temperatures(seperate by comma):").split(',')
   
    freez_list = []
    for num in lst:
        if int(num) < 0:
            freez_list.append(int(num))
    return freez_list
    

def weather():
    temp = int(input("Enter temperature:"))
    if temp > 90:
        print("Too hot")
    elif 70 < temp <= 90:
        print("Just right")
    elif 40 < temp <= 70:
        print("Chilly")
    elif 20 < temp <= 40:
        print("Cold")
    elif temp <= 20:
        print("Freezing")
    
    

def main():
    print(f'{"Degrees in Celsius:"}{far_to_c()}')
    print(f'{"Degrees in Celsius:"}{far_to_c()}')
    print(f'{"Degrees in Fahrenheit:"}{c_to_far()}')
    print(f'{"Degrees in Fahrenheit:"}{c_to_far()}')
    print(f'{"Temps below freezing in Fahrenheit:"}{below_freez_f()}')
    print(f'{"Temps below freezing in Fahrenheit:"}{below_freez_f()}')
    print(f'{"Temps below freezing in Celsius:"}{below_freez_c()}')
    print(f'{"Temps below freezing in Celsius:"}{below_freez_c()}')
    print(weather())
    print(weather())
    
    
    

if __name__ == "__main__":
    main()
