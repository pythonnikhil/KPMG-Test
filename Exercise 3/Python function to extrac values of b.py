def my_func():
  dict_list = {'dict1':{'a': 1, 'b': 2, 'c': 3},
            'dict2':{'a': 4, 'b': 5, 'c': 6},
             'dict3':{'a': 7, 'b': 8, 'c': 9}}
  temp = 'b'
  output =[]
  for value in dict_list.values():
    if temp in value:
      output.append(value[temp])

  print("The values of b are "+str(output))
  
my_func()
