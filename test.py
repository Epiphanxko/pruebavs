import os 
import secrets 

clave = secrets.token_hex(64)


api_key= secrets.token_urlsafe(64)
print("Clave HEX 64:",clave)

print("Clave URLSAFE 32", api_key )