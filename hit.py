#!/usr/bin/env python2.7

import ddpclient
import time;

def main():
    
    app = ddpclient.App("localhost:3000", False)
    time.sleep(1);
    app.do_call("hit [10, \"Ada Lovelace\"]")
        


if __name__ == '__main__':
    main()
