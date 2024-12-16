import pandas as pd
import numpy as np

# Reading the dataset
data = pd.read_csv('enjoySport.csv')  
print("Dataset:")
print(data)

# Extracting the concepts (input features) and target (output label)
concepts = np.array(data.iloc[:, 0:-1])  # All columns except the last one (features)
print("\nConcepts (Input Features):")
print(concepts)

target = np.array(data.iloc[:, -1])  # The last column (target)
print("\nTarget (Class Labels):")
print(target)

# Candidate Elimination algorithm
def learn(concepts, target):
    specific_h = concepts[0].copy()  # Initialize specific hypothesis with the first positive example
    print("\nInitialization of specific_h and general_h")
    print("\nSpecific hypothesis: ", specific_h)
    
    # Initialize general hypothesis with "?" for each feature
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("\nGeneric hypothesis: ", general_h)
    
    for i, h in enumerate(concepts):
        print("\nInstance", i+1, "is", h)
        
        if target[i] == "yes":  # Positive example
            print("Instance is Positive")
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'  # Generalize the specific hypothesis if needed
                    general_h[x][x] = '?'  # Generalize the general hypothesis as well
        elif target[i] == "no":  # Negative example
            print("Instance is Negative")
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]  # Remove the specific case from the general hypothesis
                else:
                    general_h[x][x] = '?'  # Otherwise, retain the "?" in the general hypothesis
        
        print("Specific hypothesis after", i+1, "Instance is", specific_h)
        print("Generic hypothesis after", i+1, "Instance is", general_h)
        print("\n")
    
    # Remove the irrelevant general hypotheses that are just full of "?"
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])

    return specific_h, general_h

# Running the Candidate Elimination Algorithm
s_final, g_final = learn(concepts, target)

# Displaying the final hypotheses
print("Final Specific Hypothesis: ", s_final, sep="\n")
print("Final General Hypothesis: ", g_final, sep="\n")
