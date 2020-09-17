from ising_class import *
acell=cell(3,3,10) #Args: i, j, n
print(acell.cellspin())
acell.spin.flip() #Reach
print(acell.left)
print(acell.right)
print(acell.up)
print(acell.down) 
