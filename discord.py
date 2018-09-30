from pypresence import Presence
import time
import random
import sys
import os

starttime = int(time.time())
client_id = 'id' # id of your Discord application
large_text = "Game" # text of large img of your app
large_image = "logo" # large img of your app
small_text = "FUFSoB" # text of small img of your app
small_image = "fuf" # small img of your app
RPC = Presence(client_id)
RPC.connect() # Connect RPC client

while True:
    try:
        file = open("{0}\..\state.txt".format(os.getcwd()), 'r', encoding = "utf-8").read() # get status from file
        
        if "err3" == mb:
            details = "'*.save': Status error"
            state = "Error 3: loaded wrong save-file"
            large_text = "Game"
            large_image = "logo" 
            small_text = "FUFSoB"
            small_image = "fuf" 
        elif "mm" == mb:
            details = "Main Menu"
            state = None
            large_text = "Game"
            large_image = "logo" 
            small_text = "FUFSoB"
            small_image = "fuf" 
        elif "sp" == mb:
            details = "Game is loading"
            state = None
            large_text = "Game"
            large_image = "logo" 
            small_text = "FUFSoB"
            small_image = "fuf" 
        else:
            details = "'state.txt': Status error"
            state = "Error 1: incorrect arg: '{0}'".format(file)
            large_text = "Game"
            large_image = "logo" 
            small_text = "FUFSoB"
            small_image = "fuf" 
    except:
        details = "'state.txt': Status error"
        state = "Error 2: file is missing"
        large_text = "Game"
        large_image = "logo" 
        small_text = "FUFSoB"
        small_image = "fuf" 
    RPC.update(details=details, state=state, start = starttime, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text) # update status of rpc
