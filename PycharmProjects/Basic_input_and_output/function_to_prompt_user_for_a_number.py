def input_number(msg,err_msg = None) :
    while True :
        try :
            return float(input(msg))
        except ValueError :
            if err_msg is not None :
                print(err_msg)

msg = input("Enter : ")
input_number(msg,err_msg=None)
