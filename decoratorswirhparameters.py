def title_decorator(print_name_function):
  def wrapper(*args, **kwargs):
    print("Professor:")
    print_name_function(*args, **kwargs)
  return wrapper

@title_decorator
def print_my_name(name, subject):
  print(name, "-",  subject)

print_my_name("Lorena", "History of Tattooing")
