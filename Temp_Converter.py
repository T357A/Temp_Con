#  Code explainds the comments to the computer, not to other programmers - Andy Harris ;)
# What are you trying to help the user with?
#  Output for users requirement:
# From Kelvin input
def k_calc():
    print(temp, scale, ('˚ is: '))
    kel_cel = round((temp - 273.15),)
    kel_fah = round((((temp - 273.15) * 1.8) + 32), 2)
    kel_ran = round((temp * 1.8), 2)
    print(kel_cel, ' ˚C')
    print(kel_fah, ' ˚F')
    print(kel_ran, ' ˚R')

# From Rankine input
def r_calc():
    print(temp, scale, ('˚ is: '))
    ran_fah = round((temp - 459.67), 2)
    ran_cel = round(((temp - 491.67)*1.8), 2)
    ran_kel = round((temp * 1.8), 2)
    print(ran_fah, ' ˚F')
    print(ran_cel, ' ˚C')
    print(ran_kel, ' ˚K')

# From Fahrenheit input
def f_calc():
    print(temp, scale, ('˚ is: '))
    fah_cel = round(((temp - 32) / 1.8), 2)
    fah_ran = round((temp + 459.67), 2)
    fah_kel = round((((temp - 32) / 1.8) + 273.15), 2)
    print(fah_ran, ' ˚R')
    print(fah_cel, ' ˚C')
    print(fah_kel, ' ˚K')

# From Celsius input
def c_calc():
    print(temp, scale, ('˚ is: '))
    cel_fah = round(((temp * 1.8) + 32), 2)
    cel_kel = round((temp + 273.15), 2)
    cel_ran = round(((temp * 1.8) + 491.67), 2)
    print(cel_kel, ' ˚K')
    print(cel_fah, ' ˚F')
    print(cel_ran, ' ˚R')

# Deciding what output the user is seeking to calculate remaining values


def temp_calc():
    global scale
    scale = input(str(
        "What temprature scale did you want to convert from? F= Fahrenheit, C=Celsius, R= Rankine, K:+ Kelvin: "))
    scale = scale.upper()
    if scale == 'K':
        k_calc()
    elif scale == 'R':
        r_calc()
    elif scale == 'F':
        f_calc()
    elif scale == 'C':
        c_calc()
    else:
        print('Please select a proper temperature scale: ')
        temp_calc()


# Question to user input to start program
while True:
    try:
        temp = float(
            input('What is the numerical temperature that you would like converted?: '))
        temp_calc()
    except ValueError:
        print('Please check your input: ')
        continue
# Future- GUI with buttons
