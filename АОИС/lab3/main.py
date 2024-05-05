from true_table import *
from calculation_tabular_method import *
from karno_map import *
from params_replace import *

def main():
        # (!(((!x1)+(!x2))*(!((!x2)*x3))))
        formula = input("Input formula: ")

        if not check_input(replece_params(formula)):
            raise Exception('Invalid input!')

        table, variables = true_table(replece_params(formula))

        print("_" * 60)

        SDNF = create_sdnf(table, variables)
        SDNF = SDNF.replace('-', '!')
        print("SDNF:" + dereplece_params(SDNF))
        SKNF = create_sknf(table, variables)
        SKNF = SKNF.replace('-', '!')
        print("SKNF:" + dereplece_params(SKNF))
        SDNF = [i.split("*") for i in SDNF[1:-1].split(")+(")]
        SKNF = [i.split("+") for i in SKNF[1:-1].split(")*(")]

        dnf = gluing(SDNF)
        knf = gluing(SKNF)

        print("\nCalculation-tabular method:")
        mdnf = calculation_tabular_method(dnf, SDNF, "sdnf")
        print_mdnf(mdnf)
        mknf = calculation_tabular_method(knf, SKNF, "sknf")
        print_mknf(mknf)

        print("\nCalculation method:")
        print("Result of gluing:")
        print_dnf(dnf)
        print_knf(knf)
        calculation_method(dnf, "dnf")
        calculation_method(knf, "knf")
        print_mdnf(mdnf)
        print_mknf(mknf)

        print("\nTabular method:")
        table_res = []
        for i in table.values():
            LAST = len(i) - 1
            table_res.append(int(i[LAST]))

        str(table_method(table_res, mdnf, mknf))



if __name__ == '__main__':
    main()