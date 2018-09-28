# Ren'Py RPC
Ren'Py Discord Rich Presence, using python 3.6.

[Download python.zip](https://drive.google.com/file/d/1Oubxytg3W_AzHJ4jVwCT-Aa3rjB-8FeX/view?usp=drivesdk)

[Discord server](https://discord.gg/HTPB4Wm), ℱŮℱṦøℬ#1337

## Usage:
   1. Put `discord.py`, `setupRPC.rpy` and `python.zip` in your `game` folder.
   2. Edit your splash.rpy __[all labels are currently exist, you just need to add code]__ *(code's below)*
   3. Add `$ state = "something"` everywhere you wanted status to change.
   4. Just run your game. First of all - it'll unzip `python.zip` and delete it after that. Then it will rewrite status to "Loading" and run `discord.py`.
<details>
  <summary>splash.rpy</summary>
  
  ```renpy
label after_load:
    # ...
    if discordrun:
        python:
            try:
                import io
                import os
                io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
            except:
                import io
                open("game/state.txt", 'w+')
                io.open("game/state.txt", 'w+', encoding = "utf-8").write("err3")
                state = "err3"
    # ...
    return

label before_main_menu:
    # ...
    if discordrun:
        python:
            import io
            state = "mm"
            io.open("game/state.txt", 'w+', encoding = "utf-8").write(state)
    # ...
    return

label quit:
    # ...
    if discordrun:
        python:
            import os
            os.popen('taskkill /f /im python.exe')
    # ...
    return
  ```
  
</details>

## Examples:
   <details>
    <summary>Doki Doki Literature Club</summary>
  
__As first big example I've chosen DDLC, 'cause it's my first VN (in particular - Ren'Py) game.__
  
__Edited files:__ `script.rpy`, `screens.rpy`, `splash.rpy`, `script-ch*.rpy`, `script-exclusives*.rpy`, `script-poemresponses.rpy`
__Added files:__ `discord.py`, `setupRPC.rpy`

_To check how it works you just need to add all these files in DDLC "game" folder._
## Known bugs:
   1) Incorrect text in "small image" when you have to choose in game.
   
  <details>
   <summary>Screenshots</summary>
   
![Profile vision, small image text](https://cdn.discordapp.com/attachments/449909202014568468/495253735241416708/unknown.png)

![Profile vision, large image text](https://cdn.discordapp.com/attachments/449909202014568468/495253871799566336/unknown.png)

![Small vision](https://cdn.discordapp.com/attachments/449909202014568468/495254297060311040/unknown.png)

![Small vision, large image text](https://cdn.discordapp.com/attachments/449909202014568468/495254837680799744/unknown.png)
  </details>
</details>

