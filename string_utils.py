


def split_before_uppercases(formula):
    if len(formula) == 0:
        return []
    start = 0
    list_of_elements = []
    for current in range(1, len(formula)):
        if formula[current].isupper():
            list_of_elements.append(formula[start:current])
            start = current
    list_of_elements.append(formula[start:])
    return list_of_elements

def split_at_digit(formula):
    for i in range(len(formula)):
        if formula[i].isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    atoms_count = {}
    for atom in split_before_uppercases(molecular_formula):
        atom_name, atom_count = split_at_digit(atom)
        atoms_count[atom_name] = atom_count
    return atoms_count

def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
