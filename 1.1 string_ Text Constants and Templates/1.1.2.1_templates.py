import string
values = {'var': 'foo'}

t = string.Template("$var is here but $missing is not provided")

try:
    print('substitute()     :', t.substitute(values))
except KeyError as err:
    print('ERROR:', str(err))
    
    print('save_substitute():', t.save_substitute(values))