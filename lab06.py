import matplotlib.pyplot as plt
import numpy as np
import os
#brain_image = plt.imread('image_1.jpg')
#plt.imshow(brain_image)
#plt.show()
#plt.clf()
#print(brain_image)
#print(brain_image.shape)
#print(brain_image[:, -1])
#plt.imshow(brain_image, cmap = "gray")
#plt.show()


#brain_image = 'image_1.jpg'

def center_col(brain_image):

    shape = brain_image.shape
    r, c = brain_image.shape
    colDiv = int(c / 2)
 #   print(r)
 #   print(c)
 #   print(colDiv)
    
    if c % 2 == 0:
        num = colDiv - 1
        centerCol = brain_image[:, num]
        return centerCol
    
    else:
        centerCol1 = brain_image[:, colDiv]
        return centerCol1

        
def middle_row(brain_image):

    shape = brain_image.shape
    r, c = brain_image.shape
    rowDiv = int(r/ 2)
    
    if r % 2 == 0:
        num = rowDiv - 1
        centerRow = brain_image[num, :]
        
        return centerRow
                    
    else:
        centerRow1 = brain_image[rowDiv, :]
        
        return centerRow1


def largest_intensity(brain_image):

    
    largestIntensity = np.max(brain_image)
    return largestIntensity
    
def smallest_intensity(brain_image):
    
    smallestIntensity = np.min(brain_image)
    return smallestIntensity



def is_8bit(brain_image):

    dataType = brain_image.dtype == np.dtype('uint8')
    return dataType

def simple_program(original_number):

    my_number = original_number

    if original_number < 0:
        my_number = abs(original_number)
    squareRoot = float(np.sqrt(my_number))
    #print(squareRoot)
    print('Your original number was %d and your new number is %.6f.' % (original_number, squareRoot))

def simple_program2(original_number):

    if original_number == 0:
        print('Your input is zero')

    elif original_number < 0:
        my_number = abs(original_number)
        sqrt_number = float(my_number ** 0.5)
        print("Your original number was %d" % original_number, end=" ")
        print("and was converted to: %d." % my_number)
        print("The square root of your new number is: %f." % sqrt_number)

    else:
        my_number = original_number / 2
        sqrt_number = my_number ** 0.5
        print("Your original number was %d" % original_number, end=" ")
        print("and it was divided by 2 to get: %f." % my_number)
        print("The square root of your new number is %f." % sqrt_number)

def score_to_grade(score):

    if score >= 85:
        return "A"
    elif score >= 72 and score < 85:
        return "B"
    elif score >= 65 and score < 72:
        return "C"
    elif score >= 50 and score < 65:
        return "D"
    else:
        return "F"

def retrieve_image():

    name = input('Enter the first and last name seperated by a space:  ')
    unchangedName = name
    name = name.replace(" ", "")
    name = name + ".jpg"
    #print(name)

    if os.path.isfile(name):
        print("Your request was for %s, here is the image I found for this request." % unchangedName)
        fig = plt.figure() 
        image = plt.imread(name)
        saved = plt.imshow(image, cmap="gray")
        fig.savefig('figure.jpg')
    else:
        default = plt.imread('Default.jpg') 
        print("Failed to find %s, here is the default image." % unchangedName)
        fig = plt.figure()
 #       image = plt.imread(default.jpg)
        saved = plt.imshow(default, cmap='gray')
        fig.savefig('figure.jpg') 
    


    


#a = np.array([[1, 2, 3, 5, 7, 2, 6, 7, 6],
#                        [4, 5, 6, 1, 4, 6, 7, 9, 2],
#                        [7, 8, 8, 4, 5, 9, 1, 3, 8],
#                        [3, 4, 1, 5, 7, 8, 1, 1, 1]])







#j = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#j = np.random.randint(0, 100, (5, 5))
#print(j)

#x = j[0]
#for i in range(1, j[:, :]):
#    if j[i] < x:
#        x = j[i]
#print('minimum:', x) 










