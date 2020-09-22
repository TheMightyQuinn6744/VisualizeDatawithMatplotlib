import codecademylib3_seaborn
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# # Bar Graph: Featured Games
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]
#plot bar chart using range(len(games)), viewers as arguments
plt.bar(range(len(games)),viewers,color="slateblue")
plt.title('Number of Streaming Viewers Per Game')
plt.xlabel('Games')
plt.ylabel('Number of Streaming Viewers')
#Adding ticks, ticklabels to bar chart
ax = plt.subplot()
ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
ax.set_xticklabels(games, rotation=30)
plt.legend(['Twitch'])
plt.show()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "DE", "CA", "N/A", "GB", "TR", "BR", "DK", "PL", "BE", "NL", "Others"]

countries = [447, 66, 64, 49, 45, 28, 25, 20, 19, 17, 17, 279]
#array of colors for LoL Pie Chart
colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']
#break out slice repr US
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#plot pie with countries, colors
plt.pie(countries, explode=explode, colors = colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title("League of Legens Viewers' Whereabouts")
plt.legend(labels, loc="right")
plt.show()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]

plt.plot(hour, viewers_hour)
#declare x axis & y axis labels
plt.title('Time Series')
plt.xlabel('Hours of the Day')
plt.ylabel('Number of Streaming Viewers')
#set xticks
ax2 = plt.subplot()
ax2.set_xticks(hour)
#set yticks
ax2.set_yticks([0, 20, 40, 60, 80, 100, 120, 140])
#set legend
plt.legend(['2015-01-01'])
#create upper bound list y_upper
y_upper = [i + (i*0.15) for i in viewers_hour]
#create lower bound list y_lower
y_lower = [i - (i*0.15) for i in viewers_hour]
#plot fill between 
plt.fill_between(hour,y_lower,y_upper, alpha=0.2)
plt.show()
