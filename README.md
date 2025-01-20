# 545hw1
Submission for CHEM E 545 HW 1

## Question 1
Approach:
* Read through the problem and noted what it asked me to do
* I need a function that will extract entries from a nested dictionary and return them in a specified format
* Using the hint, I looked up how to use try and except method 
* Try and accept allows me to obtain my desired output and if there's an error it will return a specific message "invalid input"
* So "try" will access the values directly from the dictionary and then format them as instructed
* "accept" will return "Invalid input" if there is a KeyError and/or an IndexError

## Question 2
Approach:
* Read through the problem and noted what it asked me to do
* I need a function that takes a list containing compound names and concentrations, matches it up with a dictionary of compounds and their molecular weights, then multiplies the molecular weights by concentration to get the weight in the solution, and returns a modified list with the compound name, concentration, and weight
* If the list contains a compound not found in the dictionary, its entry in the modified list will return "unknown"
* Because the given list contains two pieces of info for each item, I need a way to separate them so I can use the concentration in a calculation

* I looked up a method to achieve this, and found that I can use "split" to separate the compound name and its concentration

* To use the concentration in a calculation, I needed to turn it into a float number, so I did that next
* I then used an if else statement to set up my desired output
* "If" the compound is found in the molecular_weights dictionary, then multiply the molecular weight by the concentration to get weight in the solution and add it to the modified list and then return said list
* "Else" add "unknown"

