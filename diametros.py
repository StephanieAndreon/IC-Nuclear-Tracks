from math import *
#R_0: alcance do traco
R_0 = 10 * 10**(-6)
#V: Taxa de dissolucao
V = 1.6
#V_B: Taxa de dissolucao generalizada
V_B = 10**(-6)
theta = 1.22173
###### Formulas dos diametros #######
##### Diametro menor ##########
#Diametro menor na primeira fase de revelacao quimica:
def d1(altura, taxa, angulo):
    return (2 * altura * sqrt( (taxa * sin(angulo) - 1) / (taxa * sin(angulo) + 1) ))

#Diametro menor na segunda fase de revelacao quimica:
def d2(altura, taxa, angulo, alcance):
    x =  (alcance*(sin(angulo) - 1/taxa))
    y = (alcance*(sin(angulo) + 1/taxa))
    z = 2*altura - y
    r = 2*sqrt(x*z)
    return (r)
##### Diametro maior ######
#Diametro maior na primeira fase de revelacao quimica:
def D1(altura, taxa, angulo):
    return (2 * altura *(sqrt(taxa**2 -1)/(taxa*sin(angulo) + 1) ) )

#Diametro maior na segunda fase de revelacao quimica:
def D2(altura, taxa, angulo, alcance):
    return (1/2 * ((2 * altura *(sqrt(taxa**2 -1)/(taxa*sin(angulo) + 1) )) + (2 * sqrt( alcance * (sin(angulo) - 1/taxa ) * (2*altura - alcance*(sin(angulo) + 1/taxa)) ))) + cos(angulo)*(alcance - (altura*taxa/(taxa*sin(angulo) + 1))))

#Diametro maior na terceira fase de revelacao quimica:
def D3(altura, taxa, angulo, alcance):
    x =  (alcance*(sin(angulo) - 1/taxa))
    y = (alcance*(sin(angulo) + 1/taxa))
    z = 2*altura - y
    r = 2*sqrt(x*z)
    return (r)


for i in range(1, 21, 1):
    h1 = (R_0 / V) + R_0 * sin(theta)
    H1 = R_0 / V + R_0 * ((V * sin(theta) - 1) / (V - sin(theta) + cos(theta) * sqrt(V**2 -1)))
    H2 = R_0 / V + R_0 * ((V * sin(theta) - 1) / (V - sin(theta) - cos(theta) * sqrt(V**2 -1)))

    for t in range(10, 70, 10):
        h = V_B * t
        if (0 < h and h < h1):
            diametro_menor = d1(h, V, theta)
        if (h >= h1):
            diametro_menor = d2(h, V, theta, R_0)
        if (0 <= h and h < H1):
            diametro_maior = D1(h, V, theta)
        if (H1 <= h and h <= H2):
            diametro_maior = D2(h, V, theta, R_0)
        if (h <= H2):
            diametro_maior = D3(h, V, theta, R_0)
        if (t == 10):
            print(theta, diametro_menor, diametro_menor, t)
    theta = theta + 0.0174533
