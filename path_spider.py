#!/usr/bin/env python3

import glob
import os


separator = "--------"
step = 0

class Spider:


    def __init__(self, path, separator, step):
        self.path = path
        self.separator = separator
        self.step = step


    def pathContent(self):        
        for item in glob.glob(os.path.join(self.path, "*")):  # loop through directory
            isDir = self.checkDir(item)  # run checkDir function 
            if isDir == True:
                print(separator * self.step + "> " + item)
                self.path = item
                self.step += 1  # amplify separator before running through new directory
                self.pathContent()   # if a directory is found, the function will call itself to run through it
                self.step -= 1  # after new directory has been run through, make the separator shrink

            if isDir == False:
                print(separator * self.step + "> " + item)     


    def checkDir(self, item):
        if os.path.isdir(item):
            return True # true if its a directory
        else:
            return False # false if its not a directory
        

def main():
    try:
        path = input("choose the path to spider through:")
        os.chdir(path)

        spiderThis = Spider(path, separator, step)
        spiderThis.pathContent()  # Here the spidering starts!
    except OSError:
        print("Something wrong with your input... :)")
main()


            

    
