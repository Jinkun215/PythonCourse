CONST_FREEZING_TEMP = 0
CONST_VAPORIZING_TEMP = 100

def water_state (temperature_arg):
    if (temperature_arg <= CONST_FREEZING_TEMP):
        return "Solid"
    elif (temperature_arg >= CONST_VAPORIZING_TEMP):
        return "Gas"
    else:
        return "Liquid"

if (__name__ == "__main__"):
    print("Please use this file as an import")