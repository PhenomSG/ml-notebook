import pandas as pd  
import numpy as np  

data = pd.read_csv("2.csv")  
print(data)  

# attributes and target
d = np.array(data)[:,:-1] 
'''
: (before the comma): Selects all rows.
:-1 (after the comma): Selects all columns except the last one
'''
print("The attributes are: ",d) 
target = np.array(data)[:,-1]  
'''
: (before the comma): Selects all rows.
-1 (after the comma): Selects only the last column.
'''
print("The target is: ",target)  

def find_S(c, target): 
    for i, val in enumerate(target): 
        if val == "Yes": 
            specific_hypothesis = c[i].copy() 
            break 

    for i, val in enumerate(c): 
        if target[i] == "Yes": 
            for x in range(len(specific_hypothesis)): 
                if val[x] != specific_hypothesis[x]: 
                    specific_hypothesis[x] = '?' 
                else: 
                    pass 
    return specific_hypothesis

print("The final hypothesis is:",find_S(d,target))
