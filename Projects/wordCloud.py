from wordcloud import WordCloud  
import matplotlib.pyplot as plt
import sys , os
os.chdir(sys.path[0])

text=open('text.txt',mode='r',encoding='utf-8').read()


wc = WordCloud(
    background_colour = 'white',
    height = '600',
    width = '400'
)
wc.generate(text)

wc.to_file('wordcloud.png')

