#Version 0.1 Alpha
#Configurable
import os

#Configurable
i = 0

#Main Code
while(i == 0):
  shell = input("#")
  if(shell == "clr"):
    #Configurable (Linux/Macos use "clear", Windows use "CLR")
    os.system("clear")
  elif(shell == "sh"):
    while(i == 0):
      sh = input("$")
      if(sh == "exit"):
        break
      #Configurable (sh, bash, zsh, (cmd, powershell for windows user only!))
      os.system(sh)
  else:
    #Executing the code using python
    exec(shell)

