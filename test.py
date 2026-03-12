row = [{"N": True}] * 5
row[0]["N"] = False
print(row)

def add_to_list(item, my_list=[]):
  my_list.append(item)
  return my_list

print(add_to_list(1))
print(add_to_list(2))


def add_to_list_safe(item, my_list=None):
  # If no list was given, create a brand new one.
  if my_list is None:
    my_list = []

  my_list.append(item)
  return my_list

print(add_to_list_safe(1))
print(add_to_list_safe(2))
