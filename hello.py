# sheebang (#!)
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o progama exibe a mnesagem 
correspondente.

Como usar:

Tenha a variavel lang devidamente configurada ex:
    
    export LANG=pt_BR

Execeução:

    python hello.py

"""

__version__ = "0.0.1"
__autor__ = "Juan"
__license__ = "Unlicense"

import os

current_language = "pt_BR"
# snake case

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"

print(msg) 
