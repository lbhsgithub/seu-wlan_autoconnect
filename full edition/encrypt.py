import base64
def encrypt(a):
    return base64.b64encode(a.encode())

if __name__ == '__main__':
    a=encrypt('111111111')
    print(a)
