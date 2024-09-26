from flask import Flask, Response
import os
import socket
import time
import random

##app = Flask(_name_)

historychange = []
historyvalue = []
direction = 0
weight = 0
val = 300.30

##This will turn into a loop for running if we are just going to display a stream.
def rngetf(val):
    
    i = random.randint(1,8)

##    if direction != 0:
##           if direction == 1:
##               i += 1
       
##           else:
##                i += -1

    if i != 0 and i <= 4:
        direction = -1

    if i != 0 and i > 4:
        direction = 1

    if direction == -1:
            ##IF making a livestream, these numbers will have to be reduced down
            weight = random.uniform(-.05, -0.009)
            weight = val * weight
            historychange.append(weight)
            val = val + weight

    if direction == 1:
            ##IF making a livestream, these numbers will have to be reduced down
            weight = random.uniform(.05, .009)

            weight = val * weight
            historychange.append(weight)
            val = val + weight
            
    return val


i = 0
while i < 20:
    print(rngetf(val))
    print(historychange[i])
    i += 1
