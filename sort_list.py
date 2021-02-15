n = int(input())
def split_elements(string):
    list_element = string.split(' ')
    return [list_element[0],int(list_element[1])]
def take_input(n):
    num_list = [split_elements(input()) for i in range(n)]
    return num_list
num_list = take_input(n)

def sort_by_num(list_element):
    return list_element[1]
sorted_list = sorted(num_list,key = sort_by_num)
print(sorted_list)
