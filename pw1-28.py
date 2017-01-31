#! /usr/bin/python3
import sys
import pyperclip
import os.path
#this is an insecure password storing program


          
def listfill():
    account=input('Name of account? : ')   #The only reason this doesnt overwrite the earlier "account"
    acctlist.append(account)                      #is because it is in a function right?
    pwordlist.append(input(' Please enter the password for this account....'))
    print(' The account ' + account + ' and its password have been added. Thank you.')
    repeat = input('Add more?')
    if repeat.lower() == 'yes':
        listfill()
    else:
        savechanges()
        print('Database Modified')
        sys.exit()

def savechanges():
    for i in range(len(acctlist)):
        if acctlist[i] not in initlist:
            entry = ('username : ' + acctlist[i] + '|' + 'password : ' + pwordlist[i]+'\n')
            pword.write(entry)
#----------------------------------------------------------
acctlist = []
pwordlist= []

initlist = []

if not os.path.exists("./pworddatabase.txt"):  #or it propagates list of account and passwords
    pword = open('pworddatabase.txt', 'w')
    listfill()
               
else:
    pword = open('pworddatabase.txt', 'r+')
    for line in pword.readlines():# reads txt database
        accountsplit = line.strip().split('|')  
        accountitem= accountsplit[0].split(' : ')[1]    ##splits database lines
        passworditem = accountsplit[1].split(' : ')[1]

        acctlist.append(accountitem) #put these into a list
                        
        pwordlist.append(passworditem) #put these into a list
    for i in acctlist:
        initlist += [i, pwordlist[acctlist.index(i)]]#makes sure save fct creates no duplicate entries
    #print (initlist)
#------------------------------------------------------
if len(sys.argv) < 2:
    print('Usage: python pw.py [ account ] - copy account password')
    print('Arument : \"*INPUT*\" to go directly to input mode.')
    print ((sys.argv[0]))

    sys.exit()

account = sys.argv[1]  # first command line argument is account name
#this bothers me, i feel like it should be at the beginning or end, but it only works here haha. Any ideas?
#------------------------------------------

if acctlist == []:
    fillgo = input('You have no saved passwords...Type \'yes\' to enter Input Mode')
    if fillgo.lower() == 'yes':
        listfill()

if account in acctlist:
    pyperclip.copy(pwordlist[acctlist.index(account)])
    print('Password for ' + account + ' copied to clipboard.')
    sys.exit()

if account == '*INPUT*':
    listfill()

else:
    print('There is no account called ' + account +'... \n Would you like to add it?')

    addChoice = input()
    if addChoice.lower() == 'yes':
        listfill()
        '''accntlist.append(account)
        pwordlist.append(input(' Please enter the password for this account.'))
        print(' The account ' + account + ' and its password have been added. Thank you.')
      
        sys.exit()'''



                              
#account = sys.argv[1]  # first command line argument is account name
    
