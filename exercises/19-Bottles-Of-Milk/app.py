

def number_of_bottles():
     for i in range(99,0,-1):
         
         if i <=99:
             print(f"{i} bottles of milk on the wall, {i} bottles of milk. Take one down and pass it around, {i-1} bottles of milk on the wall.")
         elif i == 0:
             print("1 bottle of milk on the wall, 1 bottle of milk.")
             print("Take one down and pass it around, no more bottles of milk on the wall.")

             print("No more bottles of milk on the wall, no more bottles of milk.")
             print ("Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()

# def number_of_bottles():
#     for i in range(99,1,-1):
#         print(f"{i} bottles of milk on the wall, {i} bottles of milk.") 
#         print(f"Take one down and pass it around, {i-1} bottles of milk on the wall.")

# "1 bottle of milk on the wall, 1 bottle of milk."
# "Take one down and pass it around, no more bottles of milk on the wall."

# "No more bottles of milk on the wall, no more bottles of milk."
# "Go to the store and buy some more, 99 bottles of milk on the wall."

# number_of_bottles()