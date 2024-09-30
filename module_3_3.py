#Распаковка
# 1
def print_params(a=1, b='string', c=True):
    print(a,b,c)
print_params()
#print_params(a,b,c,d)
print_params(a=1, b=25, c=[1, 2, 3])
# 2
values_list = [25, 'string', True]
values_dict = {'a':27, 'b':'word', 'c': True}
print_params(*values_list)
print_params(**values_dict)
# 3
values_list_2 = [54.32, 'string']
print_params(*values_list_2, 42)
