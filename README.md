# Chemical Reaction Balancing Assignment

Welcome to the chemical reaction balancing assignment! Your task is to complete the provided Python project by filling in the missing code and writing the necessary imports. Follow the instructions carefully to ensure all components work together seamlessly.

---

## Instructions

### 1. Complete the Missing Functions in `string_utils.py`
In the file `string_utils.py`, you will find placeholders for two functions:  
- `split_before_uppercases`  
- `split_at_digit`  

These functions were part of last week's assignment. Use your previous implementation or write new ones based on the requirements:  
- **`split_before_uppercases`**: Splits a chemical formula (string) into a list of elements based on uppercase letters.  
- **`split_at_digit`**: Splits an element string into a tuple of (element name, count).  

---

### 2. Fill in Missing Lines in `count_atoms_in_molecule`
In the function `count_atoms_in_molecule` inside `string_utils.py`, fill in the missing lines. Here's the partially implemented function:

```python
def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    # fill in missing line to initiate a dictionary
    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        # fill in missing line to update the dictionary
    # return the dictionary
