'''
Numpy: basics , array, functions, constants, formulas , random
@anishchapagain : github
'''
import numpy as np

a=np.arange(10)
a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a.dtype
dtype('int32')

a.shape
(10,)

a.ndim
1
z=np.zeros((3,6))
z
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])
	   
ez=np.empty((3,6))
ez
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])
	   
ez+2
array([[ 2.,  2.,  2.,  2.,  2.,  2.],
       [ 2.,  2.,  2.,  2.,  2.,  2.],
       [ 2.,  2.,  2.,  2.,  2.,  2.]])
	   
ez*1.25
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])
	   
ez+z
array([[ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.]])
	   
z.shape
(3, 6)

z.ndim
2

a=np.array(60)
a
array(60)

a=np.array([12,34,45],dtype=np.int32)

a
array([12, 34, 45])

a=np.arange(10)
a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

a[2]
2

a[6]
6

a[2:6]
array([2, 3, 4, 5])

a[0]
0

a[1]
1

len(a)
10

a=np.array([[1,23,45],[56,6,7],[78,34,25]])


a
array([[ 1, 23, 45],
       [56,  6,  7],
       [78, 34, 25]])
	   
a.ndim
2

a.shape
(3, 3)

a[1]
array([56,  6,  7])
a[1][2]
7
a+5
array([[ 6, 28, 50],
       [61, 11, 12],
       [83, 39, 30]])
a
array([[ 1, 23, 45],
       [56,  6,  7],
       [78, 34, 25]])

a[a<10]
array([1, 6, 7])

[a<40]
[array([[ True,  True, False],
       [False,  True,  True],
       [False,  True,  True]], dtype=bool)]
	   
a[a<40]
array([ 1, 23,  6,  7, 34, 25])

a[1][a[1]<40]
array([6, 7])

arr= np.arange(15)

arr
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

arr= np.arange(15).reshape((3,5))

arr
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

np.sqrt(arr)
array([[ 0.        ,  1.        ,  1.41421356,  1.73205081,  2.        ],
       [ 2.23606798,  2.44948974,  2.64575131,  2.82842712,  3.        ],
       [ 3.16227766,  3.31662479,  3.46410162,  3.60555128,  3.74165739]])
	   

arr= np.arange(15).reshape((3,5))
arr
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
	   

np.where(arr>0,2,arr)
array([[0, 2, 2, 2, 2],
       [2, 2, 2, 2, 2],
       [2, 2, 2, 2, 2]])
	   
np.where(arr<=9,2,arr)
array([[ 2,  2,  2,  2,  2],
       [ 2,  2,  2,  2,  2],
       [10, 11, 12, 13, 14]])
	   
arr= np.arange(15)

np.subtract(arr,2)
array([-2, -1,  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])

np.sum(arr)
105

arr
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

np.cumsum(arr)
array([  0,   1,   3,   6,  10,  15,  21,  28,  36,  45,  55,  66,  78,
        91, 105], dtype=int32)
		
np.cumprod(arr)
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int32)

np.argmin(arr)
0

np.argmax(arr)
14

arr= np.arange(1,15)

arr
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

np.cumsum(arr)
array([  1,   3,   6,  10,  15,  21,  28,  36,  45,  55,  66,  78,  91, 105], dtype=int32)

np.cumprod(arr)
array([         1,          2,          6,         24,        120,
              720,       5040,      40320,     362880,    3628800,
         39916800,  479001600, 1932053504, 1278945280], dtype=int32)
		 
np.mean(arr)
7.5

np.std(arr)
4.0311288741492746

np.var(arr)
16.25
a = np.random.normal()
a
1.5794758066172583

a = np.random.normal((3,5))
a
array([ 2.42742712,  4.62765375])

a = np.random.normal((3,5,20))

a
array([  3.23114208,   4.70806791,  19.96316946])

a = np.random.randn(3,5)
a
array([[-1.22866385,  1.55440051,  0.07371914,  1.00509888,  0.43755076],
       [ 1.18293543, -0.8672048 , -1.62060862,  2.10759922, -0.59599103],
       [ 0.54911946, -0.21967613,  0.93047577,  1.16448085, -1.84565694]])
	   
a = np.random.randn(3,5,9)

a
array([[[  1.06439127e+00,  -1.05256102e+00,  -3.67816994e-01,
          -4.71103621e-01,   1.55132269e+00,  -1.43065691e+00,
          -5.00506157e-01,   1.02764923e+00,  -2.43005181e-01],
        [  1.75964426e-01,  -1.40742012e+00,  -1.40817056e-01,
          -4.10432956e-01,   8.28122841e-01,  -2.33610293e-01,
          -4.11819935e-01,   7.43812653e-01,   4.98330173e-01],
        [  1.72021838e-01,  -9.79224170e-01,   1.31532734e-01,
           1.12820974e-01,  -1.24142761e+00,   2.81355380e-02,
          -8.18864904e-01,   1.80005702e+00,   1.18358557e-01],
        [ -3.39378222e-01,  -5.54821251e-01,   1.38479598e+00,
          -1.05004832e+00,   7.84942114e-01,  -5.21436312e-03,
          -6.66828624e-01,  -6.25547131e-01,  -1.82862889e-02],
        [ -5.97043784e-01,  -3.92613317e-01,  -1.43432051e+00,
           9.83581660e-01,   1.69303835e+00,   1.32565538e-01,
          -5.71573487e-02,   1.19100226e+00,  -4.03722882e-01]],

       [[  3.62781135e-01,  -3.46514516e-01,  -9.12767366e-01,
           7.95806686e-01,  -7.29221156e-01,  -5.38002739e-02,
           1.09739737e+00,   9.90071685e-01,   1.02286060e+00],
        [  1.39471597e-01,  -2.91196544e-01,  -3.82779612e-01,
          -5.97075898e-01,   5.37255707e-01,  -7.74050902e-01,
          -8.23344459e-01,   1.30415493e+00,  -9.95970960e-01],
        [ -5.08759822e-01,   7.74345847e-01,   5.17004922e-01,
          -9.85345859e-01,  -7.59110983e-04,  -8.12365535e-01,
          -1.03427545e+00,  -8.51428863e-01,  -2.33342855e-01],
        [  1.50644006e+00,  -7.85244765e-02,  -2.37026638e-01,
           8.84143875e-02,  -3.19628714e-02,  -5.24821675e-01,
           5.51116403e-01,   9.20911806e-03,  -1.16066004e+00],
        [ -2.83899114e-01,  -2.27745674e-02,  -7.09368490e-01,
           1.22243241e+00,  -1.38323468e+00,   4.95949374e-01,
           9.58293791e-01,  -2.07256676e+00,  -6.29504338e-01]],

       [[  3.04279833e-01,  -2.78164418e-01,   9.92913906e-01,
          -1.00789231e+00,   6.77568594e-01,  -1.93805249e+00,
          -9.71978019e-01,  -1.13906504e+00,  -8.47694001e-01],
        [  3.51055140e-01,  -1.11699391e+00,   6.54579649e-01,
          -1.26872678e+00,  -3.22407369e-01,  -1.21363359e+00,
           7.45605499e-01,  -1.05428502e+00,   1.33242557e+00],
        [  5.16830913e-01,   4.62897426e-01,  -1.23577397e+00,
           7.49249378e-01,   8.79861856e-01,   3.96833078e-01,
           3.77722202e-01,   1.39843485e+00,  -4.23299965e-01],
        [ -7.09069067e-01,   1.78868578e-01,   3.13934537e-01,
           1.46039315e-01,  -1.54809466e+00,   6.03555578e-01,
           4.31547084e-01,   5.93540370e-01,   9.27892813e-01],
        [  5.89336710e-01,  -2.80575108e-01,  -7.74052169e-01,
          -4.94364079e-02,  -1.10456533e-01,   1.20607718e+00,
           4.51830641e-01,   7.28704161e-01,  -5.35807165e-02]]])
a = np.random.normal(size=(2,2))

a
array([[-0.45906953, -1.61453208],
       [ 0.69222822, -0.89320195]])
	   
a.ravel()
array([-0.45906953, -1.61453208,  0.69222822, -0.89320195])

a.T
array([[-0.45906953,  0.69222822],
       [-1.61453208, -0.89320195]])
	   
a.reshape(2,2)
array([[-0.45906953, -1.61453208],
       [ 0.69222822, -0.89320195]])
	   
a.reshape(4,1)
array([[-0.45906953],
       [-1.61453208],
       [ 0.69222822],
       [-0.89320195]])



arr=np.arange(3)
arr
array([0, 1, 2])

arr.repeat(3)
array([0, 0, 0, 1, 1, 1, 2, 2, 2])

np.tile(arr,3)
array([0, 1, 2, 0, 1, 2, 0, 1, 2])

np.tile(arr,2)
array([0, 1, 2, 0, 1, 2])

arr
array([0, 1, 2])

np.add(arr,2)
array([2, 3, 4])

arr
array([0, 1, 2])

np.add.reduce(arr)
3

arr = np.arange(15).reshape(3,5)

arr
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
arr*3
array([[ 0,  3,  6,  9, 12],
       [15, 18, 21, 24, 27],
       [30, 33, 36, 39, 42]])
arr+2
array([[ 2,  3,  4,  5,  6],
       [ 7,  8,  9, 10, 11],
       [12, 13, 14, 15, 16]])
	   
arr.sum()
105
arr.cumsum()
array([  0,   1,   3,   6,  10,  15,  21,  28,  36,  45,  55,  66,  78,
        91, 105], dtype=int32)
		

import matplotlib.pyplot as plt
mu,sigma=2,0.5
v = np.random.normal(mu,sigma,10000)
v
array([ 2.09324104,  1.50920066,  2.76869606, ...,  2.1439366 ,
        1.62730985,  2.44557127])
plt.hist(v,bins=50,normed=1)
(array([ 0.00135675,  0.        ,  0.0027135 ,  0.0027135 ,  0.0027135 ,
        0.00407025,  0.01356749,  0.01085399,  0.01492424,  0.02713498,
        0.04341597,  0.05426996,  0.07597794,  0.11668041,  0.15602613,
        0.21300958,  0.22657707,  0.29170102,  0.33104674,  0.43687316,
        0.50064036,  0.54541307,  0.637672  ,  0.7041527 ,  0.74485516,
        0.73807142,  0.79505487,  0.79369813,  0.76113615,  0.69465545,
        0.69465545,  0.632245  ,  0.59696953,  0.54134282,  0.4409434 ,
        0.3798897 ,  0.32426299,  0.24557156,  0.17773411,  0.16823687,
        0.1221074 ,  0.10989666,  0.06241045,  0.03798897,  0.03798897,
        0.02035123,  0.01899449,  0.00678374,  0.00407025,  0.00407025]), array([  9.88472803e-04,   7.46940772e-02,   1.48399682e-01,
         2.22105286e-01,   2.95810890e-01,   3.69516495e-01,
         4.43222099e-01,   5.16927703e-01,   5.90633308e-01,
         6.64338912e-01,   7.38044516e-01,   8.11750121e-01,
         8.85455725e-01,   9.59161329e-01,   1.03286693e+00,
         1.10657254e+00,   1.18027814e+00,   1.25398375e+00,
         1.32768935e+00,   1.40139496e+00,   1.47510056e+00,
         1.54880616e+00,   1.62251177e+00,   1.69621737e+00,
         1.76992298e+00,   1.84362858e+00,   1.91733419e+00,
         1.99103979e+00,   2.06474539e+00,   2.13845100e+00,
         2.21215660e+00,   2.28586221e+00,   2.35956781e+00,
         2.43327342e+00,   2.50697902e+00,   2.58068463e+00,
         2.65439023e+00,   2.72809583e+00,   2.80180144e+00,
         2.87550704e+00,   2.94921265e+00,   3.02291825e+00,
         3.09662386e+00,   3.17032946e+00,   3.24403506e+00,
         3.31774067e+00,   3.39144627e+00,   3.46515188e+00,
         3.53885748e+00,   3.61256309e+00,   3.68626869e+00]), a list of 50 Patch objects>)
 plt.show()

