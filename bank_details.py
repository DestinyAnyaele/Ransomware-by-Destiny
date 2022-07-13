import random,string,colorama,time
sum = 0

'''checking if payments have been done and if amount is
enough'''
def money_logger(money) :
    colorama.init(autoreset = True)
    if money < 1000 :
        print(colorama.Fore.RED + 'pay me more money ....')
        bank_info()
    else :
        print('your files will soon be decrypted')
    
    
    
# giving bank information 
def bank_info() :
    print('generating payment address')
    print('This is a one time address')
    address = random.sample(string.ascii_letters,20)
    address = ''.join(str(k) for k in address) 
    print('pay to this = ',address)
    print(colorama.Style.RESET_ALL)
    try : 
        amount = int(input('How much have you paid : '))
        print('Checking payment if True')
#        time.sleep(4)
    except Exception as message :
        print('Enter only digits')
        bank_info()
    else :
        global sum
        sum += amount    
        money_logger(sum)
