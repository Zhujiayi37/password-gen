import hashlib


def md5(base, salt):
    obj = hashlib.md5(salt.encode("utf-8"))
    obj.update(base.encode("utf-8"))
    return obj.hexdigest()


def sha1(base, salt):
    obj = hashlib.sha1(salt.encode("utf-8"))
    obj.update(base.encode("utf-8"))
    return obj.hexdigest()


def sha224(base, salt):
    obj = hashlib.sha224(salt.encode("utf-8"))
    obj.update(base.encode("utf-8"))
    return obj.hexdigest()


def sha256(base, salt):
    obj = hashlib.sha256(salt.encode("utf-8"))
    obj.update(base.encode("utf-8"))
    return obj.hexdigest()


def sha384(base, salt):
    obj = hashlib.sha384(salt.encode("utf-8"))
    obj.update(base.encode("utf-8"))
    return obj.hexdigest()


def sha512(base, salt):
    obj = hashlib.sha512(salt.encode("utf-8"))
    obj.update(base.encode("utf-8"))
    return obj.hexdigest()
