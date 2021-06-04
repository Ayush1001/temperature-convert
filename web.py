import math
import os
import sys
import argparse
from scipy.constants import convert_temperature

def convert_temprature(val, inputScale, outputScale, student_response):
        inputScale = input_unit.lower().strip()
        outputScale = output_unit.lower().strip()

        kelvin_value = 0
        target_value = 0

        if inputScale in ['fahrenheit','rankine','kelvin','celsius'] and outputScale in ['fahrenheit','rankine','kelvin','celsius']:
           if inputScale == 'celsius':
              kelvin_value = val + 273.15
           elif inputScale == 'fahrenheit':
              kelvin_value = ((val - 32)*5/9) + 273.15
           elif inputScale == 'rankine':
              kelvin_value = ((input_vaule)*5)/9
           elif inputScale == 'kelvin':
              kelvin_value = val

           if outputScale == 'celsius':
              target_value = kelvin_value - 273.15
           elif outputScale == 'fahrenheit':
              target_value = ((kelvin_value - 273.15)*9/5) + 32
           elif outputScale == 'rankine':
              target_value = kelvin_value * 1.8
           elif outputScale == 'kelvin':
              target_value = kelvin_value
        else:
           output = "invalid"
        if round(student_response,1) == round(target_value,1):
           output = "correct"
        elif round(student_response,1) != round(target_value,1):
           output = "incorrect"
        else:
           output = "incorrect"
           
        return (output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tempreature unit conversion checker')
    parser.add_argument('-inputValue', '--val',type=str,
                        help='Input temprature value')
    parser.add_argument('-inputUnit', '--inunit',type=str,
                        help='Input unit of temprature')
    parser.add_argument('-targetUnit', '--outunit',type=str,
                        help='Target temperature Unit')
    parser.add_argument('-targetVal', '--tar',type=str,
                        help='Target temperature value')
    args = parser.parse_args()

    validUnits = ["Fahrenheit", "Rankine", "Kelvin", "Celsius"]

    Input = args.val
    inUnit = str(args.inunit)
    Output = args.tar
    outUnit = str(args.outunit)

    result = convert_temprature(Input, inUnit, outunit, Output)
    print(result)