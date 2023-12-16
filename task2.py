import random
import string
def generate_password(length):
    characters=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choices(characters,k=length))
    return password
password=generate_password(8)
print(password)
