# from string_utils import parse_reaction, count_atoms_for_each_mol
# from equations_utils import build_equations, solve





from sympy import symbols, Eq
from sympy import solve as sympy_solve


ELEMENTS = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
    'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
    'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
    'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
    'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
    'Sb', 'I', 'Te', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd',
    'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb',
    'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
    'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
    'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm',
    'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
    'Rg', 'Cn', 'Uut', 'Uuq', 'Uup', 'Uuh', 'Uus', 'Uuo'
]







def generate_equation_for_element(compounds, coefficients, element):
    equation = 0
    for i, compound in enumerate(compounds):
        if element in compound:
            equation += coefficients[i] * compound[element]
    return equation



def build_equations(reactant_atoms, product_atoms):
    ## coefficients ##
    reactant_coefficients = list(symbols(f'a0:{len(reactant_atoms)}'))
    product_coefficients = list(symbols(f'b0:{len(product_atoms)}'))  # Ensure the last coefficient is 1
    product_coefficients = product_coefficients[:-1] + [1]

    ## equations ##
    equations = []
    for element in ELEMENTS:
        lhs = generate_equation_for_element(reactant_atoms, reactant_coefficients, element)
        rhs = generate_equation_for_element(product_atoms, product_coefficients, element)
        if lhs != 0 or rhs != 0:
            equations.append(Eq(lhs, rhs))

    return equations, reactant_coefficients + product_coefficients[:-1]


def solve(equations, coefficients):
    solution = sympy_solve(equations, coefficients)

    if len(solution) == len(coefficients):
        coefficient_values = list()
        for coefficient in coefficients:
            coefficient_values.append(float(solution[coefficient]))
        return coefficient_values





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



##############################################################

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







def balance_reaction(reaction): #"Fe2O3 + H2 -> Fe + H2O"

    # 1.parse reaction
    reactants, products = parse_reaction(reaction) # [""Fe2O3", "H2"], ["Fe", "H2O""]
    reactant_atoms = count_atoms_for_each_mol(reactants) # [{"Fe":2, "O":1}, {"H":2}]
    product_atoms = count_atoms_for_each_mol(products)

    # 2.build equation and solve
    equations, coefficients = build_equations(reactant_atoms, product_atoms)
    coefficients = solve(equations, coefficients) + [1]

    return coefficients # [1/3, 1, 2/3, 1]


# import numpy
# from sympy import symbols, Eq, solve



# def my_func(a):
#     arr = numpy.array([1])
#     x = symbols('x')
#     solution = solve(Eq(x**2 - 4, 0), x)
#     return a+1
