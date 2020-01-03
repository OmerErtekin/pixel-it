import platform

def sound(sound):
    if (platform.system() == "Linux"):
        import os
        merged = "aplay "+sound+"&"
        return os.system(merged)
    elif (platform.system() == "Darwin"):
        import os
        merged = "afplay "+sound+"&"
        return os.system(merged)
    elif (platform.system() ==  "Windows"):
        import winsound
        return winsound.PlaySound(sound,winsound.SND_ASYNC)
    
    #serkan direk koplayalıp yapıştırdım sorunumu halletti her yerden teşekkür etmek istiyorum şu an sana jasdjsajd ben de böyle bir şey yapayım dedim
   
