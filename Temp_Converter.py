
def k_calc():
    print(temp, temp_calc, ('˚ is: '))
    kel_cel = temp - 273.15
    kel_fah = ((temp - 273.15) * 1.8) + 32
    kel_ran = temp * 1.8
    print(kel_cel, ' ˚C')
    print(kel_fah, ' ˚F')
    print(kel_ran, ' ˚R')


def r_calc():
    print(temp, temp_calc, ('˚ is: '))
    ran_fah = temp - 459.67
    ran_cel = (temp - 491.67)*1.8
    ran_kel = temp * 1.8
    print(ran_fah, ' ˚F')
    print(ran_cel, ' ˚C')
    print(ran_kel, ' ˚K')


def f_calc():
    print(temp, temp_calc, ('˚ is: '))
    fah_cel = (temp - 32) * 1.8
    fah_ran = temp + 459.76
    fah_kel = ((temp - 32) * 1.8) + 273.15
    print(fah_ran, ' ˚R')
    print(fah_cel, ' ˚C')
    print(fah_kel, ' ˚K')


def c_calc():
    print(temp, temp_calc, ('˚ is: '))
    cel_fah = (temp * 1.8) + 32
    cel_kel = temp + 273.15
    cel_ran = (temp * 1.8) + 491.67
    print(cel_kel, ' ˚K')
    print(cel_fah, ' ˚F')
    print(cel_ran, ' ˚R')

# Deciding what function to use to calculate remaining values
def temp_calc():
    global scale
    scale = input(str(
        "What temprature scale did you want to convert from? F= Fahrenheit, C=Celsius, R= Rankine, K:+ Kelvin: "))
    scale = scale.upper()
    while True:
        try:
            if scale is 'K':
                k_calc()
            if scale is 'R':
                r_calc()
            if scale is 'F':
                f_calc()
            if scale is 'C':
                c_calc()
        except:
            print('Please select a proper temperature scale: ')
            continue

# User input to star program
while True:
    try:
        temp = float(
            input('What is the numerical temperature that you would like converted?: '))
        temp_calc()
    except ValueError:
        print('Please check your input: ')
        continue
