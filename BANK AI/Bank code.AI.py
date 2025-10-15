import pyttsx3 as p
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import datetime
import time
from word2number import w2n


class Bank:
    d = {}
    loan = {}
    loan_type = {}
    loan_date1 = {}
    loan_data = {}
    accou = {}
    passwd = {}
    loan_app = []
    loan_app_down = []
    fee = 0.05
    firstamount = 0
    f = open('General info(account).AI', 'a')
    f1 = open('Registered data.AI', 'a')
    f2 = open('balance_update.AI', 'a+')
    f3 = open('passwords.AI', 'a+')
    f4 = open('Account_number.Ai', 'a+')
    f5 = open('loan data.AI', 'a+')
    f6 = open('loan_up.AI', 'a+')
    f7 = open('loan_san_date.AI', 'a+')
    f8 = open('loan_down.AI', 'a+')
    h1 = open('data', 'a')
    r = sr.Recognizer()
    engine = p.init()

    rate = engine.getProperty("rate")
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 190)

    # engine.setProperty("voice", voices[0].id)

    def bot(self):
        self.b1 = datetime.datetime.now()
        self.begin = self.b1.strftime('%y-%m-%d on %H : %M : %S')
        self.engine.say('Hello Dear, welcome to BSBK bank')
        print('            Hello Dear welcome to BSBK bank')
        print('\n')
        self.engine.runAndWait()
        self.engine.say('Before proceeding system need to conform ,Do you need instructions? say yes or no')
        print('Before proceeding system need to conform ,Do you need instructions? say yes or no.')
        with sr.Microphone() as source:
            self.engine.say("I'm listening tell me now")
            self.engine.runAndWait()
            print('Listening...')
            text11 = self.r.listen(source, timeout=20, phrase_time_limit=10)
        intro1 = str(self.r.recognize_google(text11, language='en-IN')).lower()
        print('Your Response:', intro1)
        if 'yes' in intro1 or 's' in intro1 or 'i need them' in intro1:
            self.engine.say("I'm Alpha, your bank virtual assistant")
            self.engine.say('You can follow my instruction for any section to complete your process')
            self.engine.runAndWait()
            print('                    Instructions')
            print("1.Listening will be appeared on the screen so that you can speak with me")
            print('2.After Listening appeared on the screen you just have 15 sec time to speak with me , make sure '
                  'that your fast enough')
            print('3.Sometimes Listening may take a while to appear , please wait until Listening appeared on screen')
            print('4.Before proceeding to your process make sure that you are ready with required documents numbers')
            print('5.Please do avoid saying one word answer to me')
            print('Please check the status every moment that you conform.')
            self.engine.say('Please read this instructions carefully , or do you want me to read.')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                self.engine.say("I'm listening tell me now")
                self.engine.runAndWait()
                print('Listening...')
                text1 = self.r.listen(source, timeout=20, phrase_time_limit=10)
            intro = str(self.r.recognize_google(text1, language='en-IN')).lower()
            print('Your Response:', intro)
            if 'yes read it for me' in intro or 'yes read' in intro or 'read' in intro or 'yeah' in intro or 'red' in intro and 'no need i will read' not in intro or 'no problem' in intro:
                self.engine.setProperty("rate", 160)
                self.engine.say('I will instruct now, please make sure that you listen this instructions carefully.')
                self.engine.say('Listening will be appeared on the screen so that you can speak with me.')
                self.engine.say(
                    'After Listening appeared on the screen you just have 15 sec time to speak with me , make '
                    'sure '
                    'that you are fast enough.')
                self.engine.say('Some times Listening may take a while please wait until Listening appeared on screen.')
                self.engine.say(
                    'Before proceeding to your process make sure that you are ready with required documents or any id '
                    'proofs.')
                self.engine.say('Please do avoid saying one word answer to me.')
                self.engine.say('Please check the status every moment that you conform.')
                self.engine.runAndWait()
                self.engine.setProperty("rate", 190)
            else:
                self.engine.say('its ok then read carefully')
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
        else:
            self.engine.say('Alright dear , proceed carefully ')
            self.engine.say('Welcome to new Assistant services')
            self.engine.runAndWait()

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
        with open('loan data.AI', 'r') as fab:
            for i in fab:
                (key, val) = i.strip().split()
                self.loan[key] = int(val)
        with open('loan_san_date.AI', 'r') as fab:
            for i in fab:
                (key, val) = i.strip().split()
                self.loan_date1[key] = str(val)

        with open('loan_up.AI', 'r') as fab:
            for i in fab.readlines():
                self.loan_app.append(i.strip())
        with open('loan_down.AI', 'r') as fab:
            for i in fab.readlines():
                self.loan_app_down.append(i.strip())
        print(self.d)

        self.engine.setProperty("rate", 170)
        self.engine.say('You have currently this options')
        self.engine.say('I can create New account for you')
        print('\n')
        print('             Customer Modules')
        print('             New account')
        self.engine.say('I can do Deposits to your account')
        print('             Deposit')
        self.engine.say('I can help with Withdrawal money from your account')
        print('             Withdrawal')
        self.engine.say('I can help with providing loan for you.')
        print('             Loan')
        self.engine.say('And I can also Transfer money between accounts.')
        print('             Transfer')
        self.engine.say('And Even I check for balance of your account.')
        print('             Balance checking')
        self.engine.say('Finally i can also help you by providing bank statement for your account')
        print('             Bank statement')

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

                if "i need new account section" in s1 or "yeah new account" in s1 or 'new account' in s1 or 'i need ' \
                                                                                                            'new ' \
                                                                                                            'account' \
                        in s1:
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
                elif 'yeah loan' in s1 or 'i need loan section' in s1 or 'loan' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.g_loan()
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
                elif 'history statement for my account' in s1 or 'i need bank statement' in s1 or 'statement' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.history()
                elif 'change password' in s1:
                    a.change_password()

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
                elif 'yeah loan' in s1 or 'i need loan section' in s1 or 'loan' in s1:
                    print('Your Response:', s1)
                    self.engine.say('You will redirect to new page')
                    self.engine.runAndWait()
                    print('Redirecting...')
                    from tqdm import tqdm, trange
                    with tqdm(total=100) as pbar:
                        for i in range(10):
                            time.sleep(1)
                            pbar.update(10)
                    a.g_loan()

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
            if 'yes new account' in check_in or "new account section" in check_in or "yeah new account" in check_in or 'account' in check_in or 'create it' in check_in:

                self.engine.say('You will redirect to new page')
                self.engine.runAndWait()
                print('Redirecting...')
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                a.gen()
                break
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
                break
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
                break
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
                break
            elif 'yeah loan' in check_in or 'loan module' in check_in or 'loan' in check_in:

                self.engine.say('You will redirect to new page')
                self.engine.runAndWait()
                print('Redirecting...')
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                a.g_loan()
                break

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

            self.f.write(f'\nAccount created on {self.begin} ---->')
            self.engine.say('Say your pan card number for verification:')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, phrase_time_limit=10)
            self.engine.say('Say your Aadhaar number for identity verification:')
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
                    self.engine.say('Set name for your account generally account name must be account holder name')
                    print('CAUTION:please do remember the name of your account for future purposes')
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
                        self.engine.say('Please choose your password for your account')
                        self.engine.say('your password is encrypted by system')
                        time.sleep(10)
                        self.engine.say('Do your want to set your password by entering on keyboard')
                        time.sleep(5)
                        self.engine.say('Do your want to set your password by voice command')
                        self.engine.runAndWait()
                        with sr.Microphone() as source:
                            print('Listening...')
                            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                        text_passwords = self.r.recognize_google(text1, language='en-IN').lower()
                        if 'typing' in text_passwords or 'keyboard' in text_passwords or 'enter on keyboard ' in text_passwords:
                            self.engine.say('Please wait scanning keyboard')
                            print('Status: scanning...')
                            self.engine.runAndWait()
                            self.password = int(input('Enter your password:'))
                            self.passwd.update({self.name: self.password})
                        else:
                            self.engine.say('Set your password')
                            with sr.Microphone() as source:
                                print('Listening...')
                                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                            pass_word = self.r.recognize_google(text1, language='en-IN')
                            self.password = w2n.word_to_num(pass_word)
                            print('Your Response: password encrypted by system')

                        self.f.write(f' PAN card number:{self.p1}')
                        self.f1.write(f'\nAccount created on {self.begin} ---->')
                        self.f1.write(f'Name:{self.name}')
                        self.f1.write(f' Account number:{id(self.name)}')
                        self.f.write(f' Age :{str(self.age)}')
                        self.f2.write('\n' + self.name + " " + str(self.firstamount))
                        self.f.write(f' AADHAAR number:{self.a1}')
                        self.f4.write('\n' + self.name + " " + str(id(self.name)))
                        self.f3.write('\n' + self.name + " " + str(self.password))
                        self.f1.write(f' Password:{str(self.password)}')
                        self.h1.write(f"\n{self.name} last login:{str(begin)}")
                        self.h1.write(f'\n{self.name} created account on {self.begin}')
                        self.passwd.update({self.name: self.password})
                        self.engine.say(f'Dear {self.name} your account was successfully created and will be '
                                        f'activated  within 48 hours')
                        self.engine.runAndWait()
                        print('Please wait preparing passbook')
                        self.engine.say('Please wait preparing passbook')
                        self.engine.runAndWait()
                        print('Status:Waiting...')
                        time.sleep(20)

                        from fpdf import FPDF
                        my_pdf = FPDF()
                        my_pdf.add_page()
                        my_pdf.set_font('Arial', size=16)
                        my_pdf.cell(200, 20, txt='BSBK BANK', ln=1, align='C')
                        txt = f'Date: {self.begin}'
                        my_pdf.cell(340, 20, txt=txt, ln=1, align='C')
                        txt = f"Account number: {id(self.name)}"
                        my_pdf.cell(50, 20, txt=txt, ln=1, align='A')
                        txt = f'Customer name: {self.name}'
                        my_pdf.cell(50, 20, txt=txt, ln=1, align='A')
                        txt = 'Email:XXXXXXXXXXXXXX'
                        my_pdf.cell(50, 20, txt=txt, ln=1, align='A')
                        txt = "Branch:HYD"
                        my_pdf.cell(300, 10, txt=txt, ln=1, align='C')
                        txt = "Branch code:HYD-9014"
                        my_pdf.cell(329, 20, txt=txt, ln=1, align='C')
                        txt = 'Toll Free: xxxxxxxxxx'
                        my_pdf.cell(50, 20, txt=txt, ln=1, align='A')
                        print('P D F , E-passbook will be created please keep name for your passbook pdf file ')
                        self.engine.say(f'PDF e-passbook will be created please keep name for your passbook pdf file ')
                        self.engine.runAndWait()
                        o = str(input('Enter your pdf file name:'))
                        x = '.pdf'
                        ans = o + x
                        my_pdf.output(f'{ans}')
                        print(
                            f'Dear,{self.name} your e-passbook has been successfully created please check in left side of your files.')
                        self.engine.say(
                            f'Dear,{self.name} your e-passbook has been successfully created please check in left side of your files.')
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
                        self.engine.say('do you want say your password or manually enter on keyboard?')
                        self.engine.runAndWait()
                        with sr.Microphone() as source:
                            print('Listening...')
                            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                        text_passwords = self.r.recognize_google(text1, language='en-IN').lower()
                        if 'typing' in text_passwords or 'keyboard' in text_passwords or 'enter on keyboard ' in text_passwords:
                            self.engine.say('Please wait scanning keyboard')
                            print('Status: scanning...')
                            self.engine.runAndWait()
                            time.sleep(10)
                            self.pas = str(input('Enter your password:'))

                        else:
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
                            self.now_amount = self.firstamount
                            self.firstamount = n + self.firstamount
                            print('Please wait Processing Deposit...')
                            from tqdm import tqdm, trange
                            with tqdm(total=100) as pbar:
                                for i in range(10):
                                    time.sleep(1)
                                    pbar.update(10)
                            self.h1.write(f'\n{self.den} deposited:{str(self.now_amount)} on {str(self.begin)}')
                            self.f2.write('\n' + self.den + " " + str(self.firstamount))
                            print(
                                f"Bank fee charges 5% only ${n} will credited to acc number:{self.accou.get(self.den)} ")
                            self.engine.say(
                                f"Bank fee charges 5% only ${n} will credited to acc number:{self.accou.get(self.den)} ")
                            self.engine.runAndWait()
                            print(f'Dear , {self.den} amount has been successfully deposited to your account.')
                            self.engine.say(
                                f'Dear , {self.den} amount has been successfully deposited to your account.')
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
                                break
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
                                break

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
                        break
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
            break

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
                        self.engine.say('Do you want to say your password or enter manually on keyboard?')
                        self.engine.runAndWait()
                        with sr.Microphone() as source:
                            print('Listening...')
                            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                        text_passwords = self.r.recognize_google(text1, language='en-IN').lower()
                        if 'typing' in text_passwords or 'keyboard' in text_passwords or 'enter on keyboard ' in text_passwords:
                            self.engine.say('Please wait scanning keyboard')
                            print('Status: scanning...')
                            self.engine.runAndWait()
                            time.sleep(10)
                            self.pas = int(input('Enter your password:'))
                        else:
                            with sr.Microphone() as source:
                                print('Listening...')
                                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                            self.pas = self.r.recognize_google(text1)
                        self.engine.say('Your password was highly encrypted by system.')
                        print('Your Response:Password encrypted')
                        self.engine.runAndWait()
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
                                    self.h1.write(f'\n{self.wname} withdrawed:{str(v)} on {self.begin}')
                                    self.engine.say(
                                        f"\n${z} will be debited as Bank fee charges 5% from account number:{str(self.accou.get(self.wname))}")
                                    print(
                                        f"\n${z} will be debited as Bank fee charges 5% , from account number:{self.accou.get(self.wname)}")
                                    self.engine.say(
                                        f'Dear {self.wname} your withdrawal amount was suceesufully debited from your account ')
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
                            break

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
                        self.h1.write(f'\n{utrans} Transferred:{transamount} on {self.begin}')
                        self.h1.write(f'\n{trans} Received:{transamount} on {self.begin}')
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
                self.engine.say('Please wait Loading...')
                self.engine.runAndWait()

                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                acc = str(self.accou.get(ch))
                print(f"\nName:{ch} \nBalance:{self.d.get(ch)} \nAccount number:{self.accou.get(ch)}")
                self.engine.say(
                    f"\nName:{ch} \nBalance:{self.d.get(ch)} dollars \nAccount number:{acc}")
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

    def history(self):
        print('               logged in as history')
        self.engine.say('Say your name')
        self.engine.runAndWait()
        with sr.Microphone() as source:
            print('Listening...')
            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
        name = self.r.recognize_google(text1).lower()
        print('Your Response:', name)
        self.engine.say('Say your password')
        self.engine.say('Your password is highly encrypted by system')
        self.engine.runAndWait()
        with sr.Microphone() as source:
            print('Listening...')
            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
        password = self.r.recognize_google(text1)
        print('Your Response:Your password is Encrypted can not be shown')
        if password == self.passwd.get(name):
            self.engine.say(f'You have successfully logged in dear,{name}')
            print('Status:Correct')
            self.engine.say(f'Please wait preparing history statement')
            print('Preparing...')
            self.engine.runAndWait()
            from tqdm import tqdm, trange
            with tqdm(total=100) as pbar:
                for i in range(10):
                    time.sleep(1)
                    pbar.update(10)
            with open('data', 'r') as fq:
                x = 0
                z = 0
                for i in fq.readlines():
                    if name in i.split():
                        print(i)
                        x = 1
                        z = 1
                    else:
                        x = 0
                        pass
                if x == 0 and z == 0:
                    print('not found')
                else:
                    pass
        else:
            self.engine.say(f'Dear {name},you have entered Wrong password please check and try again')
            print('Status:Wrong password')
            self.engine.runAndWait()
            print('               logged out from history')
            a.history()
        a.check_in()

    def change_password(self):
        print('               logged in as forgotten password')
        print('Caution:Forgotten password may take a long moment and without valid information account '
              'passwords cant be changed')
        self.engine.say('Caution:Forgotten password may take a long moment and without valid information account '
                        'passwords cant be changed')
        print('Incase of misuse the passwords bank is not responsible for this activities')

        self.engine.say('Incase of misuse the passwords bank is not responsible for this activities')
        print('You can proceed for changing your account password by accepting all terms and conditions')
        self.engine.say('You can proceed for changing your account password by accepting all terms and conditions')
        print('Say Yes to agree or No to stop process')
        self.engine.say('Say Yes to agree or No to stop process')
        self.engine.runAndWait()
        with sr.Microphone() as source:
            print('Listening...')
            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
        agree = self.r.recognize_google(text1).lower()
        print('Your Response:', agree)
        if 'yes' in agree or 's' in agree:
            self.engine.say('Please conform it again to proceed')
            print('Please conform it again to proceed\nSay Yes to agree or No to stop process')
            self.engine.say('Say Yes to agree or No to stop process')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)

            agree1 = self.r.recognize_google(text1).lower()
            print('Your Response:', agree1)
            if 'yes' in agree1 or 's' in agree1:
                self.engine.say('Please say your account name')
                self.engine.runAndWait()
                with sr.Microphone() as source:
                    print('Listening...')
                    text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                name = self.r.recognize_google(text1).lower()
                print('Your Response:', name)
                self.engine.say('Please wait searching account...')
                print('Please wait searching account...')
                self.engine.runAndWait()
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                if name in self.passwd.keys():
                    self.engine.say(f'{name} account found')
                    self.engine.runAndWait()
                    self.engine.say(f'Please say your new password')
                    self.engine.runAndWait()
                    with sr.Microphone() as source:
                        print('Listening...')
                        text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                    self.new_pass = self.r.recognize_google(text1)
                    print('Your Response:', self.new_pass)
                    self.engine.say('Changed password will be updated within 9 hours')
                    self.engine.say('Incase of any emergency you can proceed with old password')
                    self.engine.runAndWait()
                    self.passwd.update({name: self.new_pass})
                    self.f3.write('\n' + name + " " + str(self.new_pass))
                    self.h1.write(f'\n{name} changed password on {self.begin}')
                    print('               logged out from forgotten password')

                else:
                    self.engine.say(f'{name} account not found')
                    self.engine.runAndWait()
                    print('               logged out from forgotten password')
            else:
                self.engine.say(f'Exited')
                self.engine.runAndWait()
                print('               logged out from forgotten password')

        else:
            self.engine.say(f'Exited')
            self.engine.runAndWait()
            print('               logged out from forgotten password')

    def g_loan(self):
        print('               logged in as loan')
        count = 0
        self.engine.say(f'Hey, Hi welcome to loan module')
        self.engine.runAndWait()
        print('Please say your account name')
        self.engine.say(f'Please say your account name')
        self.engine.runAndWait()
        with sr.Microphone() as source:
            print('Listening...')
            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
        self.loan_name = self.r.recognize_google(text1).lower()
        print('Your Response:', self.loan_name)
        self.engine.say('Please wait validating your account')
        print('Please wait validating your account...')
        self.engine.runAndWait()
        from tqdm import tqdm, trange
        with tqdm(total=100) as pbar:
            for i in range(10):
                time.sleep(1)
                pbar.update(10)
        if self.loan_name in self.d.keys():
            self.engine.say(f'Hi , {self.loan_name} your account was verified successfully.')
            self.engine.runAndWait()
            self.engine.say('Do you want to take loan or Do you want to clear your loan.')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            agree3 = self.r.recognize_google(text1).lower()
            print('Your Response: ', agree3)
            if 'yes' in agree3 or 'i want to take loan' in agree3:
                self.engine.say(f'You have currently these loan types')
                print('''
                             1.Educational Loan
                             2.House Loan
                             3.Financial Loan
                             4.General Loan''')
                self.engine.say('Please choose any of them')
                self.engine.runAndWait()
                self.engine.say(f'Please say your loan type')
                self.engine.runAndWait()
                with sr.Microphone() as source:
                    print('Listening...')
                    text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                self.loan_type_assi = self.r.recognize_google(text1).lower()
                print('Your Response: ', self.loan_type_assi)
                if 'educational loan' in self.loan_type_assi or 'education loan' in self.loan_type_assi or 'education' in self.loan_type_assi:
                    count = count + 1
                    a.loan_san(count)
                elif 'house loan' in self.loan_type_assi:
                    count = count + 2
                    a.loan_san(count)
                elif 'financial loan' in self.loan_type_assi:
                    count = count + 3
                    a.loan_san(count)
                elif 'general loan' in self.loan_type_assi:
                    count = count + 4
                    a.loan_san(count)
                elif 'request loan' in self.loan_type_assi:
                    count = count + 5
                    a.t_bank_sys()

            else:
                self.engine.say('Please wait redirecting to new page')
                self.engine.runAndWait()
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                a.loan_ret()

    def loan_san(self, count):
        print('               logged in to loan sanctioning module.')
        loan_trans = 0
        intreset = 10
        if count == 1 and (self.loan_name not in self.loan_app or self.loan_name in self.loan_app_down):
            print(f'Welcome, {self.loan_name} to the Educational Loan module.')
            self.engine.say(f'Welcome, {self.loan_name} to the educational loan module.')
            self.engine.runAndWait()
            self.engine.say(f'Please provide your institution admission loan number')
            self.engine.say('If you cant find it, please refer to the right top of your institution admission document')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            admission_num = self.r.recognize_google(text1, language='en-IN')
            print('Your Response:', admission_num)
            self.engine.say('Please wait conforming with the institution.')
            self.engine.runAndWait()
            from tqdm import tqdm, trange
            with tqdm(total=100) as pbar:
                for i in range(10):
                    time.sleep(1)
                    pbar.update(10)
            self.engine.say(
                f'{self.loan_name} your admission was validated, with all clearances.You can proceed for next step.')
            self.engine.runAndWait()
            print('Educational Loan Interest rate 10% over a 1 year period of time')
            self.engine.say('Educational Loan Interest rate 10% over a 1 year period of time')
            self.engine.runAndWait()
            self.engine.say('Please say how much amount you want from loan')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            am_l = self.r.recognize_google(text1, language='en-IN')
            self.loan_amount = w2n.word_to_num(am_l)
            print('Your Response:', self.loan_amount)
            self.engine.say(f'Loan Amount has been deposited to your account number {self.accou.get(self.loan_name)}')
            self.engine.runAndWait()
            from datetime import date
            import datetime
            x = datetime.datetime.now()
            self.f_date = date(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")))
            self.loan_type.update({self.loan_name: 'Educational_loan'})
            # self.loan_date.update({self.loan_name:{'san_date':self.f_date}})
            self.f5.write('\n' + self.loan_name + " " + str(self.loan_amount))
            bal = self.loan_amount + self.d.get(self.loan_name)
            self.f2.write('\n' + self.loan_name + " " + str(bal))
            self.loan_app.append(self.loan_name)
            self.f6.write('\n' + self.loan_name)
            self.f7.write('\n' + self.loan_name + " " + str(self.f_date))
            self.h1.write('\n' + self.loan_name + " " + 'has taken loan from bank')
            print('               logged out from loan sanctioning module.')
            a.check_in()

    def loan_ret(self):
        print('               logged in to loan clear module.')
        self.engine.say(f'Welcome, to loan retrieval process')
        self.engine.runAndWait()
        self.engine.say('Please say your account name for loan cancellation process:')
        self.engine.runAndWait()
        with sr.Microphone() as source:
            print('Listening...')
            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
        self.loan_ret_name = self.r.recognize_google(text1).lower()
        print('Your Response: ', self.loan_ret_name)
        if self.loan_ret_name in self.loan:
            self.engine.say('Please wait preparing documents and statements.')
            self.engine.runAndWait()
            from tqdm import tqdm, trange
            with tqdm(total=100) as pbar:
                for i in range(10):
                    time.sleep(1)
                    pbar.update(10)
            print(f'{self.loan_ret_name} you have taken loan amount {self.loan.get(self.loan_ret_name)} dollars')
            self.engine.say(
                f'{self.loan_ret_name} you have taken loan amount {self.loan.get(self.loan_ret_name)} dollars, and your loan type was {self.loan_type.get(self.loan_ret_name)}')
            self.engine.say('In order of clear loan please pay full amount with interest.')
            self.engine.runAndWait()
            time.sleep(5)
            from datetime import date
            import datetime
            x = datetime.datetime.now()
            l_date = date(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")))
            x1 = self.loan_date1.get(self.loan_ret_name).split('-')
            f1_date = date(int(x1[0]), int(x1[1]), int(x1[2]))
            delta = l_date - f1_date
            p = self.loan.get(self.loan_ret_name)
            r = 10
            s1 = (p * r * delta.days) / 100
            s = s1 * (1 / 365)
            self.engine.say(
                f'{self.loan_ret_name},you have taken an loan amount {self.loan.get(self.loan_ret_name)} dollars,'
                f'over a time period {delta.days} days and your interest amount was {s} dollars ')
            print(f'{self.loan_ret_name},you have taken an loan amount {self.loan.get(self.loan_ret_name)} dollars,'
                  f'over a time period {delta.days} days and your interest amount was {s} dollars ')
            self.engine.runAndWait()
            time.sleep(5)
            self.engine.say(f'Your amount can be paid through self banking account')
            print(
                'Your amount can be paid through self banking account,Please say Yes to proceed or No to stop process')
            self.engine.say('Please say Yes to proceed or No to stop process')
            self.engine.runAndWait()
            print('Caution:If "NO" your loan will not clear and will be continued.')
            self.engine.say('Caution If NO your loan will not clear and will be continued.')
            print('If "Yes" your loan amount plus interest amount will be deducted from your account.')
            self.engine.say(
                'If Yes your loan amount plus interest amount will be cleared and deducted from your account.')
            self.engine.runAndWait()
            time.sleep(10)
            self.engine.say('Please say I am listening.')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            loan_can = self.r.recognize_google(text1, language='en-IN').lower()
            print('Your Response: ', loan_can)
            if 'yes' in loan_can:
                self.engine.say('Please wait getting ready with loan clearance documents')
                print('Please wait getting ready with loan clearance documents...')
                self.engine.runAndWait()
                from tqdm import tqdm, trange
                with tqdm(total=100) as pbar:
                    for i in range(10):
                        time.sleep(1)
                        pbar.update(10)
                t = self.d.get(self.loan_name)
                dud = t - (p + s)
                cut = self.d.get(self.loan_ret_name) - dud
                if self.d.get(self.loan_ret_name) >= dud:
                    if cut == 0:
                        self.engine.say(f'{self.loan_ret_name} there is a caution in your balance.')
                        self.engine.say('If you proceeding to clear your loan, your account balance will be zero')
                        self.engine.say('If you want to proceed please say Yes or No to stop process')
                        self.engine.runAndWait()
                        with sr.Microphone() as source:
                            print('Listening...')
                            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                        agree1 = self.r.recognize_google(text1).lower()
                        print('Your Response:', agree1)
                        if 'yes' in agree1 or 'proceed' in agree1:
                            self.engine.say('Deducting amount from your account')
                            print('Deducting amount from your account...')
                            self.engine.runAndWait()
                            from tqdm import tqdm, trange
                            with tqdm(total=100) as pbar:
                                for i in range(10):
                                    time.sleep(1)
                                    pbar.update(10)

                            self.engine.say('Changes may take a while')
                            self.engine.runAndWait()
                            time.sleep(5)
                            self.engine.say(f'{self.loan_ret_name}, you have successfully cleared your loan amount '
                                            f'Please wait for loan clearance number will be generated')
                            self.engine.runAndWait()
                            print('Waiting...')
                            time.sleep(20)
                            clr = str(id(self.loan_ret_name))
                            self.engine.say(
                                f'Dear {self.loan_ret_name}, your loan clear reference number is {str(id(self.loan_ret_name))} please keep it for reference.')
                            print(
                                f'Dear {self.loan_ret_name}, your loan clear reference number is {clr} please keep it for reference.')
                            self.engine.runAndWait()
                            print('               logged out from loan clear module.')
                            self.f8.write('\n' + self.loan_ret_name)
                            self.f2.write('\n' + self.loan_ret_name + " " + str(self.d.get(self.loan_ret_name) - cut))
                            self.f5.write('\n' + self.loan_ret_name + " " + str(0))

                        else:
                            self.engine.say(f'Your amount will be not deducted and loan will be cleared')
                            self.engine.say(
                                'Do you want me to take to deposit module to add amount and clear your loan')
                            self.engine.say('Please say Yes or No')
                            with sr.Microphone() as source:
                                print('Listening...')
                                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
                            agree2 = self.r.recognize_google(text1).lower()
                            print('Your Response:', agree2)
                            if 'yes' in agree2:
                                a.deposit()
                            else:
                                self.engine.say(f'Thank you {self.loan_ret_name}')
                                print(f'Thank you {self.loan_ret_name}')
                                self.engine.runAndWait()
                                print('               logged out from loan clear module.')
                                a.check_in()

                    else:
                        self.engine.say('Deducting amount from your account')
                        print('Deducting amount from your account...')
                        self.engine.runAndWait()
                        from tqdm import tqdm, trange
                        with tqdm(total=100) as pbar:
                            for i in range(10):
                                time.sleep(1)
                                pbar.update(10)

                        self.engine.say('Changes may take a while')
                        self.engine.runAndWait()
                        time.sleep(5)
                        self.engine.say(f'{self.loan_ret_name}, you have successfully cleared your loan amount '
                                        f'Please wait for loan clearance number will be generated')
                        self.engine.runAndWait()
                        print('Waiting...')
                        time.sleep(20)
                        clr = str(id(self.loan_ret_name))
                        self.engine.say(
                            f'Dear {self.loan_ret_name}, your loan clear reference number is {str(id(self.loan_ret_name))} please keep it for reference.')
                        print(
                            f'Dear {self.loan_ret_name}, your loan clear reference number is {clr} please keep it for reference.')
                        self.engine.runAndWait()
                        self.f2.write('\n' + self.loan_ret_name + " " + str(self.d.get(self.loan_ret_name) - cut))
                        self.f8.write('\n' + self.loan_ret_name)
                        self.f5.write('\n' + self.loan_ret_name + " " + str(0))
                        print('               logged out from loan clear module.')
                        a.check_in()
                else:
                    self.engine.say(f"{self.loan_ret_name} , your balance was low for clearing loan amount")
                    print(
                        f'{self.loan_ret_name} , your balance was low for clearing loan amount , Please deposit money in your account and pay again')
                    self.engine.say('Please deposit money and pay again')
                    self.engine.runAndWait()
                    print('               logged out from loan clear module.')
                    a.check_in()
    def bank_sys(self,l):
        if self.identity != 0:
            a.p_bank_sys()
        else:
            pass


    def t_bank_sys(self):
        self.identity = 0
        for i in self.d:
           if self.d.get(i) > 100000:
               print(i)
               a.t_loan_user()


    def p_bank_sys(self):
      global l1
      if self.select == 'yes':
            l1=a.p_loan_user()
            if l1 == 'yes':
               a.fixed_loan()



    def t_loan_user(self):
        self.engine.say('Please select your loan provider')
        print('Please select your loan provider')
        self.engine.runAndWait()
        with sr.Microphone() as source:
            print('Listening...')
            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
        self.select = self.r.recognize_google(text1).lower()
        print('Your Response:', self.select)
        self.engine.say('Please wait')
        print('Please wait...')
        self.engine.runAndWait()
        time.sleep(5)
        self.engine.say('Your Request has been sent to selected provider.')
        print('Your Request has been sent to selected provider.')
        self.engine.say('You will be intimated soon as possible when provider has granted your request.')
        self.engine.say('Please check for updates to your loan request by logging into your account.')
        print('You will be intimated soon as possible within one day when provider has granted your request.Please check for updates to your loan request by logging into your account.')
        print('NOTICE:PLEASE CHECK FREQUENTLY FOR UPDATES')
        self.engine.runAndWait()
        a.t_msg()
    def p_loan_user(self):
        self.engine.say(f'Hello {self.select} you have a request from user.')
        self.engine.say(f'You are request to give loan to user.')
        self.engine.runAndWait()
        self.engine.say('Please say yes or no.')
        self.engine.runAndWait()

        with sr.Microphone() as source:
            print('Listening...')
            text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
        select1 = self.r.recognize_google(text1).lower()
        if select1 == 'yes':
            return select1
        else:
            return select1
    def t_msg(self):
        a.bank_sys(self.select)
        pass
    def g_msg(self):
        a.bank_sys(self.select)


    def fixed_loan(self):
        print('You are providing loan to user by assurance with bsbk bank')
        print('please wait fetching information')
        print('Now you will redirect to tranfer module please transfer money.')
        print('You will shortly get details.')
        from tqdm import tqdm, trange
        with tqdm(total=100) as pbar:
            for i in range(10):
                time.sleep(1)
                pbar.update(10)
        print('User datails')
        res1 = a.fixed_transfer()


    def fixed_transfer(self):
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
                        self.h1.write(f'\n{utrans} Transferred:{transamount} on {self.begin}')
                        self.h1.write(f'\n{trans} Received:{transamount} on {self.begin}')
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
        return 1
    def notify(self):
        z = True
        print('               logged in as Transfer')
        while z:
            self.engine.say('Please say your account name')
            self.engine.runAndWait()
            with sr.Microphone() as source:
                print('Listening...')
                text1 = self.r.listen(source, timeout=15, phrase_time_limit=10)
            notify = self.r.recognize_google(text1).lower()
            print('Your Response:', notify)
            self.engine.say('Please say account name')
            self.engine.runAndWait()
            print('Please wait checking account status...')
            self.engine.runAndWait()
            from tqdm import tqdm, trange
            with tqdm(total=100) as pbar:
                for i in range(10):
                    time.sleep(1)
                    pbar.update(10)
            if notify in self.d.keys():
                    print('Accounts status:Active ')













a = Bank()
a.bot()
