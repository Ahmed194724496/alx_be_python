# shopping_list=[]
# shopping_list.append()
# shopping_list.append()
# shopping_list[:]
shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
           item = input("add item name: ") 
           if item:
               shopping_list.append(item)
               print("item added")
           else:
               print("item cannot be added")
           pass
        elif choice == '2':
            item = input("remove item name: ")
            if item:
               shopping_list.removed(item)
               print("item removed") 
            else :
               print("item cannot be removed")         
            pass
        elif choice == '3':
         if  shopping_list:
            print(f"\nCurrent Shopping List:{ shopping_list}")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
