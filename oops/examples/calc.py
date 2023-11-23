import os,sys

if sys.platform =="win32":
    clear = lambda:os.system("cls")
else:
    clear = lambda:os.system("clear")
class Calc:
    result =0

    def add(self,num):
        self.result+= num
        return self
    
    def sub(self,num):
        self.result-= num
        return self
        
    def mul(self,num):
        self.result*=num
        return self
    
    def div(self,num):
        try:
            self.result/=num
            return self
        except Exception as e:
            print(f"Error:{e}")

    def final(self):
        return self.result
    
def validate(inp: any, _type: any = int):
    try:
        return _type(inp)
    except Exception as e:
        return {e}

def main():
    clear()
    cal = Calc()
    print("Calculator".center(100))
    
    while True:
        num = input("enter the number (Type 'exit for exiting): ")
        if not num or num in ("x","exit","q","quit"):
            break
        v_num = validate(num,float)
        operator = input('Operator: ')
        
        
        op = None
        if operator in("+","add"):
            op = "add"
        elif operator in("-","sub"):
            op = "sub"
        elif operator in("*","mul"):
            op = "mul"
        elif operator in("/","div"):
            op = "div"
        else:
            print("Invalid operator")
            continue

        method_mapping = {
            "add": cal.add,
            "sub": cal.sub,
            "mul": cal.mul,
            "div": cal.div
        }
        method = method_mapping[op]
        if v_num is None:
            continue
        method(v_num)

    print(f"Result: {cal.final():.2f}")

if __name__ == "__main__":
    main()
    

    
