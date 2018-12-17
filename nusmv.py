import os
import commands

username = commands.getoutput("echo $USERNAME")
path = "/home/" + username + "/NuSMV-2.6.0-Linux/bin/NuSMV -int"
os.system(path)
