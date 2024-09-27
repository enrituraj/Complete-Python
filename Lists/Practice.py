# list


user_input = input("Enter number separated by spaces : ")
input_list = user_input.split()

element = input("Enter the element that has to remove : ")
input_list.remove(element)
print("Item present in list ",input_list)