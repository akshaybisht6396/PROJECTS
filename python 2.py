#def modify_immutable(x):
    #  x += 1
 #     print(f"Inside function: {x}")
#a = 5
#modify_immutable(a)
#print(f"Outside function: {a}")  # Output: 5 (unchanged)
  
def modify_mutable(lst):
      lst.append(4)
      print(f"Inside function: {lst}")
my_list = [1, 2, 3]
modify_mutable(my_list)
print(f"Outside function: {my_list}")  # Output: [1, 2, 3, 4] (modified)
  
