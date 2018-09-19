from random import random;
import numpy as np
'''
Use one hidden layer with 4 hidden units. Plot the error as a function of the number of iterations. Remember the initial weights.

| x1  | x2  | xor |
| --- | --- | --- |
| 0   | 0   | 0   |
| 1   | 0   | 1   |
| 0   | 1   | 1   |
| 1   | 1   | 0   |

X =[
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
]

T = [
        [0],
        [1],
        [1],
        [0],
]

4x2
W<1> = [
        [W11, W12],
        [W21, W22],
        [W31, W32],
        [W41, W42]
];

4x1
b<1> = [
        [b11],
        [b12],
        [b13],
        [b14]
];

1x4
W<2> =  [W21, W22, W23, W24];
'''


def feedForward(x, t, W1, b1, W2, b2):
    Z1 = W1 * x.T + b1;

    print(Z1);


X = np.matrix([
    [0, 0],
    [1, 0],
    [0, 1],
    [1, 1]
]);

T = np.matrix([
        [0],
        [1],
        [1],
        [0],
]);


W111 = -.4; 
W112 = -.2;
W121 = .3;
W122 = .5;
W131 = -.1;
W132 = .1;
W141 = -.1;
W142 = .2;
    
W1 = np.matrix([
    [W111, W112],
    [W121, W122],
    [W131, W132],
    [W141, W142]
]);

b11 = .1;
b12 = -.2;
b13 = .1;
b14 = -.1;

b1 = np.matrix([
    [b11],
    [b12],
    [b13],
    [b14]
]);

W21 = -.3; 
W22 = .3; 
W23 = -.2; 
W24 = .4;

W2 = np.matrix(''+str(W21) +'; '+str(W22) +'; '+ str(W23) +'; '+str(W24) +'');

b21 = -.3;

b2 = np.matrix([b21]);

feedForward(x=X[1], t=0, W1=W1, b1=b1, W2=W2, b2=b2);