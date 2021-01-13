#final exam study guide

import numpy as np

degrees = 30
#print(np.sin(np.deg2rad(degrees)))

x = 4
y = 4

#print(np.logical_xor(x > 5, y <10))

my_age = 24

ftemp = 55
ctemp = (5/9) * (ftemp - 32)
#print(ctemp)

A = 55
x = 15
c = (A/x) * np.sqrt((2/(np.pi * np.e)))
#print(c)

weight = 65
n = 2

mat = np.random.uniform(0, 2, (3, 5))
mat = np.delete(mat, 2, axis = 0)
#print(mat)

a  = np.array([[2, 1, 3], [1, 5, 6], [3, 6, 0]])
c = np.array([[3, 2, 5], [4, 1, 2]])
#print(a)
#print(c)


h = np.array([[1, 4]])
k = np.array([[2], [3]])
#print(h)
#print(k)


#usr = input("please enter the length: ")
#huy = input("is that in f(eet) or m(eteres)?: ")



Mat = np.random.randint(0, 5, (2, 3))
#print(Mat)


get = np.random.randint(0, 5, (2, 4, 3))
#print(get)


vec = np.random.randint(-10, 11, (1, 5))
#print(vec)


jj = np.array([[1, 2, 3, 4, 5], [6, 7, 22, 9, 1], [4, 3, 7, 5, 8]])
print(jj)
r, c = jj.shape
j = []

for i in range(r):
    print(np.min(jj[i , :]))

def echostring():
    enter = input("enter your sting: ")
    print("your string was: '%s' " % enter)


def mph_to_mps(x):
    x *= 5280
    meters = x * .3048
    distance = meters / 3600
    print(distance)

def velocity(pt, ps):
    v = 1.016 * np.sqrt(pt - ps)
    print(v)
    
    
def divide_by_4(y):
    if y % 4 == 0:
        print('true')
    else:
        print('false')


def flowrate():
    x = input('Enter the flow in m^3/s: ')
    x = float(x)
    y = x / .028

    print("A flow rate of %.3f cubic meters per sec" % x)
    print("is equivilent to %.3f cubic feet per second" % y)
    

def is_pythagorean_triple(a, b, c):
    
    if a**2 + b**2 == c**2:
        print('true')
    else:
        print('false') 


def vecount(x):
    vec = []
    y = x + 5
    for i in range(x, y+1, 1):
        vec.append(i)
    print(vec)


def cost_n(n):
    C = ((5*n**2) - (44*100) + 11)
    print('The cost for %d units will be $%.2f' % (n, C))
    
def mfg_cost():
    n = input('Enter the number of units: ')
    n = int(n)
    cost_n(n)



def fuck():
    h = int(input("please enter your re number: "))
    if h <= 2300:
        print('Laminar region')
    elif h <= 4000:
        print('Transition region')
    else:
        print('Turbulent region')
        
        
def detection():
    rf = np.random.randint(0, 13)
    print(rf)

    if rf <= 0:
        print('no wind')
    elif rf <= 6:
        print('breaze')
    elif rf <= 9:
        print('gale')
    elif rf <= 11:
        print('storm')
    else:
        print('hurricane')



def shit():
    n = int(input('please enter your value for n: '))
    for i in range(n):
        print('i love this stuff')
        
        
def sum1(n):
    x = 0
    for i in range(1, n + 1, 2):
        x += i
    print(x)


def table(n):

    for i in range(1, n +1):
        print(' ')
        for c in range(1, i+1):
            rows = c * i
            print('%d' % rows, end=' ')


def damn():
    vit = [5.5, 11, 3.45]
    x = 1
    for i in range(len(vit)):   
        print('Element %d is %.2f' % (x, vit[i]))
        x +=1

def ss():
    n = 3
    x = np.zeros((n, n))
    y = np.zeros((n, n))
    for i in range(n):
        x[:, i] = i
        y[i, :] = i
    print(x)
    print(y)




def dd(n):

    for i in range( 1, n+1):
        print(' ')
        for x in range(1, i +1):
            rows = i *x
            print('%d' % rows, end=' ')


def what():
    k = []
    g = float(input("please enter the threshold: "))
    h = int(input("enter the number number of samples: "))

    for i in range(h):
        d = float(input("enter the input: "))
        if d > g:
            k.append(d)
    s = np.average(k)
    print('the average of the %d valid data samples is %.2f volts' % (len(k), s))
          


def hh(n):

    for i in range(1, n+1):
        print(' ')
        for k in range(1, i+1):
            rows = i * k
            print('%d' % rows, end=' ')


def carnot(tc, th):
    tc = abs(tc)
    th = abs(th)
    if tc <= 0 or th <= 0:
        print('error..... must be greater than 0')
        
    if th < tc:
        tc, th = th, tc

    n = 1 - (tc/th)
    print('eta = %.3f' % n)



def rr(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan(y/x)
    return r, theta


def ff(dd):
    deg = int(dd)
    minutes = (60*(dd%1))
    seconds = (60*(dd%1))
    return deg, minutes, seconds


def kk():
    z = input('enter your values: ')
    print(z)






















