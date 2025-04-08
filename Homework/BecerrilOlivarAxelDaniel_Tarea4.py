'''
1.- Sean A={1,2,3,4}, B={2,4,6,8} y C={3,4,5,6}, hallar:
    1. AuB
    2. AuC
    3. BuC
    4. BuB
'''
print("Ejercicio 1.")
A={1,2,3,4} 
B={2,4,6,8} 
C={3,4,5,6}

print("A =",A)
print("B =",B)
print("C =",C)

U1=A|B
print("\nAuB =",U1)

U2=A|C
print("AuC =",U2)

U3=B|C
print("BuC =",U3)

U4=B|B
print("BuB =",U4)

'''
2.- Sean A={1,2,3,4}, B={2,4,6,8} y C={3,4,5,6}, hallar:
    1. AnB
    2. AnC
    3. BnC
    4. BnB
'''

print("\nEjercicio 2.")
A={1,2,3,4} 
B={2,4,6,8} 
C={3,4,5,6}

print("A =",A)
print("B =",B)
print("C =",C)

U1=A&B
print("\nAnB =",U1)

U2=A&C
print("AnC =",U2)

U3=B&C
print("BnC =",U3)

U4=B&B
print("BnB =",U4)

'''
3.- Sean A={1,2,3,4}, B={2,4,6,8} y C={3,4,5,6}, hallar:
    1. A-B
    2. C-A
    3. B-C
    4. B-A
    5. B-B
'''

print("\nEjercicio 3.")
A={1,2,3,4} 
B={2,4,6,8} 
C={3,4,5,6}

print("A =",A)
print("B =",B)
print("C =",C)

U1=A-B
print("\nA-B =",U1)

U2=C-A
print("C-A =",U2)

U3=B-C
print("B-C =",U3)

U4=B-A
print("B-A =",U4)

U5=B-B
print("B-B = ",U5)

'''
4.- Sean U={1,2,3,4,5,6,7,8,9}, A={1,2,3,4}, B={2,4,6,8} y C={3,4,5,6}, hallar:
    1. A'
    2. B'
    3. (AnC)'
    4. (AuB)'
    5. (A')'
    6. (B-C)'
'''

print("\nEjercicio 4.")
U={1,2,3,4,5,6,7,8,9}
A={1,2,3,4} 
B={2,4,6,8} 
C={3,4,5,6}

print("U =",U)
print("A =",A)
print("B =",B)
print("C =",C)

U1=U-A
print("\nA'=",U1)

U2=U-B
print("B' =",U2)

u3=U-A
u2=U-C
U3=u3|u2
print("(AnC)' =",U3)

u3=U-A
u4=U-B
U4=u3&u4
print("(AuB)' =",U4)

U5=A
print("(A')' = ",U5)

u6=U-B
u7=U-C
U6=u6-u7
print("(B-C)' =",U6)