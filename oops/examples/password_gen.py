import random
import string
class Password:
    def __init__(self,length):
        self.length = length
        assert self.length >=8,"password length is less than 8"
        

    def generate(self):
        small = "abcdefghijklmnopqrstuvwxyz"
        upper = small.upper()
        digits = "1234567890"
        sp = "!@#$^&"
        chars = small + upper + digits + sp
        ps = random.choices(chars,k=self.length)
        join_ps = ''.join(ps)
        if self.validate(join_ps):
            return join_ps
        else:
            self.generate()

        # out= ''
        # for _ in range(self.length):
            
        #     out+=random.choice(chars)
        
        
        # print(out)

    def validate(self,passw):
        length = True if len(passw) >= 8 else False
        is_upper = False
        is_lower = False
        is_schars = False
        is_digits = False
        for i in passw:
            if i in string.ascii_uppercase:
                is_upper = True
            elif i in string.ascii_lowercase:
                is_lower = True
            elif i in string.ascii_letters:
                is_schars = True
            elif i in string.digits:
                is_digits = True
        if is_upper and is_lower and is_schars and is_digits and length:
            return "password is",passw
        else:
            return "Invalid password"


ps1 = Password(10)
print(ps1.generate())

