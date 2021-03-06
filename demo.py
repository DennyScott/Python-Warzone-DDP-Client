#!/usr/bin/env python2.7

import ddpclient
import time

collections = {}
collections["players"] = {}
def main():
    
    app = ddpclient.App("localhost:3000", False)
    time.sleep(2)
    app.do_sub("players")

    while(True):
        time.sleep(.5)

def addToCollections(collection, cID, fields):

    collections[collection][cID] = {}
        
    for key, value in fields:
        collections[collection][cID][key] = value
        
def editCollections(collection, cID, fields):
    for key, value in fields:
        collections[collection][cID][key] = value

if __name__ == '__main__':
    main()
