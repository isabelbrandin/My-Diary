import webbrowser
import random

def grejor():
    choose = input("Would you rather listen to music or watch a video to boost your mood? :D \n[music / video] \n")

    if choose == "music":
        music = [
            "https://www.youtube.com/watch?v=56WBK4ZK_cw" , "https://www.youtube.com/watch?v=DHwxF48LxPU" , 
            "https://www.youtube.com/watch?v=Yim4--J44gk" , "https://www.youtube.com/watch?v=R_k31vxG26s" , 
            "https://www.youtube.com/watch?v=LLUYAJO64DA" , "https://www.youtube.com/watch?v=bo59ICL2DsI" , 
            "https://www.youtube.com/watch?v=rxf5ZGg9sQw" , "https://youtu.be/dy9nwe9_xzw" , 
            "https://www.youtube.com/watch?v=KmVnOHjO6yU" , "https://www.youtube.com/watch?v=RfsAtKdATj0" , 
            "https://www.youtube.com/watch?v=1OK1OqA-En4" , "https://www.youtube.com/watch?v=dhYOPzcsbGM" , 
            "https://www.youtube.com/watch?v=60ItHLz5WEA" , "https://www.youtube.com/watch?v=6RLLOEzdxsM" , 
            "https://www.youtube.com/watch?v=wJnBTPUQS5A" , "https://www.youtube.com/watch?v=1-xGerv5FOk" , 
            "https://www.youtube.com/watch?v=L3wKzyIN1yk" , "https://www.youtube.com/watch?v=Oj18EikZMuU" , 
            "https://www.youtube.com/watch?v=M-P4QBt-FWw", "https://www.youtube.com/watch?v=kTJbE3sfvlI" , 
            "https://www.youtube.com/watch?v=0Mo_jbZtE-Q"
            ]
        
        webbrowser.open_new(random.choice(music))

    elif choose == "video":
        videos = [
            "https://www.youtube.com/watch?v=xVIbwE_eGK0" , "https://www.youtube.com/watch?v=5Cdv932eoU0" ,
            "https://www.youtube.com/watch?v=PI4JABNwB_U" , "https://www.youtube.com/watch?v=7Nn7NZI_LN4" , 
            "https://www.youtube.com/watch?v=gCAYhUkKUjU" , "https://www.youtube.com/watch?v=1-G6ufv3wG0" , 
            "https://www.youtube.com/watch?v=cjp3iq7fJsI" , "https://www.youtube.com/watch?v=LS_FPxmtz_U" , 
            "https://www.youtube.com/watch?v=4UaYMPfOMGI" , "https://www.youtube.com/watch?v=YJ73wMKovik" , 
            "https://www.youtube.com/watch?v=BT94ZwTGSQU" , "https://www.youtube.com/watch?v=H-zFRGP7MUQ" , 
            "https://www.youtube.com/watch?v=dRkQW-9XvBI" , "https://www.youtube.com/watch?v=PppkNH3bKV4" , 
            "https://youtu.be/26520P-sDmY" , "https://www.youtube.com/watch?v=JRnqdEZ8aoc" , 
            "https://www.youtube.com/watch?v=ur48jVNNlKk" , "https://www.youtube.com/watch?v=D-UmfqFjpl0" , 
            "https://www.youtube.com/watch?v=Ut-fJCc0zS4"
            ]

        webbrowser.open_new(random.choice(videos))