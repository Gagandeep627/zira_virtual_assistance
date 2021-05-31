


import os
query = "open my games"


#opening all gamwes in laptop
if "open my games" in query.lower():
    code_path  = "C:\\Program Files\\NVIDIA Corporation\\NVIDIA GeForce Experience\\NVIDIA GeForce Experience.exe"
    #SpeakText("opening your games."))
    os.startfile(code_path)