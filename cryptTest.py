import time
import bcrypt 
from  multiprocessing import Pool

def hash_password(password):
    print(password, bcrypt.hashpw(password, bcrypt.gensalt()))
    

if __name__ == "__main__":
    str = [b'password1', b'password2'
    ,b'password3',b'password4',b'password5',b'password6'
    ,b'password7',b'password8',b'password9',b'password10'
    ,b'password11,',b'password12',b'password13',b'password14'
    ,b'password15',b'password16',b'password17',b'password18'
    ,b'password19',b'password20']

    p = Pool()
    p.map(hash_password, str)
    # for i in str:
    #     hash_password(i)

