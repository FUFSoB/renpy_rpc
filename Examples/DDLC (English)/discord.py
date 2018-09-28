from pypresence import Presence
import time
import random
import sys
import os

client_id = '487972734085759018'
large_text = "DDLC"
large_image = "logo"
small_image = "fuf"
small_text = "FUFSoB"
RPC = Presence(client_id)
RPC.connect()
### STRUCTURE ###

## place/CG-day[-st]

## places: class, club, residential, bedroom, closet, corridor, house_mc, house_s, kitchen, sayoribed, black, white, monika_room, s_hang
## CGs: natsuki_cg1, natsuki_cg2, natsuki_cg3, sayori_cg1, sayori_cg2, sayori_cg3, yuri_cg1, yuri_cg2, yuri_cg3, y_kill, monika_cg1

## Days: d0, d1, d2, d3, sn, fest, d0_g, d1_g, d2_g, d3_g, y_g, fest_g, monika, d0_a
## As [-st] statement can be: poem, poem_n, poem_s, poem_m, poem_y, nr, sr, yr, txt

#####################
# Other settings: mm, sp, poem, poem_g, cr

while True:
    try:
        file = open("{0}\..\state.txt".format(os.getcwd()), 'r', encoding = "utf-8").read().split("\n", 1)
        status = file[0].split("-")
        bg = status[0]
        cg = bg
        mb = cg
        try:
            day = status[1]
        except:
            day = ""
        try:
            st = status[2]
        except:
            st = ""
            
        ### Параметры меню (И не только) ###
            
        if "err3" == mb:
            details = "'*.save': Status error"
            state = "Error 3: loaded wrong save-file"
            large_text = "DDLC"
            large_image = "logo" 
            small_image = "fuf" 
            small_text = "FUFSoB"
            menu = True
        elif "mm" == mb:
            details = "Main Menu"
            state = None
            large_text = "DDLC"
            large_image = "logo" 
            small_image = "fuf"
            small_text = "FUFSoB"
            menu = True
        elif "sp" == mb:
            details = "Game is loading"
            state = None
            large_text = "DDLC"
            large_image = "logo" 
            small_image = "fuf" 
            small_text = "FUFSoB"
            menu = True
        elif "poem" == mb:
            details = "In game"
            state = "Writing a poem"
            large_text = "Writing a poem."
            large_image = "notebook"
            small_image = "logo" 
            small_text = "DDLC"
            menu = True
        elif "poem_g" == mb:
            details = "Just Monika"
            state = "Just Monika"
            large_text = "Just Monika."
            large_image = "notebook_glitch"
            small_image = "logo" 
            small_text = "DDLC"
            menu = True
        elif "cr" == mb:
            details = "In game"
            state = "Watching credits"
            large_text = "Watching credits."
            large_image = "black"
            small_image = "logo" 
            small_text = "DDLC"
            menu = True
        elif "skill" == mb:
            details = "In game"
            state = "First day??? (Act 1)"
            large_text = "PLEASE MAKE IT STOP!"
            large_image = "residential"
            small_image = "logo" 
            small_text = file[1]
            menu = True
        else:
            small_image = "logo"
            small_text = file[1]
            menu = False
            
        ### Дни ###
          
        if "d0" == day:
            details = "In game"
            state = "First day (Act 1)"
        elif "d1" == day:
            details = "In game"
            state = "Second day (Act 1)"
        elif "d2" == day:
            details = "In game"
            state = "Third day (Act 1)"
        elif "d3" == day:
            details = "In game"
            state = "Fourth day (Act 1)"
        elif "sn" == day:
            details = "In game"
            state = "Sunday (Act 1)"
        elif "fest" == day:
            details = "In game"
            state = "Festival day (Act 1)"
        elif "d0_g" == day:
            details = "In game"
            state = "First day (Act 2)"
        elif "d1_g" == day:
            details = "In game"
            state = "Second day (Act 2)"
        elif "d2_g" == day:
            details = "In game"
            state = "Third day (Act 2)"
        elif "d3_g" == day:
            details = "In game"
            state = "Fourth day (Act 2)"
        elif "y_g" == day:
            details = "In game"
            state = '"Weekends" with Yuri (Act 2)'
        elif "fest_g" == day:
            details = "In game"
            state = "Festival day (Act 2)"
        elif "monika" == day:
            details = "Just Monika"
            state = "Just Monika (Act 3)"
        elif "d0_a" == day:
            details = "In game"
            state = "Final day (Act 4)"
            
        ### Фоны ###
        
        if bg == "class":
            large_text = "Class."
            large_image = "class"
        elif bg == "club":
            large_text = "Club."
            large_image = "club"
        elif bg == "residential":
            large_text = "Street."
            large_image = "residential"
        elif bg == "bedroom":
            large_text = "Bedroom."
            large_image = "bedroom"
        elif bg == "closet":
            large_text = "Closet."
            large_image = "closet"
        elif bg == "corridor":
            large_text = "Corridor."
            large_image = "corridor"
        elif bg == "house_mc" or bg == "house":
            large_text = "House."
            large_image = "house"
        elif bg == "house_s":
            large_text = "Sayori's house."
            large_image = "house"
        elif bg == "kitchen":
            large_text = "Kitchen."
            large_image = "kitchen"
        elif bg == "sayoribed":
            large_text = "Sayori's bedroom."
            large_image = "sayoribed"
        elif bg == "black":
            large_text = "Black."
            large_image = "black"
        elif bg == "white":
            large_text = "White."
            large_image = "white"
        elif bg == "monika_room":
            large_text = "Monika's room."
            large_image = "monika_room"
        elif cg == "natsuki_cg1":
            large_text = "Reading manga with Natsuki."
            large_image = "natsuki_cg1"
        elif cg == "natsuki_cg2":
            large_text = "Helping Natsuki in closet."
            large_image = "natsuki_cg2"
        elif cg == "natsuki_cg3":
            large_text = "Natsuki and icing."
            large_image = "natsuki_cg3"
        elif cg == "sayori_cg1":
            large_text = "Zipping Sayori's jacket."
            large_image = "sayori_cg1"
        elif cg == "sayori_cg2":
            large_text = "Helping Sayori with her bruise."
            large_image = "sayori_cg2"
        elif cg == "sayori_cg3":
            large_text = "Hugging Sayori."
            large_image = "sayori_cg3"
        elif cg == "yuri_cg1":
            large_text = "Reading a book with Yuri."
            large_image = "yuri_cg1"
        elif cg == "yuri_cg2":
            large_text = "Feeding Yuri with candies."
            large_image = "yuri_cg2"
        elif cg == "yuri_cg3":
            large_text = "Yuri and dye."
            large_image = "yuri_cg3"
        elif cg == "y_kill":
            large_text = '"Nice weekend"'
            large_image = "y_kill"
        elif cg == "monika_cg1":
            large_text = "Just Monika."
            large_image = "monika_cg1"
        elif cg == "s_hang":
            large_text = "Sayori's bedroom."
            large_image = "s_hang"
        elif not menu:
            details = "'state.txt': Status error"
            state = "Error 1: incorrect arg '{0}'".format(file[0])
            large_text = "DDLC"
            large_image = "logo" 
            small_image = "fuf" 
            small_text = "FUFSoB"
            
        ### Дополнительные параметры ###
            
        if st == "poem":
            large_text += " Sharing poem."
        elif st == "poem_n":
            large_text += " Sharing poem with Natsuki."
        elif st == "poem_s":
            large_text += " Sharing poem with Sayori."
        elif st == "poem_y":
            large_text += " Sharing poem with Yuri."
        elif st == "poem_m":
            large_text += " Sharing poem with Monika."
        elif st == "nr":
            large_text += " Natsuki's route."
        elif st == "sr":
            large_text += " Sayori's route."
        elif st == "yr":
            large_text += " Yuri's route."
        elif st == "txt":
            small_text = "[No text]"
            
    except:
        details = "'state.txt': Status error"
        state = "Error 2: file is missing"
        large_text = "DDLC"
        large_image = "logo" 
        small_image = "fuf" 
        small_text = "FUFSoB"
    if len(small_text) > 126:
        small_text = small_text[0:125].rsplit(" ", 1)[0] + "..."
    elif len(small_text) == 0:
        small_text = "DDLC"
    elif small_text.startswith("<Dynamic>"):
        small_text = "[No text]"
    RPC.update(details=details, state=state, large_image=large_image, large_text=large_text, small_image=small_image, small_text=small_text)