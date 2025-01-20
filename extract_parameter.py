
unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}
}



def extract_parameter(unit_operations_data, unit_name, parameter_name, index):
    try:
        value = unit_operations_data[unit_name][parameter_name][index] #accessing the values directly using keys
        return f"{unit_name}_{parameter_name}_{value}" #if the input aligns with the dictionary entry, the output will be printed in that format
    except (KeyError,IndexError) as e: #if the input(s) does not align with the dictionary a produces an error, "invalid input" will be printed
        return "Invalid input"

print(extract_parameter(unit_operations_data, "distillation_column", "temperature", 1)) 
#this will search the dictionary "unit_operations_data" for the unit name "distillation_column" and the parameter "temperature" for said unit, from said parameter, it will pull the second index from the list
print(extract_parameter(unit_operations_data, "heat_exchanger", "temperature", 1))
#because the heat exchanger does not have a "temperature" parameter, "invalid input" is printed

# source for try and except method: https://www.w3schools.com/python/python_try_except.asp
# source for help with nested dictionaries: https://www.w3schools.com/python/python_dictionaries_nested.asp
