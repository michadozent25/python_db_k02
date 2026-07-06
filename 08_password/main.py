import bcrypt

password ="test"

hashed = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())

print(hashed)# byte-Objekt

print(hashed.decode('utf-8')) # bytes zu String -> in DB speichern

print(bcrypt.checkpw(password.encode('utf-8'),hashed))