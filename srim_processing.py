import re
import mendeleev
import numpy as np
import matplotlib.pyplot as plt


def create_SR_IN_file(output_file_name, ion_element, target_data, target_elements, energy):
    file = open("./SRIM_files/SR.IN", "w")
    file.write(
        '---Stopping/Range Input Data (Number-format: Period = Decimal Point) \n'
        '---Output File Name\n'
        f'"{output_file_name}"\n'
        '---Ion(Z), Ion Mass(u)\n'
        f'{mendeleev.element(ion_element).atomic_number}       {mendeleev.element(ion_element).mass}\n'
        '---Target Data: (Solid=0,Gas=1), Density(g/cm3), Compound Corr.\n'
        f'{target_data.get("Estate")}     {target_data.get("Density")}        {target_data.get("Correction")}\n'
        '---Number of Target Elements\n'
        f'{len(target_elements)}\n'
        '---Target Elements: (Z), Target name, Stoich, Target Mass(u)\n')
    for element in target_elements:
        input_element = target_elements.get(element)[0]
        stoich = target_elements.get(element)[1]
        file.write(
            f'{mendeleev.element(input_element).atomic_number}       "{mendeleev.element(input_element).name}"       {stoich}       {mendeleev.element(input_element).mass}\n')
    file.write(
        '---Output Stopping Units (1-8)\n'
        '3\n'
        '---Ion Energy : E-Min(keV), E-Max(keV)\n'
        '0    0\n')
    for i in range(energy[0], energy[1], energy[2]):
        file.write(f'{i}\n'
                   f'0')
    file.close()


def generate_energy_loss_curve(file, step=0.1, save_figure=False):
    """"
     Step must be in Mev
    """
    f = open(file, "r")
    lines = f.readlines()

    ## Delete header lines
    del lines[:4]

    list_eletronic_stopping_power = []
    list_del_track_lenght = []

    for line in lines[::-1]:
        ## Split energy columns
        energy = re.split(r'\s', line)

        eletronic_stopping_power = replace_scientific_notation(energy[3])
        nuclear_stopping_power = replace_scientific_notation(energy[5])

        del_track_lenght = 1 / (eletronic_stopping_power + nuclear_stopping_power) * step  ## unit in mm

        list_eletronic_stopping_power.append(eletronic_stopping_power)
        list_del_track_lenght.append(del_track_lenght)

    list_eletronic_stopping_power = np.array(list_eletronic_stopping_power)

    plt.interactive(False)
    x = np.cumsum(list_del_track_lenght)
    print(x)
    y = list_eletronic_stopping_power

    legend = re.search(r'\.\/SRIM_files\/(.*)', file)
    if legend:
        legend = f'Energy loss of {legend.group(1)}'
    #plt.legend(f'{legend}',)

    plt.plot(x, y)
    plt.xlabel('Track lenght (mm)')
    plt.ylabel('Stopping Power (Mev/mm)')
    plt.yscale('log')
    plt.title(f'Energy loss of {legend}')
    plt.tight_layout(pad=2)

    if save_figure:
        plt.savefig(f'./images/Energy_loss_{legend.replace(" ", "_")}.png')

    else:
        plt.show()


def replace_scientific_notation(string):
    numero, sinal, potencia = re.search('(.*)E(\+?\-?)(\d{2})', string).groups()
    if sinal == '+':
        valor = float(numero) * 10 ** (float(potencia))
    else:
        valor = float(numero) * 10 ** (-float(potencia))
    return valor


# create_SR_IN_file(output_file_name="Alpha particles in CR-39", ion_element="He", energy=[100, 10100, 100]
#                   target_data={"Estate": "0", "Density": "1.32", "Correction": "0"},
#                   target_elements={"1": ["C", "12"], "2": ["H", "18"], "3": ["O", "7"]})

generate_energy_loss_curve(file="./SRIM_files/Alpha particles in CR-39", step=0.1, save_figure=1)
