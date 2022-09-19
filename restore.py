import subprocess , socket
drive = input('drive you have your file in(optional,type "n" if none: ')
path = input('enter path to restore your files(if the above input is "n",this will be ignored): ')
print('app restorer')
a = input('is this a linux machine?[y/n]: ')
print(socket.gethostname())
if a == 'n':
        quit()
print('uptading the apt package manager...')
update_apt = subprocess.run('sudo apt update' ,  shell = True)
print('updating the apt-get package manager...')
update_get = subprocess.run('sudo apt-get update' , shell=True)
print('The apt package manager was updated successfully.')
packages_needed = ['opencv-python',
'colorama',
'requests',
'pyautogui',
'pygame',
'playsound',
'ursina',
'pytube',
'shutil',
'psutil'
]
print('installing needed python packages.....')
for package in packages_needed:
        print('installing package: ' + str(package))
        try:
                install = subprocess.run('pip3 install ' + package , shell = True)
                print(package + ' was installed successfully')
        except:
                print(package + ' failed to be installed')
print('installed needed packages')
import shutil
from colorama import Fore
print(Fore.GREEN + 'installing needed programs...')
print('installing vscode')
print(Fore.RESET)
subprocess.run('sudo snap install --classic code' , shell = True)
print(Fore.GREEN + 'vscode was installed successfully.')
print('installing brave')
print(Fore.RESET)
subprocess.run('sudo apt install -y brave-browser' , shell = True)
print(Fore.GREEN + 'brave browser was installed successfully.')
print('installing VLC Media Player')
print(Fore.RESET)
subprocess.run('sudo snap install vlc' , shell = True)
print(Fore.GREEN + 'VLC Media Player was installed successfully.')
print('Applications were restored successfully.')
if drive == 'n':
        print('exiting....')
        quit()
print('Restoring Files..')
if '\\' in drive:
        drive = drive.replace('\\' , '/')
if '\\' in path:
        path = path.replace('\\' , '/')
shutil.copytree(drive , path)
print('Files have been restored successfully.')
#project restore is complete