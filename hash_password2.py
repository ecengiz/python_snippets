import hashlib

def hash_password(password):
    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    # Return the hashed password
    return hashed_password

# This will output a string representing the hashed password. Note that SHA-256 is a one-way hashing algorithm, so the original password cannot be recovered from the hashed value.
  
# In [2]: password = "my_password"
#    ...: hashed_password = hash_password(password)
#    ...: print(hashed_password)
#    ...: 
# f6e248ea994f3e342f61141b8b8e3ede86d4de53257abc8d06ae07a1da73fb39

# In [3]: password = "my_password"
#    ...: hashed_password = hash_password(password)
#    ...: print(hashed_password)
#    ...: 
# f6e248ea994f3e342f61141b8b8e3ede86d4de53257abc8d06ae07a1da73fb39
