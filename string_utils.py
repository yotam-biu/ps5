


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
    """Counts the number of each atom in a molecular formula."""
    atoms_count = {}
    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        atoms_count[atom_name] = atom_count
    return atoms_count

def parse_chemical_reaction(reaction_equation):
    """Parses a chemical reaction equation into reactants and products."""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Counts the atoms in a list of molecular formulas."""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
