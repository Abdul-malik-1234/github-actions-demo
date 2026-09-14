# This uses the new t-string literal prefix
def check_template():
    name = "World"
    template_obj = f"Hello {name}" 
    print(type(template_obj))

check_template()
