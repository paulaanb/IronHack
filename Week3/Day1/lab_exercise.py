#1. Import the NUMPY package under the name np and PANDAS as pd.
#2. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"

 
#3. Create a 5x2x3 3-dimensional array with all values equaling 1.

 
#4. Do a and b have the same size? How do you prove that in Python code?

 
#4. Identify the max, min, and mean values in a. Assign those values to variables "d_max", "d_min", and "d_mean"

 
#5. Now we want to label the values in a. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using np.empty.

 
#6. Populate the values in f.

#For each value in a, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
#If a value in a is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
#If a value equals to d_mean, assign 50 to the corresponding value in f.
#Assign 0 to the corresponding value(s) in f for d_min in d.
#Assign 100 to the corresponding value(s) in f for d_max in d.
#In the end, f should have only the following values: 0, 25, 50, 75, and 100.
#Note: you don't have to use Numpy in this question.

 
#Print a and f.

#Do you have your expected f?

#For instance, if your a is:

#array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
    [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
    [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],
   [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
    [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
    [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

#Your f should be:

#array([[[ 75.,  75.,  75.,  25.,  75.],
    [ 75.,  75.,  25.,  25.,  25.],
    [ 75.,  25.,  75.,  75.,  75.]],
   [[ 25.,  25.,  25.,  25., 100.],
    [ 75.,  75.,  75.,  75.,  75.],
    [ 25.,  75.,   0.,  75.,  75.]]])
#7. Create a Pandas DataFrame from the list of lists below. Each sublist should be represented as a row.

#matriz = [[53.1, 95.0, 67.5, 35.0, 78.4],
     [61.3, 40.8, 30.8, 37.8, 87.6],
     [20.6, 73.2, 44.2, 14.6, 91.8],
     [57.4, 0.1, 96.1, 4.2, 69.5],
     [83.6, 20.5, 85.4, 22.8, 35.9],
     [49.0, 69.0, 0.1, 31.8, 89.1],
     [23.3, 40.7, 95.0, 83.8, 26.9],
     [27.6, 26.4, 53.8, 88.8, 68.5],
     [96.6, 96.4, 53.4, 72.4, 50.1],
     [73.7, 39.0, 43.2, 81.6, 34.7]]
#8. Rename the data frame columns based on the names in the list below.

#colnames = ['Score_1', 'Score_2', 'Score_3', 'Score_4', 'Score_5']
#9. Create a subset of this data frame that contains only the Score 1, 3, and 5 columns.

 
#10. From the original data frame, calculate the average Score_3 value.

 
#11. Create a Pandas DataFrame from the dictionary of product orders below.

#orders = {'Description': ['LUNCH BAG APPLE DESIGN',
  'SET OF 60 VINTAGE LEAF CAKE CASES ',
  'RIBBON REEL STRIPES DESIGN ',
  'WORLD WAR 2 GLIDERS ASSTD DESIGNS',
  'PLAYING CARDS JUBILEE UNION JACK',
  'POPCORN HOLDER',
  'BOX OF VINTAGE ALPHABET BLOCKS',
  'PARTY BUNTING',
  'JAZZ HEARTS ADDRESS BOOK',
  'SET OF 4 SANTA PLACE SETTINGS'],
 'Quantity': [1, 24, 1, 2880, 2, 7, 1, 4, 10, 48],
 'UnitPrice': [1.65, 0.55, 1.65, 0.18, 1.25, 0.85, 11.95, 4.95, 0.19, 1.25],
 'Revenue': [1.65, 13.2, 1.65, 518.4, 2.5, 5.95, 11.95, 19.8, 1.9, 60.0]}

 
#12. Calculate the total quantity ordered and revenue generated from these orders.