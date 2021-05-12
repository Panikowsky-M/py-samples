#!/bin/python3.9
import hashlib,bcrypt

def GetBcryptPw(pw,s):
    Hpass = bcrypt.hashpw( (pw + s).encode('utf-8'),bcrypt.gensalt() )
    return Hpass

def GetSha256Pw(pw,s):
    Hpass = hashlib.sha256( (pw + s).encode('utf-8') ).hexdigest()
    return Hpass

def GetMd5Pw(pw,s):
    Hpass = hashlib.md5( (pw + s).encode('utf-8') ).hexdigest()
    return Hpass

password = 'superPuperPassword'
salt = '$2b$15$NSVH/I.9u1l/WoYUd/sSI.'

_pass = [] 
with open('pw.txt','r',encoding='utf-8') as pwfile:
    for line in pwfile:
        _pass.append(line)

for p in _pass:
    print("Пароль %s в формате sha256: %s" % (p,GetSha256Pw(p,salt)) )
    print("Пароль %s в формате bcrypt: %s" % (p,GetBcryptPw(p,salt)) )
    print("Пароль %s в формате md5:    %s" % (p,GetMd5Pw(p,salt)) )
