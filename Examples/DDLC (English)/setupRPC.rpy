init python:
    import os
    import subprocess
    import io
    discordrun = False
    if renpy.windows:
        try:
            process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
        except:
            pass
        try:
            discord_list = ['discord.exe']
            if list(set(process_list).intersection(discord_list)):
                discordrun = True
                try:
                    import zipfile
                    with zipfile.ZipFile('game/python.zip', "r") as z:
                        z.extractall("game/")
                    os.remove('game/python.zip')
                except:
                    pass
                state = "sp"
                try: 
                    open("{0}\game\state.txt".format(os.getcwd()), 'r')
                except:
                    io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
                else:
                    io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
                p = subprocess.Popen('cd {0}\game\PPython && python "{0}\game\discord.py"'.format(os.getcwd()), shell=True)
        except:
            pass
    whathere = None
    texthere = None
    textthere = None
    day = ""
    st = ""

label rpc:
    if discordrun:
        python:
            import io
            io.open("{0}\game\state.txt".format(os.getcwd()), 'w+', encoding = "utf-8").write(state)
    return