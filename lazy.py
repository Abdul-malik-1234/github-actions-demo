# This runs without error on Python 3.14+
# On Python 3.13, it raises a NameError at runtime because UndefinedType is not defined yet.
class Demo:
    value: UndefinedType  # Notice UndefinedType does not exist anywhere!

def check_feature():
    print("Class created successfully!")

check_feature()
