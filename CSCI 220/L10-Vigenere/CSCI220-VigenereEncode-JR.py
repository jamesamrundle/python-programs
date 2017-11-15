#CSCI220-VigenereEncode-JR.py
#James Rundle
#puts a Vigenere encryption on a string provided from a file. Writes results to new file
from graphics import *


alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def GUI():
    win = GraphWin("CaesarEncode- JR",400,300)
    win.setCoords(0.0,0.0,9.0,12.0)    #draw gui
    ## init and draws field prompts
    msgText = Text(Point(3,9),"{0:>16}".format("File to Encode:"))
    keyText = Text(Point(3,7),"{0:>14}".format("Key Expression:"))
    outputText = Text(Point(3,5),"{0:>19}".format("Output File:"))
    outputText.draw(win)
    msgText.draw(win)
    keyText.draw(win)
    #init and draws entry boxes
    userMsg = Entry(Point(5.9,9),15)
    userMsg.setFill("white")
    userKey = Entry(Point(5.9,7),15)
    userKey.setFill("white")
    userOutput = Entry(Point(5.9,5),15)
    userOutput.setFill("white")
    userMsg.draw(win)
    userKey.draw(win)
    userOutput.draw(win)

    #draw button
    buttonShade = Rectangle(Point(3.1,1.7),Point(6.1,3.3))
    buttonShade.setWidth(3)
    buttonShade.setOutline("grey")
    buttonShade.draw(win)
    button = Rectangle(Point(3.1,1.7),Point(6.1,3.3))
    button.draw(win)
    buttonText = Text(Point(4.5,2.5),"  COMMENCE\n CONVERSION")
    buttonText.setSize(10)
    buttonText.draw(win)
    
    #draw window outline
    winOutline =Rectangle(Point(0,0),Point(9,12))
    winOutline.setOutline("grey")
    winOutline.setWidth(5)
    winOutline.draw(win)

    #wait for click to process
    win.getMouse()
        #DEBUG CODE
        #print(userMsg,userKey)
    userMsg = userMsg.getText()
    userKey = userKey.getText()
    userOutput= userOutput.getText()

    #calls file processing. Parameters are all user entered
    main(userMsg,userKey,userOutput)
   
    buttonText.setText("Close")
    

    win.getMouse()
    win.close()
##------END GUI        



def main(inFile,key,outFile):
    #open file and creates output
    inFile = open(inFile,"r")
    outfile = open(str(outFile), "w")

    #formats key from user
    key = key.replace(" ", "")
    key = key.upper()

    ##iterate through each line in file.
    for sent in inFile:
        #formats line
        sent = sent.upper().replace(" ", "").rstrip("\n")
        #calls function to create key string.
            #Needs to be created for each line due to differing length of line
        keyString = makeKeyStr(sent,key)
        # calls funtion to encode message using line of file and unique key string
        string = msgEncode(sent,keyString)
        #DEBUG CODE#print(string)
        #writes file keeping line order
        outfile.write(string + "\n")
        

def makeKeyStr(sent,key):
    
    keyString = ""
    #repetes key for len of formatted line
    for i in range(len(sent)):
        #DEBUG CODE#print(keyString+ "+ Key i:",i, key[i%len(key)] , " len sent: ",len(sent))
        keyString += key[i% len(key)]
    #DEBUG CODE#print(keyString)
    return(keyString)
#------END makeKeyStr




def msgEncode(sent,keyString):# i need to adjust string based on index addition between key and sentence
    #DEBUG CODE#print("HEY!", len(sent),len(keyString))
    string = ""
    for i in range(len(sent)):
        
        #DEBUG CODE#print("index ",i, " of", len(sent),"=",sent[i]) print(alpha)
        #DEBUG CODE#print("index ",i, " of", len(sent),"=",sent[i])print(sent)
        #DEBUG CODE#print("index ",i, " of", len(sent),"=",sent[i])
        #DEBUG CODE#print("index ",i, " of", len(sent),"=",sent[i])print(alpha.index(sent[i]))
        
        char = alpha.index(sent[i])+ alpha.index(keyString[i])
        char = char % 26
        
        string += alpha[char]
        
        #DEBUG CODE#print(string+"#",i)
        #DEBUG CODE#print(keyString)
            
    return string
#-------END msgEncode

GUI()
