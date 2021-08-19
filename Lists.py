# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:06:19 2021

@author: s2138675
"""

pressure = [0.27,0.456,0.3333,0.7,1.4]
print('pressure: ',pressure)

# subset value 2 
pressure[1]

print(pressure[1])

# append value at the end
pressure.append(0.54333)
print('pressure: ',pressure)

# add another list within the list
pressure.append([0.43,2.7,0.665])
print('pressure: ',pressure)


# extend a list
pressure1 = [0.27,0.456,0.3333,0.7,1.4]
pressure1.extend([0.43,2.7,0.665])
print('pressure1: ',pressure1)




