import string 

class MyTemplate(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'
    
template_text = '''
  Delimeter  :  %%
  Replaced   : %with_underscore
  Ignored    : % notunderscored   
'''