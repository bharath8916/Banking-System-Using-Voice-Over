import datetime
import time


class Bank:
    d = {}
    accou = {}
    passwd = {}
    fee = 0.05
    famt = 0
    f = open('General info(acc)', 'a')
    f1 = open('Registered data', 'a')
    f2 = open('highconf', 'a+')
    f3 = open('passwords', 'a+')
    f4 = open('hiconfide', 'a+')
    h1 = open('data','a')
    q = None
    q1 = None

    # def __init__(self,ac,name,ba):

    #    self.ac=None
    #    self.den=None
    #    self.name=None
    #    self.famt=None
    # self.p=0

    def gen(self):
        with open('highconf', 'r') as fa:
            for i in fa:
                (key, val) = i.strip().split()
                self.d[key] = float(val)

        with open('passwords', 'r') as fab:
            for i in fab:
                (key, val) = i.strip().split()
                self.passwd[key] = (val)
        with open('hiconfide', 'r') as fab:
            for i in fab:
                (key, val) = i.strip().split()
                self.accou[key] = int(val)


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
                    print('Account number:', self.accou.get(self.name))
                    print('Balance Amount:', self.d.get(self.name))

            else:
                print('1.New account:')
                i = int(input('Enter your choice:'))
                b1 = datetime.datetime.now()
                self.begin = b1.strftime('%y-%m-%d on %H : %M : %S')
                self.f.write(f'\nAccount created on {self.begin} ---->')
                j = (input('Enter PAN card number:'))
                self.f.write(f' PAN card number:{j}')
                j = int(input('Enter AADHAAR card number:'))
                self.f.write(f' AADHAAR number:{j}')
                j = int(input('Enter your age:'))

                if j >= 18:
                    ch = input("Purpose:")
                    print('Will be activated within 48 hours')
                    l = {}
                    # n=int(input())
                    for o in range(1):
                        self.famt = int(input('Enter first amount >3000:'))
                        self.pos = input('Enter your name:')
                        if self.pos not in self.d:
                            if self.famt >= 3000:

                                b1 = datetime.datetime.now()
                                begin = b1.strftime('%y-%m-%d on %H : %M : %S')
                                self.f1.write(f'\nAccount created on {begin} ---->')
                                self.h1.write(f"\nLast login: {self.pos}\t {begin}")
                                self.f1.write(f'Name:{self.pos}')
                                self.f1.write(f' Account number:{id(self.pos)}')
                                self.f2.write('\n' + self.pos + " " + str(self.famt))
                                self.d.update({self.pos: self.famt})
                                self.accou.update({self.pos: id(self.pos)})
                                print('Please wait Loading...')
                                from tqdm import tqdm, trange

                                with tqdm(total=100) as pbar:
                                    for i in range(10):
                                        if i == 5:
                                            print('\nAccount created waiting for account number...')
                                        time.sleep(1)
                                        pbar.update(10)
                                print("\nAccount number:", id(self.pos))
                                self.password = input('Please choose your password:')
                                self.f4.write('\n' + self.pos + " " + str(id(self.pos)))
                                self.f3.write('\n' + self.pos + " " + str(self.password))
                                self.f1.write(f' Password:{self.password}')
                                self.passwd.update({self.pos: self.password})
                            else:
                                print('Low balance unable to process "Try again"')
                        else:
                            print(f'Sorry! user with name "{self.pos}" as already registered')
                    self.f.write(f' Age :{j}')
                else:
                    print('Unable to process for age:', j, 'years')
                z = int(input('Enter (3) to exit or (1) to continue:'))

    def deposit(self):
        count = 3
        x = int(input("Enter '1' to deposit or '2' to exit:"))
        while x == 1:
            if count == 1 or count == 2 or count == 3:
                self.den = input('Enter your name:')
                if self.den in self.d:
                    self.famt = self.d.get(self.den)
                    self.pas = input('Enter your password:')
                    if self.pas == self.passwd.get(self.den):
                        n = float(input('Enter amount to deposit:'))
                        self.p = self.fee * n
                        n = n - self.p
                        self.d.update({self.den: n + self.famt})

                        self.famt = n + self.famt
                        print('Please wait Processing Deposit...')
                        from tqdm import tqdm, trange
                        with tqdm(total=100) as pbar:
                            for i in range(10):
                                time.sleep(1)
                                pbar.update(10)
                        self.f2.write('\n' + self.den + " " + str(self.famt))
                        self.h1.write(f"\n{self.den}\t deposited:{str(n)}")
                        print(f"Bank fee charges 5% only ${n} will credited to acc number:{self.accou.get(self.den)} ")

                        x = int(input("Enter '1' to continue or '2' to exit:"))
                        q = self.d.get(self.den)

                    else:
                        print('Wrong password try again!!!')
                        count = count - 1
                        x = int(input("Enter '1' to deposit or '2' to exit:"))
            else:
                print('ATTEMPTED 3 times')
                break

    def withdrawl(self):
        count = 3

        x = int(input("Enter '1' to withdrawl or '2' to exit:"))
        while x == 1:
            if count == 1 or count == 2 or count == 3:
                wname = input('Enter your name:')
                self.pas = input('Enter your password:')
                if self.pas == self.passwd.get(wname):
                    w = float(input('Enter amount to withdrawl:'))
                    print('Please wait Processing withdrawal...')
                    from tqdm import tqdm, trange

                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    if w <= self.d.get(wname) and self.d.get(wname) > 0:

                        z = self.fee * w
                        i = 0
                        res = self.d.get(wname) - z
                        c = self.d.get(wname)
                        v = self.d.get(wname) - w - z
                        t = self.d.get(wname) - w - i
                        k = self.d.get(wname)
                        self.d.update({wname: res})

                        if w > self.d.get(wname):
                            print('Insufficent balance!!!')
                            self.d.update({wname: t})
                            self.d.update({wname: k})

                        else:
                            # self.d.update({wname: res})
                            self.d.update({wname: v})
                            q1 = self.d.get(self.den)

                            self.f2.write('\n' + wname + " " + str(v))
                            self.h1.write(f"\n{wname}\t withdrawal:{str(v)}")
                            print(
                                f"\n${z} will be debited as Bank fee charges 5% from account number:{self.accou.get(wname)}")
                    elif w > self.d.get(wname):
                        print('In sufficent balance')
                        print('Please try again!!!')

                else:
                    print('Wrong password try again!!!')
                    count = count - 1
                x = int(input('Enter 1 to withdrawl or 2 to exit :'))
                x = x + 0
            else:
                print('ATTEMPTED 3 times')
                break

    def transfer(self):
        x = int(input("Enter '1' to transfer or '2' to exit:"))
        while x == 1:
            utrans = input('Enter account name ')
            trans = input('Enter account name to transfer:')
            if utrans and trans in self.d.keys():
                transamount = int(input('Enter amount to transfer:'))
                print('Please wait Performing transactions...')
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                if transamount < self.d.get(utrans):
                    x = self.d.get(utrans)

                    y = self.d.get(utrans) - transamount
                    self.f2.write('\n' + utrans + " " + str(y))
                    self.d.update({utrans: y})
                    z = self.d.get(trans) + transamount
                    self.d.update({trans: z})
                    self.f2.write('\n' + trans + " " + str(z))
                    self.h1.write(f"\n{utrans}\t {str(transamount)} transfered")
                    self.h1.write(f"\n{trans}\t recieved:{str(transamount)} ")

                    print('Successfully transferred')
                    x = int(input("Enter '1' to transfer or '2' to exit:"))
                else:
                    print(f'Insufficeint balance in {utrans} account\n')
                    print('Try again!!!')
                    x = int(input("Enter '1' to transfer or '2' to exit:"))

    def display(self):
        x = int(input("Enter '1' to get info or '2' to exit:"))
        while x == 1:
            ch = input('Enter name for details:')
            print('Please wait Loading...')
            from tqdm import tqdm, trange
            with tqdm(total=100) as pbar:
                for i in range(10):
                    time.sleep(1)
                    pbar.update(10)
                print(f"\nName:{ch} \nBalance:{self.d.get(ch)} \nAccount number:{self.accou.get(ch)}")
            x = int(input("Enter '1' to get info or '2' to exit:"))
    def history(self):
        with open('data', 'r') as f:
            x = 0
            z=0
            for i in f.readlines():
                if 'krishna'  in i.split():
                    print(i)
                    x = 1
                    z=1
                else:
                    x = 0
                    pass
        if x == 0 and z==0:
            print('not found')
        else:
            pass

a = Bank()
#h = a.gen()
#a.deposit()
#a.withdrawl()
#a.transfer()
#a.display()
a.history()
