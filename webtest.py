import webbrowser
import random

websites = ["https://www.youtube.com/watch?v=VSPuRXkUWoU" , "https://www.youtube.com/watch?v=3K7l4HBnd9g" , 
"https://www.youtube.com/watch?v=EZg3OqzO7NU" , "https://www.youtube.com/watch?v=TsCqMhhoHa8" , 
"https://www.youtube.com/watch?v=ms1KxfdcSsE" , "https://www.youtube.com/watch?v=bh9N1A5gnR0" , 
"https://www.youtube.com/watch?v=xo8hfBbb7ok" , "https://www.youtube.com/watch?v=v1K4EAXe2oo" , 
"https://www.youtube.com/watch?v=PppkNH3bKV4" , "https://youtu.be/26520P-sDmY" , 
"https://www.youtube.com/watch?v=JRnqdEZ8aoc" , "https://www.youtube.com/watch?v=ur48jVNNlKk" , 
"https://www.youtube.com/watch?v=D-UmfqFjpl0" , "https://www.youtube.com/watch?v=Ut-fJCc0zS4"
]

webbrowser.open_new(random.choice(websites))