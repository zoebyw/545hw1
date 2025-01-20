molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052
}

solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']


def calculate_solution_weights(molecular_weights,solutions_needed):
    result = [] #creating blank list for results
    for solution in solutions_needed: # looking among the entries in the solutions_needed list
        compound, concentration = solution.split('-') # splitting the solutions_needed list into sublists with the compound name and desired concentration
        concentration = float(concentration.replace('M','')) # taking the concentration from solutions_needed and turning it into a float number that can be multiplied by molecular_weight later on
                                                            # this is also getting rid of the unit 'M'
        if compound in molecular_weights: 
            molecular_weight = molecular_weights[compound] #accessing value from dictionary using key
            weight = molecular_weight * concentration #calculating weight of compound in 1 L solution
            result.append(f"{compound}-{concentration}M-{weight:.2f}g") # formatting the return function, including units and rounding the weight to two decimal places
        else:
            result.append("unknown") #will return "unknown" if chemical compound not in molecular_weights
    return result
print(calculate_solution_weights(molecular_weights,solutions_needed))

# help with split and float: https://www.geeksforgeeks.org/python-string-split/#
# help with append: https://www.w3schools.com/python/ref_list_append.asp
