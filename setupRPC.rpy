init python:
    import os
    import subprocess
    import io
    discordrun = False
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n") # get processes
        except:
            pass
        try:
            discord_list = ['discord.exe']
            if list(set(process_list).intersection(discord_list)): # check if Discord.exe is in "process_list"
                discordrun = True # if successfully - turn discord_rpc on
                try: # unzip python3.6 to "game" folder, if "python.zip" exists
                    import zipfile
                    with zipfile.ZipFile('game/python.zip', "r") as z:
                        z.extractall("game/")
                    os.remove('game/python.zip') # delete "python.zip" for next getting "except"
                except:
                    pass
                state = "sp" # set "loading" rpc status
                io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state) # write "state" to file
                p = subprocess.Popen('cd {0}\game\PPython && python "{0}\game\discord.py"'.format(os.getcwd()), shell=True) ### START RPC IN BACKGROUND ###
        except:
            pass

label rpc: # callable label to set state. 
    if discordrun:
        python:
            import io
            io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
    return
