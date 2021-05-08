
# class TempCon:
#     def __init__(self, scale, temp):
#         self.scale = scale
#         self.temp = temp
def choose_scale():
    while True:
        try:
#User input
            scale = input(str("What temprature scale did you want to convert from? F= Fahrenheit, C=Celsius, R= Rankine, K:+ Kelvin: "))
#Make it upper case for ease of reading
            scale_case = scale.upper()
            in_temp()
        except ValueError:
            print ('please choose a valid scale')
            continue

def in_temp():
    while True:
        try:
            temp = float (input('What is the numerical temperature that you would like converted?: '))
            temp_calc()
        except ValueError:
            print ('Please put in a numerical value with a decimal')
            continue
# Degree symbol on mac is Opt+K ˚
def k_calc():
    print (in_temp,scale_case,('˚ is: '))
    kel_cel = in_temp - 273.15
    kel_fah = ((in_temp -273.15) * 1.8) + 32
    kel_ran = in_temp * 1.8
    print (kel_cel,' ˚C')
    print (kel_fah, ' ˚F')
    print (kel_ran, ' ˚R')

def r_calc():
    print (in_temp,scale_case,('˚ is: '))
    ran_fah = in_temp - 459.67
    ran_cel = (in_temp - 491.67)*1.8
    ran_kel = in_temp *1.8
    print (ran_fah, ' ˚F')
    print (ran_cel, ' ˚C')
    print (ran_kel, ' ˚K')

def f_calc():
    print (in_temp,scale_case,('˚ is: '))
    fah_cel = (in_temp - 32) * 1.8
    fah_ran = in_temp + 459.76
    fah_kel = ((in_temp- 32) *1.8) + 273.15
    print (fah_ran, ' ˚R')
    print (fah_cel, ' ˚C')
    print (fah_kel, ' ˚K')

def c_calc():
    print (in_temp,scale_case,('˚ is: '))
    cel_fah = (in_temp * 1.8) + 32
    cel_kel = in_temp + 273.15
    cel_ran = (in_temp * 1.8) + 491.67
    print (cel_kel, ' ˚K')
    print (cel_fah, ' ˚F')
    print (cel_ran, ' ˚R')

def temp_calc():
    while True:
        try:
            if scale_case == 'K':
                k_calc()
            elif scale_case == 'R':
                r_calc()
            elif scale_case == 'F':
                f_calc()
            elif scale_case == 'C':
                c_calc()
                
choose_scale()