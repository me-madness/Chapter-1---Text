import string

values = {'var': 'foo'}

t = string.Template("""
Variable         : $var                    
Escape           : $$                     
Variable in text : ${var}iable                    
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable         : %(var)s
Escape           : %%
Variable in text : %(var)iable
"""

print('INTERPOLATION:', s % values)