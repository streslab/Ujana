from components import switchmate

while(1):
    cmd = input("> ")
    if(cmd == "on" or cmd == "off"):
        lightswitch.SetState(cmd)
    elif(cmd == "time"):
        switchmate.Bright("0").SetMotion()
    else:
        lightswitch = switchmate.Bright(cmd)
