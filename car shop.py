import datetime
print("!!!!!!! CAR SHOP !!!!!!!!")

class vechicle:
    def __init__(self,audi,mercedes,bmw,jaguar):
        self.audi = audi
        self.mercedes = mercedes
        self.bmw = bmw
        self.jaguar = jaguar
    def __str__(self):
        return str(self.audi)+' ' +str(self.mercedes)+'  '+str(self.bmw)+'  '+str(self.jaguar)

vech = vechicle('1- audi','2- mercedes','3- bmw','4- jaguar')
print(vech)


class payment:
    def __init__(self,full_payment,loan):
        self.full_payment = full_payment
        self.loan =loan
    def __str__(self):
        return "%s for full_payment deposit and \n%s deposit if bank loan"  %(self.full_payment,self.loan)

cash = payment('$2000','$1000')
sel_car = input("Sir ,which car are you looking for =   \t")
print(sel_car.upper(),"GREAT!!! we have four color")

class color:
    def __init__(self,a_black,me_yellow,b_purple,ja_white):
        self.a_black = a_black
        self.me_yellow = me_yellow
        self.b_purple = b_purple
        self.ja_white = ja_white
    def __str__(self):
        return str(self.a_black) +' '+str(self.me_yellow)+ ' '+str(self.b_purple)+' '+str(self.ja_white)

design = color('1- black','2- yellow','3- purple','4- white')
print(design)
choice_color = input("which color you prefer: ")
prize =input('should i show you the prize  [y,n]= \t')
if prize == ('y'):
    print(cash)
elif prize == ('n','N'):
    print('Thank You')
else:
    print('### -we can check for other car- ###')


class date:
    def __init__(self,monday,wednesday,sunday):
        self.monday = monday
        self.wednesday = wednesday
        self.sunday = sunday
    def __str__(self):
        return str(self.monday)+ '  '+str(self.wednesday)+'   '+str(self.sunday)

devl_date = datetime.datetime(2020, 5, 4)
print(devl_date.strftime('car delivery : %B '))
print('[payment will be done in Cash or Cheque]')
booking =input('sir, how would you like to pay: ')
if booking == ('cash'):
    print('Thank You')
elif booking == ('cheque'):
    print('Thank You')
else:
    print("No,sorry not excepted!!")



