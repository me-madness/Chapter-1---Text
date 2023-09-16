import string 

t = string.Template('$var')
print(t.pattern.pattern)

\$(?:
  (?P<escaped>\$)                | # Two delimiters    
  (?P<named>[_a-z][_a-z0-9]*)    | # Identifier    
  {(?P<braced>[_a-z][_a-z0-9]*)} | # Braced identifier   
  (?P<invalid>)                    # Ill- formed delimiter exprs
)