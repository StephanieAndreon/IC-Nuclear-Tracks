from cmath import *
#R_0: R_0 do traco
R_0 = 0.00001
#V: V de dissolucao
V = 1.6
#V_B: V de dissolucao generalizada
V_B = 0.000001
h = V_B * 70
theta = 1.22173
#H1 = 1.0
#H1 = R_0/V + R_0*(V * sin(theta) - 1)/ (V - sin(theta) - cos(theta)*sqrt(V**2 -1))
#for i in range(1, 21, 1):
#    H1 = R_0 / V + R_0 * ((V * sin(theta) - 1) / (V - sin(theta) + cos(theta) * sqrt(V**2 -1)))
#    float(H1)
#    print(H1)
#    theta = theta + 0.0174533
#def d2(altura, V, theta, R_0):
#    return (2 * sqrt( R_0 * (sin(theta) - 1/V ) * (2*altura - R_0*(sin(theta) + 1/V)) ))
#a = d2(h, V, theta, R_0)


#a =  (R_0*(sin(theta) - 1/V))
#c = sin(theta) + 1/V
#b = 2*h - R_0*c
#print(a)
#print(b)
#print(c)
#D3 = 2*sqrt(a*b)
#print(D3)


x =  (R_0*(sin(theta) - 1/V))
y = (R_0*(sin(theta) + 1/V))
z = 2*h - y
r = 2*sqrt(x*z)
print(x)
print(y)
print(z)
print(r)
