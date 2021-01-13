import numpy as np
import random 

#This is number 7 on the homework 5
def approx_e_inv():
    n = 1
    apr = (1-(1/n))**n
    dif = (1/(np.e)) - apr
    inv_e = (1/np.exp(1))
    

    while dif > 0.0001:
        n += 1
        apr = (1-(1/n))**n
        dif = (1/(np.e)) - apr
    print(" 1/e = %4f, approx = %4f, n = %d" % (inv_e, apr, n))
        
#Home work number 1

def random_numbers():
    x = random.uniform(0, 100)
    print(x)

def characters():

    a = ord('a')
    print(a)

    b = chr(88)
    print(b)

def trig():

    degrees = 30
    print(np.sin(np.deg2rad(degrees)))
    
#when it comes to upper case and lower case UPPER always comes first 

def logical():

    x = 6
    y = 9
    fact = np.logical_xor(x > 5, y<10) #this is the magic key
    print(fact)


x = list(range(5, 10, 2))
#print(x)
x = np.random.uniform(0, 1, (3, 5))
x = np.delete(x, 2, axis=0)  # deleting rows and columns


j = np.array([[1, 2, 3, 4, 5],
                       [3, 4, 5, 6, 7],
                       [2, 5, 6, 8, 9]])


ex = np.array([[1, 4],
                          [3, 2]])

ex1 = np.array([[3, 2, 5],
                            [4, 1, 2]])


ex2 = np.array([[2, 1, 3],
                            [1, 5, 6],
                            [3, 6, 0]])

ex3 = np.array([[1, 4]])

ex4 = np.array([[2],
                            [3]]) 



vec4 = np.zeros((2, 4, 1))
vec5 = np.ones((2, 4, 1))
vec6 = 2 * np.ones((2, 4, 1))

def haha():
    vec = []
    n = int(input("please enter your value for n: "))
    for i in range(1, n+1, 2):
        vec.append(i)
    print(np.prod(vec))


def sums_steps4(n):

    for i in range(1, n+1, 2):
        i += n
        print(i)
    
def what_the():
    vec = []
    n = int(input("please enter your value for n: "))

    for i in range(1, n+1):
        vec.append(i)
    for j in range(1, n+1):
        print(" ")

        for h in range(1, j+1):
            tableRows = h * j
            print(" %3d" % tableRows, end=" ")
            


def new_game():

    keep_playing = 'y'
    random = np.random.randint(1, 101)
    while keep_playing == 'y':
        
        guess = int(input("Please enter your guessing number: "))

        if guess == random:
            print("correct")
        elif guess < random:
            print("Too low")
        else:
            print("Too high") 

        
        
        







    
