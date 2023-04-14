import bcrypt

def hash_password(password):
    # Generate a salt value to mix with the password
    salt = bcrypt.gensalt()

    # Hash the password using the salt and bcrypt's hash function
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Return the hashed password
    return hashed_password.decode('utf-8')

# >>> password = "my_password"
# >>> hashed_password = hash_password(password)
# >>> print(hashed_password)
# $2b$12$uZqgDJzaKV3f8uTgW8KJkOw/gxGfxe4UrkrTkcLWkXHtoOZTMiNrS
