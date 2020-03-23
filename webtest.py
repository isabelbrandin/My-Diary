import webbrowser
import random

websites = ["https://www.youtube.com/watch?v=PppkNH3bKV4" , "https://youtu.be/26520P-sDmY" , "https://www.youtube.com/watch?v=JRnqdEZ8aoc" , "https://www.youtube.com/watch?v=ur48jVNNlKk" , "https://www.youtube.com/watch?v=D-UmfqFjpl0" , "https://www.youtube.com/watch?v=Ut-fJCc0zS4"
]

webbrowser.open_new(random.choice(websites))