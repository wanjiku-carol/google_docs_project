import re
import pandas as pd
from functools import partial

CHECK_MESSAGE = '...Checking your pin...'
RESP = None

def check_white_spaces(input):
  """This helper function removes whitespaces from the input"""
  print(CHECK_MESSAGE)
  check_whitespace = re.search('\s', input)
  if check_whitespace:
    RESP =', There are whitespaces in your input'
  return RESP if RESP else 'Everything looks good here'

def check_digits(input):
  print(CHECK_MESSAGE)
  check_digits = re.search('\d', input)
  if not check_digits:
    RESP = 'Your pin should always be numbers'
  return RESP if RESP else 'Everything looks good here'

def check_length(input):
  """Just testing a regex to confirm that the pin is between 1000-9999"""
  RESP = None
  print(CHECK_MESSAGE)
  check_length = re.search('[1-9][0-9]{3}', input)
  if not check_length:
    RESP = 'Your pin must be 4 numbers or more'
  return RESP if RESP else 'Everything looks good here'


def sort_this__list_of_tuples(lst):
  sort_first = sorted(lst, key=lambda x: x[0])
  sort_second = sorted(sort_first, key=lambda x: x[1])
  direct_sort = sorted(lst)
  print(f'First sort: {sort_first}')
  print(f'Step sort: {sort_second}')
  print(f'Direct sort: {direct_sort}')
  return sort_second == direct_sort

def partial_functions(a, b):
  """
  Using partial example:
  add_two = partial(partial_functions, 2)
  two_plus_anthing_else = add_two(x) - x being any other number
  """
  return a + b

def partial_function_with_functions(f, lst):
  """
  Using partial example:
  map_something = partial(partial_function_with_functions, map)
  map_anything = map_something(some_list) - some_list being any list
  filter_something = partial(partial_function_with_functions, filter)
  filter_anything = map_something(some_list) - some_list being any list
  """
  p_lst = list(f(lambda x: x / 2, lst))
  return p_lst

def seed_data():
  data = pd.read_excel (r'/Users/carolinewanjiku/Downloads/AIS DATA.xlsx')
  df = pd.DataFrame(data, columns= ['Name'])
  import pdb; pdb.set_trace()
  print (type(df))
  return df.values

def compare_names(array):
  array_of_names = []
  for item in array:
    name = item[0]
    array_of_names.append(name)
  return array_of_names

def update_data(name, placed):
  data = pd.read_excel (r'/Users/carolinewanjiku/Downloads/AIS DATA.xlsx')
  new_df = pd.DataFrame('Placed':placed)
  return new_df

def write_to_your_doc(array_of_names, your_doc):
  data = pd.read_excel (r'/Users/carolinewanjiku/Downloads/AIS DATA.xlsx')
  placed_status = pd.DataFrame(data, columns= ['Placed'])
  names = pd.DataFrame(data, columns= ['Name'])
  names_on_your_doc = compare_names(names)
  names_on_ais = compare_names(seed_data())
  new_df = pd.DataFrame({'Placed':'Yes' })
  placed_status.update(new_df) for name in names_on_your_doc if name == ais_name for ais_name in names_on_ais
