# renpy_rpc
Ren'Py Discord Rich Precense, using python 3.6.

[Download python.zip](https://drive.google.com/file/d/1Oubxytg3W_AzHJ4jVwCT-Aa3rjB-8FeX/view?usp=drivesdk)

[Discord server](https://discord.gg/HTPB4Wm), ℱŮℱṦøℬ#1337


### Usage:
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

## Example's coming soon...
