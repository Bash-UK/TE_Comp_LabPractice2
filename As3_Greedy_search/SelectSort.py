class SelectSort:
   
    def selection_sort(self,array):  
        length = len(array)  
        for ind in range(length):
            min_index = ind
 
            for j in range(ind + 1, length):
                # select the minimum element in every iteration
                if array[j] < array[min_index]:
                    min_index = j
            # swapping the elements to sort the array
            (array[ind], array[min_index]) = (array[min_index], array[ind])
        return array      

    def file_input(self):
        inner_list=[]
        with open('sort.csv') as f:
         for line in f:
             # inner_list = [num.strip() for num in line.split(',')]
             # in alternative, if you need to use the file content as numbers
             inner_list = [int(num.strip()) for num in line.split(',')]
         print(inner_list)
         return inner_list
   