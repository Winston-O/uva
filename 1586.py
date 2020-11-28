
test_no = int(input())
std_weight = {"C":12.01, "H":1.008, "O":16.00, "N":14.01}
for n in range (test_no):
    item = input()
    molar_mass = 0

    for i in range (len(item)):
        atom_no = 0

        if item[i].isalpha():
            atom_name = item[i]
            for j in range (i+1, len(item)):
                if item[j].isdigit():
                    atom_no = atom_no * 10 + int(item[j])
                else:
                    break

            if atom_no == 0:
                atom_no = 1

            molar_mass += std_weight.get(atom_name) * atom_no

    print("{:.3f}".format(molar_mass))