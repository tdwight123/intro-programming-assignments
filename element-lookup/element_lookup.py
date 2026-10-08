"""
Tim Dwight
CS 1210
Programming Assignment
"""


ELEMENTS = (None, "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron",
            "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium",
            "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur",
            "Chlorine", "Argon", "Potassium", "Calcium", "Scandium",
            "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt",
            "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic",
            "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium",
            "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
            "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium",
            "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium",
            "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
            "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium",
            "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
            "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium",
            "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead",
            "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium",
            "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium",
            "Plutonium", "Americium", "Curium", "Berkelium", "Californium",
            "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium",
            "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium",
            "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium",
            "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine",
            "Oganesson")


if __name__ == '__main__':
    choice = input('Do you wish to look up by element name or atomic number? '
                   'e/a: ')
    if choice == 'e':
        element = input('Enter the name of the element: ').capitalize()
        if element in ELEMENTS:
            atomic_number = ELEMENTS.index(element)
            print(f'The atomic number of {element} is '
                  f'{(atomic_number)}')
        else:
            print(f'Error. {element} does not exist!')
    elif choice == 'a':
        atomic_number = int(input('Enter the atomic number of the element: '))
        if 1 <= atomic_number <= len(ELEMENTS) - 1:
            print(f'The element with atomic number {atomic_number} '
                  f'is {ELEMENTS[atomic_number]}')
        else:
            print('Invalid atomic number supplied.')
    else:
        print('Invalid choice.')
