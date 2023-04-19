import SelectSort
import Prims
# Define the graph as a dictionary of dictionaries
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

def menu():
    flag= True
    while(flag):
         print("\n1] Selection Sort")
         print("\n2] Prims Algo")
         print("\n\n Press 0 to exit ")
         choice = int(input('\nEnter your choice: '))
         #switch
         if choice==1:
            select = SelectSort.SelectSort()
            array = select.file_input()
            select.selection_sort(array)
            print(array)
         elif choice==2:
            prims = Prims.Prims()
            mst = prims.prim(graph,'A')
            print("MST edges: \n\n\n")
            print(mst)
         elif choice==0:
             flag=False
    
if __name__== "__main__":
    menu()