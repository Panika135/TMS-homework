my_dict = {'a': 400, 'b': 58700, 'c': -560, 'd': 'one', 'e': 20000, 'f': 2000, 'd': 400}
list_k_v = [(k, v) for k, v in my_dict.items()]
list_k_v.sort(key= lambda i : i[1], reverse=True)
for i in range(3):
    print(list_k_v[i][0])
