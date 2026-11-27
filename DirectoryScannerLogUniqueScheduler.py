####################################################################################
#
#   Importing required libraries
#
####################################################################################

import sys
import os
import time
import schedule

##############################################################################################################################
#
#   Function Name : DirectoryScanner
#   Input         : DirectoryPath
#   Description   : function scans a folder and all its subfolders, then writes a timestamped list of every filename into a new log file.
#   Date          : 31/07/2026
#   Author        : Himani Ramesh Salunkhe
#
###############################################################################################################################

def DirectoryScanner(DirectoryPath = "Marvellous"):
    Border = "-"*40
    timestamp = time.ctime()
    logfilename = "Marvellous%s.log"%(timestamp)    
    logfilename = logfilename.replace(" ","_")
    logfilename = logfilename.replace(":","_")
    
    print("LogFile gets created with name : ",logfilename)

    fobj = open(logfilename,"w")

    fobj.write(Border+"\n\n")
    fobj.write("Marvellous Automation Script \n")
    fobj.write(Border+"\n\n")

    fobj.write("Files from the directory are : \n\n")
    fobj.write(Border+"\n")

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for Fname in FileName:
            fobj.write(Fname+"\n")

    fobj.write(Border+"\n")
    fobj.write("Log file gets created at : "+timestamp)
    fobj.write("\n"+Border+"\n")
    
    fobj.close()        

##############################################################################################################################
#
#   Function Name : main
#   Input         : Command line arguments
#   Description   : It controls the script
#   Date          : 31/07/2026
#   Author        : Himani Ramesh Salunkhe
#
###############################################################################################################################

def main():
    Border = "-"*80
    print(Border) 
    print("Marvellous Automation Script")
    print(Border)
    
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("For better usage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")

        else:    
           
            schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])

            while(True):    
                schedule.run_pending()
                time.sleep(1)
               
        
    else:
        print("Invalid number of arguments")
        print("Please use --h or --u for more information")
    

    print(Border)
    print("Thanking for using Marvellous Automation Script")
    print(Border)

####################################################################################
#
#   Starter of the automation script
#
####################################################################################

if __name__ =="__main__":
    main()