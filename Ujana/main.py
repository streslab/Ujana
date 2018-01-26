from components import switchmate

while(1):
    cmd = input("> ")
    if(cmd == "on" or cmd == "off"):
        lightswitch.SetState(cmd)
    elif(cmd == "time"):
        lightswitch.SetMotion()
    else:
        lightswitch = switchmate.Bright(cmd)
