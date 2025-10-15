
import datetime
import time


class Bank:


    d={}
    accou={}
    passwd={}
    fee = 0.05
    famt=0
    f = open('General info(acc)', 'a')
    f1 = open('hiconfide', 'a')

    f3=open('data','a')
    q=None
    q1=None

   # def __init__(self,ac,name,ba):

    #    self.ac=None
    #    self.den=None
    #    self.name=None
    #    self.famt=None
        #self.p=0

    def gen(self):
     with open('highconf', 'r') as f:
            for i in f:
                (key, val) = i.strip().split()

                self.d[key] = int(val)


     z = 1
     while z < 2:
        print('1.New customer')
        print('2.Existing customer')
        i = int(input('Enter your choice:'))
        if i == 2:
            print('1.Account balance')
            i = int(input('Choose your option:'))
            if i == 1:
                self.name = input('Enter name:')
                password=input('Enter password:')
                if password == self.passwd.get(self.name):
                  print('Account number:', self.accou.get(self.name))
                  print('Balance Amount:', self.d.get(self.name))
        else:
            b1 = datetime.datetime.now()
            self.begin=b1.strftime('%y-%m-%d on %H : %M : %S')
            self.f.write(f'\nAccount created on {self.begin} ---->')
            print('Enter your age:20')
            j=20
            if j >= 18:
                print('Will be activated within 48 hours')
                l = {}
                for o in range(1):
                    print('Enter first amount >3000:5000')
                    self.famt=5000
                    print('Enter your name:a')
                    self.pos=input()
                    if self.pos not in self.d:
                      if self.famt >= 3000:
                        b1 = datetime.datetime.now()
                        self.d.update({self.pos: self.famt})
                        self.accou.update({self.pos: id(self.pos)})
                        print('Hold for 10 sec to generate account number')

                        print("\nAccount number:", id(self.pos))
                        print('Please choose your password:9093')
                        self.password=9093
                        self.f1.write(f' Password:{self.password}')
                        self.passwd.update({self.pos:self.password})
                        print(self.d)
                      else:
                        print('Low balance unable to process "Try again"')
                    else:
                       print('sorry re-register with another name')
                       print(self.d)
                self.f.write(f' Age :{j}')
            else:
                print('Unable to process for age:', j, 'years')
            z = int(input('Enter (3) to exit or (1) to continue:'))
            print(self.d)
    def transfer(self):
        utrans = input('Enter account name ')
        trans = input('Enter account name to transfer:')
        if trans and utrans in self.d.keys():
            transamount = int(input('Enter amount to transfer:'))
            if transamount < self.d.get((utrans)):
                x=self.d.get((utrans))
                y=self.d.get((utrans))-transamount
                self.d.update({(utrans):y})
                z=self.d.get((trans))+transamount
                self.d.update({(trans): z})


    def display(self):
        ch = input('Enter name for details:')
        print('Hold for 10 sec to get information')
      #  for u in range(10, 0, -1):
       #     print(u, ' ', end="")
      #      time.sleep(2.5)
        print(self.d)
        print(f"\nName:{ch} \nBalance:{self.d.get(ch)} \nAccount number:{self.accou.get(ch)}")
a=Bank()
h=a.gen()
#a.deposit()
#a.withdrawl()
a.transfer()
a.display()
