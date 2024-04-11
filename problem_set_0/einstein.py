# This file contains a function to calculate the mass-energy equivalence (E = mc^2)


def e_mc():
    m_input = int(input("Enter the mass (m): "))

    c_squared = 300000000**2

    energy = m_input * c_squared

    print("Energy (E):", energy)


e_mc()
