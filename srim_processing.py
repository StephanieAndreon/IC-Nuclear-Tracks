import re
import mendeleev
import numpy as np
import matplotlib.pyplot as plt


def create_SR_IN_file(output_file_name, ion_element, target_data, target_elements, energy):
    file = open("SR_IN", "w")
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
        print(element)
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


def generate_energy_loss_curve(file, passo):
    f = open(file, "r")
    lines = f.readlines()
    ## Pular as linhas de cabeçalho do arquivo
    del lines[:4]
    list_s_eletronica = []
    list_dEdx = []
    for line in lines:
        ## Separar as colunas de energia
        energias = re.split(r'\s', line)
        s_eletronica = format_substituir_notacao_cientifica(energias[3])
        s_nuclear = format_substituir_notacao_cientifica(energias[5])
        list_s_eletronica.append(s_eletronica)
        list_dEdx.append(1/(s_eletronica+s_nuclear)*passo)

    list_s_eletronica = np.array(list_s_eletronica[::-1])
    list_dEdx = list_dEdx[::-1]

    plt.interactive(False)
    y = np.cumsum(list_dEdx)
    x = list_s_eletronica
    plt.plot(x, y, label='Energy loss')
    plt.ylabel('dE/dx')
    plt.xlabel('S_e')
    plt.title("Curva da perda de Energia")
    plt.legend()
    curve = plt.show(block=True)
    plt.interactive(False)

    return curve


def format_substituir_notacao_cientifica(string):
    numero, sinal, potencia = re.search('(.*)E(\+?\-?)(\d{2})', string).groups()
    if sinal == '+':
        valor = float(numero) * 10 ** (float(potencia))
    else:
        valor = float(numero) * 10 ** (-float(potencia))
    return valor


create_SR_IN_file(output_file_name="Alpha particles in CR-39",
                  ion_element="He",
                  target_data={"Estate": "0",
                               "Density": "1.32",
                               "Correction": "0"},
                  target_elements={"1": ["C", "12"],
                                   "2": ["H", "18"],
                                   "3": ["O", "7"]},
                  energy=[100, 10100, 100])

a = generate_energy_loss_curve("Alpha particles in CR-39", 100)
print(a)
