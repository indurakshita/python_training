import json

#
# def get_name(name):
#     f = open('ATM.json')
#     data = json.load(f)
#     print(data[name])
#     return data[name]
#
#
# def get_password(pswd)):
#     password = input('enter a pswd')
#     for values in pswd():
#         print(values)
#         # if password == values:
#     # print("balance")
#     #
    # # for y in data.values():
    # #     if y==password:
    # # print("balance")

def get_userval(name,password):
    f = open('ATM2.json')
    data = json.load(f)
    print('data',data)
    if name in data:
        print(name)
        if  'password' in data[name]:
            if data[name]['password']==password:
                return data[name]
            else:
                exit('password is not matching to username')
        else:
            exit('password is not created for this user')
    else:
        exit('invalid user')

def creditordebit(data):
    print('data1',data)
    process=input('enter cerdit or debit')
    print(process)
    if process=='debit':
        amount=int(input('enter the amount'))
        print(data['balance']-amount)
    elif process=='balance':
        print('enter the amount')
        print(data['balance'])
    else:
        exit('invalid')





if __name__ == "__main__":
    x=get_userval('shan','sr')
    print(x)
    creditordebit(x)
