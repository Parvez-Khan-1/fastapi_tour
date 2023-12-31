from passlib.context import CryptContext

pass_cxt = CryptContext(schemes="bcrypt", deprecated="auto")


class Hash():
    @staticmethod
    def bcrypt(password: str):
        return pass_cxt.hash(password)

    @staticmethod
    def verify(hashed_password, plain_password):
        return pass_cxt.verify(plain_password, hashed_password)
