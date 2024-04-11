import subprocess
from time import sleep

#Class Created Ghostnet
class Ghostnet:
    def __init__(self,directory_path):
        self.directory_path = directory_path
        #self.command = command
    
    #Code to change the Directory where IPFS Located   
    def change_path(self):

        try:
            ans = subprocess.run(["cd",self.directory_path],shell=True,check=True)
            print(f"Changed directory to {self.directory_path}")
    
        except subprocess.CalledProcessError as e:
            print(f"Command failed {e.returncode}")
    
    #Access the IPFS-CLI Commands
    def check_ipfs(self,command):
        try:
            res = subprocess.run([".\ipfs",command],shell=True,check=True)
            print(f"the version of IPFS is{res}")
        except subprocess.CalledProcessError as e:
            print(f"Command failed {e.returncode}")

ghost = Ghostnet("D:\Ghostnet\IPFS")
ghost.change_path()
sleep(3)
ghost.check_ipfs("--version")
ghost.check_ipfs("daemon")


