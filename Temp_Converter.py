
def k_calc():
    print(temp, scale, ('˚ is: '))
    kel_cel = temp - 273.15
    kel_fah = ((temp - 273.15) * 1.8) + 32
    kel_ran = temp * 1.8
    print(kel_cel, ' ˚C')
    print(kel_fah, ' ˚F')
    print(kel_ran, ' ˚R')


def r_calc():
    print(temp, scale, ('˚ is: '))
    ran_fah = temp - 459.67
    ran_cel = (temp - 491.67)*1.8
    ran_kel = temp * 1.8
    print(ran_fah, ' ˚F')
    print(ran_cel, ' ˚C')
    print(ran_kel, ' ˚K')


def f_calc():
    print(temp, scale, ('˚ is: '))
    fah_cel = (temp - 32) * 1.8
    fah_ran = temp + 459.76
    fah_kel = ((temp - 32) * 1.8) + 273.15
    print(fah_ran, ' ˚R')
    print(fah_cel, ' ˚C')
    print(fah_kel, ' ˚K')


def c_calc():
    print(temp, scale, ('˚ is: '))
    cel_fah = (temp * 1.8) + 32
    cel_kel = temp + 273.15
    cel_ran = (temp * 1.8) + 491.67
    print(cel_kel, ' ˚K')
    print(cel_fah, ' ˚F')
    print(cel_ran, ' ˚R')


def temp_calc():
    while True:
        try:
            if scale == 'K':
                k_calc()
            elif scale == 'R':
                r_calc()
            elif scale == 'F':
                f_calc()
            elif scale == 'C':
                c_calc()
        except:
            print('Please select a proper temperature scale: ')
            continue


while True:
    try:
        temp = float(
            input('What is the numerical temperature that you would like converted?: '))
        break
    except ValueError:
        print('Please check your input: ')
        continue

while True:
    try:
        scale = input(str(
            "What temprature scale did you want to convert from? F= Fahrenheit, C=Celsius, R= Rankine, K:+ Kelvin: "))
        scale = scale.upper()
        temp_calc()
    except ValueError:
        print('Please choose a valid temperature scale: ')
        continue
