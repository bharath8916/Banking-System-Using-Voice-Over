import pyttsx3 as p
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import datetime
import time
from word2number import w2n


class Bank:
    d = {}
    accou = {}
    passwd = {}
    fee = 0.05
    firstamount = 0
    f = open('General info(account).AI', 'a')
    f1 = open('Registered data.AI', 'a')
    f2 = open('balance_update.AI', 'a+')
    f3 = open('passwords.AI', 'a+')
    f4 = open('Account_number.Ai', 'a+')
    r = sr.Recognizer()
    engine = p.init()

    rate = engine.getProperty("rate")
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 190)
    engine.setProperty("voice", voices[17].id)

    def bot(self):

        intro = 'no need i will read'
        print('Your Response:', intro)
        if 'no need i will read' not in intro in intro or 'yes read' in intro or 'read it' in intro or 'yeah' in intro or 'red' in intro or 'no problem' in intro:
            self.engine.setProperty("rate", 160)
            with open('data', 'r') as f:
                for i in f:
                    self.engine.say(i)
                    self.engine.runAndWait()
            self.engine.setProperty("rate", 190)
        else:
            self.engine.say('its ok then read  carefully')
            self.engine.say('You have only 30 seconds of time')
            self.engine.runAndWait()
            from tqdm import tqdm, trange
            with tqdm(total=150) as pbar:
                for i in range(30):
                    time.sleep(1)
                    pbar.update(5)
            print('Ended')
            self.engine.say('Your time has ended')
            self.engine.say('Listen to the next instruction please')
            self.engine.runAndWait()
        self.engine.setProperty("rate", 190)

        with open('balance_update.AI', 'r') as fa:
            for i in fa:
                (key, val) = i.strip().split()
                self.d[key] = float(val)

        with open('passwords.AI', 'r') as fab:
            for i in fab:
                (key, val) = i.strip().split()
                self.passwd[key] = (val)
        with open('Account_number.Ai', 'r') as fab:
            for i in fab:
                (key, val) = i.strip().split()
                self.accou[key] = int(val)
        self.engine.setProperty("rate", 170)
        self.engine.say('You have currently this options')
        self.engine.say('I can create New account for you')
        print('New account')
        self.engine.say('I can do Deposits to your account')
        print('Deposit')
        self.engine.say('I can help with Withdrawal money from your account')
        print('Withdrawal')
        self.engine.say('And I can also Transfer money between accounts.')
        print('Transfer')
        self.engine.say('And Even I check for balance of your account.')
        print('Balance checking')
        self.engine.say('Which option do you need?')
        self.engine.runAndWait()

        with sr.Microphone() as source:
            print('\n')
            print('Listening...')
            text1 = self.r.listen(source, timeout=20, phrase_time_limit=10)

        try:
            s1 = str(self.r.recognize_google(text1, language='en-IN')).lower()
            if 'yes' in s1 or 's' in s1 or 'yeah' in s1 or 'account' in s1:
                self.engine.say("Sorry I'am not sure I understand ")
                self.engine.say("Could you please try again")
                print("Sorry I'am not sure I understand ,Could you please try again")
                self.engine.runAndWait()
                with sr.Microphone() as source:
                    print('Listening...')
                    text1 = self.r.listen(source, timeout=20, phrase_time_limit=10)
                s1 = str(self.r.recognize_google(text1, language='en-IN')).lower()

                if "i need new account section" in s1 or "yeah new account" in s1 or 'new account' in s1 or 'i need new account' in s1:
                    print('Your Response:', s1)
                    self.engine.say('its absolutely free to take')
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.gen()
                elif 'yeah deposit' in s1 or 'i need deposit section' in s1 or 'deposit' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.deposit()
                elif 'withdrawal from my account' in s1 or 'i need withdrawal section' in s1 or 'withdrawal' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.withdrawl()
                elif 'transfer from my account' in s1 or 'i need transfer section' in s1 or 'transfer' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.transfer()
                elif 'balance in my account' in s1 or 'i need balance section' in s1 or 'balance' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.balance()

                else:
                    self.engine.say('Please check the options again')
                    self.engine.runAndWait()
                    a.bot()

            else:

                if "i need new account section" in s1 or "yeah new account" in s1 or 'account' in s1 or 'i need it' in s1:
                    print('Your Response:', s1)
                    self.engine.say('its absolutely free to take')
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.gen()
                elif 'yeah deposit' in s1 or 'i need deposit section' in s1 or 'deposit' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.deposit()
                elif 'yeah withdrawal' in s1 or 'i need withdrawal section' in s1 or 'withdrawal' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.withdrawl()
                elif 'yeah transfer' in s1 or 'i need transfer section' in s1 or 'transfer' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.transfer()
                elif 'yeah balance' in s1 or 'i need balance section' in s1 or 'balance' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.balance()

                else:
                    self.engine.say('Please check the options again')
                    self.engine.runAndWait()
                    a.bot()
        except sr.UnknownValueError:
            print('sorry no response!!!')
        except sr.RequestError as e:
            print('Your computer is not connected to internet')

    def check_in(self):
        while True:
            self.engine.say('Do You want anything or exit?')
            print('Do you want anything or exit?')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            check_in = self.r.recognize_google(text1, language='en-IN').lower()
            print('Your Response:', check_in)
            if 'yes new account' in check_in or "new account section" in check_in or "yeah new account" in check_in or   'create new one for me' in check_in:

                self.engine.say('You will redirect to new page')
                self.engine.runAndWait()
                print('Redirecting...')
                from tqdm import tqdm
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                a.gen()
            elif 'deposit' in check_in or 'yes i want to do deposit' in check_in or 'i will do ' \
                                                                                    'deposit' in check_in:

                self.engine.say('You will redirect to new page')
                self.engine.runAndWait()
                print('Redirecting...')
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                a.deposit()
            elif 'yeah withdrawal' in check_in or 'withdrawal section' in check_in or 'withdrawal' in check_in:

                self.engine.say('You will redirect to new page')
                self.engine.runAndWait()
                print('Redirecting...')
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                a.withdrawl()
            elif 'yeah transfer' in check_in or 'transfer section' in check_in or 'transfer' in check_in:

                self.engine.say('You will redirect to new page')
                self.engine.runAndWait()
                print('Redirecting...')
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                a.transfer()

            elif 'exit' in check_in or 'quit' in check_in or 'leave' in check_in or 'thank you' in check_in:
                print('please wait updating information...')
                self.engine.say('please wait updating information...')

                self.engine.runAndWait()
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                self.engine.say('Your information was successfully updated.')
                self.engine.runAndWait()
                print('status:Exit')
                self.engine.say('Thank you for choosing BSBK Bank virtual assistance')
                print('Thank you for choosing BSBK Bank virtual assistance')
                self.engine.runAndWait()

                break

    def gen(self):
        z = True
        while z:
            print('               logged in as New account')
            b1 = datetime.datetime.now()
            self.begin = b1.strftime('%y-%m-%d on %H : %M : %S')
            self.f.write(f'\nAccount created on {self.begin} ---->')
            self.engine.say('Provide your pan number:')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, phrase_time_limit=10)
            self.engine.say('Provide your Aadhaar number:')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text2 = self.r.listen(source, phrase_time_limit=10)
            try:
                p = str(self.r.recognize_google(text1, language='en-IN')).upper()
                aw = str(self.r.recognize_google(text2, language='en-IN'))
                self.p1 = "".join(p.split())
                self.a1 = "".join(aw.split())
                print('Your Response(PAN):', self.p1)
                print('Your Response(Aadhaar):', self.a1)


            except sr.UnknownValueError:
                print('sorry i could not catch it say it again')
                a.gen()


            except sr.RequestError as e:
                print('Your computer is not connected to internet')
                break

            self.engine.say('Please say your age:')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)

            age_1 = self.r.recognize_google(text1, language='en-IN')
            self.age = w2n.word_to_num(age_1)

            print('Your Response:', self.age)

            if self.age >= 18:
                self.engine.say('Please say your purpose of creating this account')
                self.engine.runAndWait()
                with sr.Microphone() as source:
                    print('Listening...')
                    text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                purpose = self.r.recognize_google(text1, language='en-IN')
                print('Your Response:', purpose)
                self.engine.say('Please say your first deposit amount')
                self.engine.say('First amount has to be more than three thousand')
                self.engine.runAndWait()

                with sr.Microphone() as source:
                    print('Listening...')
                    text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                first_amt = self.r.recognize_google(text1, language='en-IN')
                self.firstamount = w2n.word_to_num(first_amt)

                print('Your Response:', self.firstamount)

                if self.firstamount >= 3000:
                    self.engine.say('Say name for your account')
                    print('CAUTION:please do remember they name of your account for future purposes')
                    self.engine.runAndWait()
                    with sr.Microphone() as source:
                        print('Listening...')
                        text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                    self.name = self.r.recognize_google(text1, language='en-IN').lower()
                    if self.name not in self.d:
                        print('Your Response:', self.name)
                        b1 = datetime.datetime.now()
                        begin = b1.strftime('%y-%m-%d on %H : %M : %S')

                        self.d.update({self.name: int(self.firstamount)})
                        self.accou.update({self.name: id(self.name)})
                        self.engine.say('Please wait loading')
                        print('Please wait loading...')
                        self.engine.runAndWait()
                        from tqdm import tqdm, trange
                        with tqdm(total=100) as pbar:
                            for i in range(10):
                                if i == 5:
                                    print('\nAccount created waiting for account number...')
                                time.sleep(1)
                                pbar.update(10)
                        print('\nAccount number:', id(self.name))
                        self.engine.say('Please choose your password')
                        self.engine.say('your password is encrypted')
                        print('Your Response: password encrypted')
                        self.engine.runAndWait()
                        with sr.Microphone() as source:
                            print('Listening...')
                            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)

                        pass_word = self.r.recognize_google(text1, language='en-IN')
                        self.password = w2n.word_to_num(pass_word)

                        print('Your Response:', self.password)

                        self.f.write(f' PAN card number:{self.p1}')
                        self.f1.write(f'\nAccount created on {begin} ---->')
                        self.f1.write(f'Name:{self.name}')
                        self.f1.write(f' Account number:{id(self.name)}')

                        self.f.write(f' Age :{str(self.age)}')
                        self.f2.write('\n' + self.name + " " + str(self.firstamount))
                        self.f.write(f' AADHAAR number:{self.a1}')
                        self.f4.write('\n' + self.name + " " + str(id(self.name)))
                        self.f3.write('\n' + self.name + " " + str(self.password))
                        self.f1.write(f' Password:{str(self.password)}')
                        self.passwd.update({self.name: self.password})
                        self.engine.say(f'Dear {self.name} your account was successfully created and will be '
                                        f'activated  within 48 hours')
                        self.engine.runAndWait()
                        break
                    else:
                        self.engine.say(
                            f'user with name {self.name} has already registered please re-register with another name')

                        self.engine.runAndWait()
                        print('               logged out from New account')
                        break


                else:
                    self.engine.say(
                        f'Sorry your deposit amount {self.firstamount} must be more than three thousand dollars')
                    self.engine.runAndWait()
                    print('               logged out from New account')
                    break



            else:
                self.engine.say(f'Sorry as per norms your age is only {self.age} it must be more 18 to get an account')
                self.engine.runAndWait()
                print('               logged out from New account')
                break
        a.check_in()

    def deposit(self):

        count = 3
        z = True
        print('               logged in as Deposit')
        while z:
            if count == 1 or count == 2 or count == 3:
                self.engine.say('Do you have account?')
                self.engine.runAndWait()
                with sr.Microphone() as source:
                    print('Listening...')
                    text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                sec_check = self.r.recognize_google(text1)
                if 'yes' in sec_check or 'i have' in sec_check or 'i do have' in sec_check:
                    self.engine.say('Please say your account name')
                    self.engine.runAndWait()
                    with sr.Microphone() as source:
                        print('Listening...')
                        text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                    self.den = self.r.recognize_google(text1).lower()
                    print('Your Response:', self.den)

                    if self.den in self.d:
                        self.firstamount = self.d.get(self.den)
                        self.engine.say('say your password')
                        self.engine.runAndWait()
                        with sr.Microphone() as source:
                            print('Listening...')
                            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                        self.pas = self.r.recognize_google(text1)
                        if self.pas == self.passwd.get(self.den):
                            self.engine.say('say amount to deposit')
                            self.engine.runAndWait()
                            with sr.Microphone() as source:
                                print('Listening...')
                                text = self.r.listen(source, timeout=15, phrase_time_limit=10)
                            d = self.r.recognize_google(text)
                            n = w2n.word_to_num(d)
                            self.p = self.fee * n
                            n = n - self.p
                            self.d.update({self.den: n + self.firstamount})

                            self.firstamount = n + self.firstamount
                            print('Please wait Processing Deposit...')
                            from tqdm import tqdm, trange
                            with tqdm(total=100) as pbar:
                                for i in range(10):
                                    time.sleep(1)
                                    pbar.update(10)
                            self.f2.write('\n' + self.den + " " + str(self.firstamount))
                            print(
                                f"Bank fee charges 5% only ${n} will credited to acc number:{self.accou.get(self.den)} ")
                            self.engine.say(
                                f"Bank fee charges 5% only ${n} will credited to acc number:{self.accou.get(self.den)} ")
                            self.engine.runAndWait()
                            q = self.d.get(self.den)
                            self.engine.say('Do you want to deposit again or exit?')
                            print('Do you want to deposit again or exit?')
                            self.engine.runAndWait()
                            with sr.Microphone() as source:
                                print('Listening...')
                                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                            z = self.r.recognize_google(text1).lower()
                            if 'yes' in z:
                                a.deposit()
                            else:
                                print('               logged out from Deposit')
                                a.check_in()

                                break

                        else:
                            print('Wrong password try again!!!')
                            count = count - 1
                            self.engine.say('Do you want to try again or exit?')
                            self.engine.runAndWait()
                            with sr.Microphone() as source:
                                print('Listening...')
                                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                            z = self.r.recognize_google(text1).lower()
                            if 'yes' in z:
                                a.deposit()

                            else:
                                print('               logged out from Deposit')
                                break
                else:
                    self.engine.say('First you must have an account to deposit amount')
                    self.engine.say("Do you want to redirect to account creating page or exit?")
                    print('Do you want to redirect to account creating page or exit?')
                    self.engine.runAndWait()
                    with sr.Microphone() as source:

                        print('Listening...')
                        text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                    create_deposit = self.r.recognize_google(text1).lower()
                    if 'yes i will create' in create_deposit or 'yes i will' in create_deposit or 'i will create a ' \
                                                                                                  'new account' in \
                            create_deposit or 'i will' in create_deposit or 'i must' in create_deposit:
                        self.engine.say('its absolutely free to take')
                        self.engine.say('You will redirect to new page')
                        self.engine.runAndWait()
                        print('Redirecting...')
                        from tqdm import tqdm, trange
                        with tqdm(total=100) as pbar:
                            for i in range(10):
                                time.sleep(1)
                                pbar.update(10)
                        a.gen()
                    else:
                        self.engine.say('its ok exiting please wait')
                        self.engine.runAndWait()
                        print('Exited')
                        print('               logged out from Deposit')
                        break

            else:
                self.engine.say('You have exceed maximum attempts try again later')
                print('ATTEMPTED 3 times')
                self.engine.runAndWait()
                print('               logged out from Deposit')
                break
            a.check_in()

    def withdrawl(self):
        count = 3
        z = True
        print('               logged in as withdrawal')
        while z:
            if count == 1 or count == 2 or count == 3:
                self.engine.say('Do you have account?')
                self.engine.runAndWait()
                with sr.Microphone() as source:
                    print('Listening...')
                    text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                sec_check = self.r.recognize_google(text1).lower()
                print('Your Response:', sec_check)
                if 'yes i had' in sec_check or 'i had' in sec_check or 'i do have' in sec_check:
                    self.engine.say('Please say your account name')
                    self.engine.runAndWait()
                    with sr.Microphone() as source:
                        print('Listening...')
                        text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                    self.wname = self.r.recognize_google(text1).lower()
                    print('Your Response:', self.wname)
                    if self.wname in self.d:
                        self.firstamount = self.d.get(self.wname)
                        self.engine.say('Please say your password')
                        self.engine.runAndWait()
                        with sr.Microphone() as source:
                            print('Listening...')
                            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                        self.pas = self.r.recognize_google(text1)
                        if self.pas == self.passwd.get(self.wname):
                            self.engine.say('Please say your withdrawal amount')
                            self.engine.runAndWait()
                            with sr.Microphone() as source:
                                print('Listening...')
                                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                            p = self.r.recognize_google(text1)
                            w = w2n.word_to_num(p)

                            from tqdm import tqdm, trange

                            with tqdm(total=100) as pbar:
                                for i in range(10):
                                    time.sleep(1)
                                    pbar.update(10)
                            if w <= self.d.get(self.wname) and self.d.get(self.wname) > 0:
                                z = self.fee * w
                                i = 0
                                res = self.d.get(self.wname) - z
                                c = self.d.get(self.wname)
                                v = self.d.get(self.wname) - w - z
                                t = self.d.get(self.wname) - w - i
                                k = self.d.get(self.wname)
                                self.d.update({self.wname: res})

                                if w > self.d.get(self.wname):
                                    self.engine.say('your account has insufficient balance')
                                    print('In sufficient balance')
                                    self.engine.runAndWait()
                                    self.d.update({self.wname: t})
                                    self.d.update({self.wname: k})


                                else:
                                    # self.d.update({wname: res})
                                    self.d.update({self.wname: v})
                                    q1 = self.d.get(self.wname)

                                    self.f2.write('\n' + self.wname + " " + str(v))
                                    self.engine.say(
                                        f"\n${z} will be debited as Bank fee charges 5% from account number:{self.accou.get(self.wname)}")
                                    print(
                                        f"\n${z} will be debited as Bank fee charges 5% , from account number:{self.accou.get(self.wname)}")
                                    self.engine.runAndWait()
                                    break
                            elif w > self.d.get(self.wname):
                                self.engine.say('your account has insufficient balance')
                                print('In sufficient balance')
                                self.engine.runAndWait()
                                break
                            else:
                                pass



                    else:
                        print('Wrong password try again!!!')
                        count = count - 1
                        self.engine.say('Do you want to try again or exit?')
                        self.engine.runAndWait()
                        with sr.Microphone() as source:
                            print('Listening...')
                            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                        z = self.r.recognize_google(text1).lower()
                        if 'yes' in z:
                            a.withdrawl()

                        else:
                            print('               logged out from withdrawal')
                            break
                else:
                    self.engine.say('First you must have an account to withdrawal amount')
                    self.engine.say("Do you want to redirect to account creating page or exit?")
                    self.engine.runAndWait()
                    with sr.Microphone() as source:
                        print('Listening...')
                        text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                    create_withdrawal = self.r.recognize_google(text1).lower()
                    if 'yes i will create' in create_withdrawal or 'yes i will' in create_withdrawal or 'i will ' \
                                                                                                        'create a ' \
                                                                                                        'new account' in \
                            create_withdrawal or 'i will' in create_withdrawal or 'i must' in create_withdrawal:
                        self.engine.say('its absolutely free to take')
                        self.engine.say('You will redirect to new page')
                        self.engine.runAndWait()
                        print('Redirecting...')
                        from tqdm import tqdm, trange
                        with tqdm(total=100) as pbar:
                            for i in range(10):
                                time.sleep(1)
                                pbar.update(10)
                        print('               logged out from withdrawal')

                        a.gen()
                        break
                    else:
                        self.engine.say('its ok exiting please wait')
                        self.engine.runAndWait()
                        print('Exited')
                        print('               logged out from withdrawal')
                        break
            else:
                self.engine.say('You have exceed maximum attempts try again later')
                print('ATTEMPTED 3 times')
                self.engine.runAndWait()
                print('               logged out from withdrawal')
                break
            a.check_in()

    def transfer(self):

        z = True
        print('               logged in as Transfer')
        while z:
            self.engine.say('Please say your account name')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            utrans = self.r.recognize_google(text1).lower()
            print('Your Response:', utrans)
            self.engine.say('Please say account name to transfer')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            trans = self.r.recognize_google(text1).lower()
            print('Your Response:', trans)
            self.engine.say('Please wait checking status of the accounts')
            print('Please wait checking accounts status...')
            self.engine.runAndWait()

            from tqdm import tqdm, trange
            with tqdm(total=100) as pbar:
                for i in range(10):
                    time.sleep(1)
                    pbar.update(10)

            if utrans in self.d.keys():
                if trans in self.d.keys():
                    self.engine.say('Both accounts are in active state you can proceed with transactions')
                    print('Accounts status:Active ')
                    self.engine.runAndWait()
                    self.engine.say('say amount to transfer')
                    self.engine.runAndWait()
                    with sr.Microphone() as source:
                        print('Listening...')
                        text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                    p = self.r.recognize_google(text1)
                    transamount = w2n.word_to_num(p)
                    print('Your Response:', transamount)
                    self.engine.say('Please wait Performing transactions')
                    print('Please wait Performing transactions...')
                    self.engine.runAndWait()

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
                        self.engine.say(
                            f'{transamount} has been successfully transferred from {utrans} to {trans} account')
                        print('Successfully transferred')
                        self.engine.runAndWait()
                        break

                    else:
                        self.engine.say(f'Insufficient balance in {utrans} account')
                        print(f'Insufficient balance in {utrans} account\n')
                        print('Try again!!!')
                        self.engine.runAndWait()
                        print('               logged out from transfer')
                        break

                else:
                    self.engine.say(f'sorry {trans} account not found')
                    print('Account status:Deactivated')
                    self.engine.runAndWait()
                    print('               logged out from transfer')
                    break

            else:
                self.engine.say(f'sorry {utrans} account not found')
                print('Account status:Deactive')
                self.engine.runAndWait()
                print('               logged out from transfer')
                break
        a.check_in()

    def balance(self):
        print('               logged in as balance')

        while True:
            self.engine.say(f'say your account name')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            ch = self.r.recognize_google(text1).lower()
            if ch in self.d.keys():
                print('Please wait Loading...')

                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                print(f"\nName:{ch} \nBalance:{self.d.get(ch)} \nAccount number:{self.accou.get(ch)}")
                self.engine.say(f"\nName:{ch} \nBalance:{self.d.get(ch)} dollars \nAccount number:{self.accou.get(ch)}")
                self.engine.runAndWait()
                print('               logged out from balance')
                break
            else:
                self.engine.say(f'Sorry account name {ch} not found')
                print(f'Sorry account name {ch} not found')
                self.engine.say('Try again later')
                self.engine.runAndWait()
                print('               logged out from balance')
                break
        a.check_in()


a = Bank()
a.bot()
