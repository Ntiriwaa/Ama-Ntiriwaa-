#Computer Application In Civil Engineering
"""
Ama Ntiriwaa Kyere
6940421

Github Address= https://github.com/Ntiriwaa/Ama-Ntiriwaa.git
"""

import numpy as np
L=12 #length of beam in metres
w=10 #intensiy of load in KN/m

#Question a
#Bending moment(BM) and shear force(SF) at the first end,x=0

x=0
BM=(w*(-6*x**2+6*L*x-L**2))/12
SF=w*(L/2-x)
m='The bending moment at x=0 is'
n='the shear force at x=0 is'
print()
print('(ai)'+m+str(BM)+'and',n + str(SF))
#Bending moment(BM) and shear force(SF) at the first end,x=L=10
x=L
BM=(w*(-6*x**2+6*L*x-L**2))/12
SF=w*(L/2-x)
a='The bending moment at x=L is'
b='the shear force at x=L is'
print()
print('(aii)'+ m + str(BM) +'and',n+str(SF))

#Question b
"""
When the bending moment is zero,the expression will be x**2-Lx + L**2/6=0
"""
#from the expression

a=1
b=-L

c=L**2/6
#From the almighty formula;
discriminant=b**2-4*a*c
root_1b = (-b +np.sqrt(discriminant))/2*a
root_2b =(-b-np.sqrt(discriminant))/2*a
print()
print('(b) The points of contra-flexeur are {0} and {1}'.format(root_1b,root_2b))


#Question c
"""

When the shear force is zero,x=L/2
"""
x=L/2

print()

print('(c) The point at which SF=0 is {}'.format(x))


#Question d
p=0
s=0.01
q=L+s
x=np.arange(p,q,s)
M=(w*(-6*x**2+6*L*x-L**2))/12
print()
print('(d) Using the commence variable,the bending moment at each step in the array is {0}'.format(BM))


#Question e
V=w*(L/2-x)
print()
print('(e) The shear force for each step along the span is {}'.format(SF))


#Question f
"""
Let the absolute value of the bending moment array be ABS

Also let the minimum ABS be m_ABS
"""
ABS =abs(M)
m_ABS=min(ABS)
"""

When the bending moment is m_ABS,we get an expression x**2-Lx +(L**2/6)+(2*m_ABS)/w=0
"""
#from the above expression

a=1
b=-L
c=(L**2/6)+(2*m_ABS)/w

#From the Almighty formula;
discriminant=b**2-4*a*c

root_1f =(-b+np.sqrt(discriminant))/2*a

root_2f =(-b-np.sqrt(discriminant))/2*a

print()

print('(f) The points along L at which the absolute values of the bending moment array is minimum are{0} and {1}'.format(root_1f,root_2f))


#Question g
"""
Let the relative errors be r_e
"""

r_e1=((root_1b-root_1f)/root_1b*100)
r_e2=((root_2f-root_2b)/root_2f*100)

print()     

print('g) The relative errors between estimated points of contra-flexure are {0}% and {1}%'.format(r_e1,r_e2))


#Question h

"""
Let the maximum bending moment be max_BM and the minimum bending moment be min_BM
"""
#for the maximum
max_BM=max(M)

a=1

b=-L

c=(L**2/6)+(2*max_BM)/w

#From the Almighty formula;
discriminant=b**2-4*a*c

root_1=(-b + np.sqrt(discriminant))/2*a

root_2=(-b - np.sqrt(discriminant))/2*a

print()

print('hi)The points at which the maximum bending moment occur are {0} and {1}'.format(root_1,root_2))

#for the minimum
min_BM =min(M)




a=1
b=-L
c=(L**2//6)+(2*min_BM)/w

#Frim the Almighty formula;
discriminant=b**2-4*a*c

root_1=(-b -np.sqrt(discriminant))/2*a
root_2=(-b + np.sqrt(discriminant))/2*a
print()

# print('(hii) The points at which the minimum bending moment occur are {0} and {1}'.format(root_1,root_2))
      

