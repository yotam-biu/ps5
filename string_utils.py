


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

def parse_compound(compound):
    compound_elements = {}
    for element in split_before_uppercases(compound):
        element_name, element_value = split_at_digit(element)
        compound_elements[element_name] = element_value
    return compound_elements

def parse_reaction(reaction_str):
    """Converts the reaction string into reactants and products list."""
    reaction_str = reaction_str.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_str.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_for_each_mol(mols):
    atoms = []
    for mol in mols:
        atoms.append(parse_compound(mol))
    return atoms
