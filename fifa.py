import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
# % matplotlib inline

df = pd.read_csv(r'C:\Users\DELL\Documents\Fulldata.csv', encoding='latin1')
print(df.head(7))
del df['National_Kit']
#print(df.head(7))

#plt.figure(figsize=(15,32))
#sns.countplot(y = df.Nationality, palette='Set2')
#plt.show()

#.plt.figure(figsize=(15, 6))
#sns.countplot(x = 'Age', data = df)
#plt.show()

a = 0.5
b = 1
c = 2
d = 3
                    #Goal Keeper
df['gk_shot_stopper'] = (b*df.Reactions + b*df.Composure + a*df.Speed + a*df.Strength + c*df.Jumping + b*df.GK_Positioning + c*df.GK_Diving + b*df.GK_Handling + d*df.GK_Reflexes)/(2*a + 4*b + 2*c + 1*d)
df['gk_sweeper'] = (b*df.Reactions + b*df.Composure + b*df.Speed + a*df.Short_Pass+ a*df.Long_Pass + b*df.Jumping + b*df.GK_Positioning + b*df.GK_Diving + b*df.GK_Handling + d*df.GK_Reflexes + d*df.GK_Kicking + c*df.Vision)/(2*a + 7*b + 1*c + 2*d)

plt.figure(figsize=(15,6))
sd1 = df.sort_values('gk_shot_stopper', ascending=False)[:5]
x1 = np.array(list(sd1['Name']))
y1 = np.array(list(sd1['gk_shot_stopper']))

sns.barplot(x1, y1, palette= 'colorblind')
plt.ylabel("Show stopping score")
plt.show()

plt.figure(figsize=(15, 6))
sd1 = df.sort_values('gk_sweeper', ascending=False)[:5]
x1 = np.array(list(sd1['Name']))
y1 = np.array(list(sd1['gk_sweeper']))

sns.barplot(x1, y1, palette='colorblind')
plt.ylabel("Sweeper score")
plt.show()

                 #defender

df['df_centre_backs'] = (d*df.Reactions + c*df.Interceptions + d*df.Sliding_Tackle + d*df.Standing_Tackle + b*df.Vision + b*df.Composure + b*df.Crossing + a*df.Short_Pass + b*df.Long_Pass + c*df.Acceleration + b*df.Speed + d*df.Stamina + d*df.Jumping + d*df.Heading + b*df.Long_Shots + d*df.Marking + c*df.Aggression)/(6*b + 3*c + 7*d)
df['df_wb_Wing_Backs'] = (b*df.Ball_Control + a*df.Dribbling + a*df.Marking + d*df.Sliding_Tackle + d*df.Standing_Tackle + a*df.Attacking_Position + c*df.Vision + c*df.Crossing + b*df.Short_Pass + c*df.Long_Pass + d*df.Acceleration + d*df.Speed + c*df.Stamina + a*df.Finishing)/(4*a + 2*b + 5*c + 5*d)

#plot left centre backs

plt.figure(figsize=(15, 6))
sd = df[(df['Club_Position'] == 'LCB')].sort_values('df_centre_backs', ascending=False)[:5]
x2 = np.array(list(sd['Name']))
y2 = np.array(list(sd['df_centre_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LCB Score")
plt.show()

#plt Right Centre Backs
plt.figure(figsize=(15, 6))
sd = df[(df['Club_Position'] == 'RCB')].sort_values('df_centre_backs', ascending=False)[:5]
x2 = np.array(list(sd['Name']))
y2 = np.array(list(sd['df_centre_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("RCB Score")
plt.show()

             #Plot Left WB

plt.figure(figsize=(15,6))
sd = df[(df['Club_Position'] == 'LWB') | (df['Club_Position'] == 'LB')].sort_values('df_wb_Wing_Backs', ascending=False)[:5]
x4 = np.array(list(sd['Name']))
y4 = np.array(list(sd['df_wb_Wing_Backs']))
sns.barplot(x4, y4, palette=sns.color_palette('Blues_d'))
plt.ylabel("Left Back Score")
plt.show()

# Plot Right WB

plt.figure(figsize=(15, 6))
sd = df[(df['Club_Position'] == 'RWB') | (df['Club_Position'] == 'RB')].sort_values('df_wb_Wing_Backs', ascending=False)[:5]
x4 = np.array(list(sd['Name']))
y4 = np.array(list(sd['df_wb_Wing_Backs']))
sns.barplot(x4, y4, palette=sns.color_palette("Blues_d"))
plt.ylabel("Right Back Score")
plt.show()
                #Best Mid Fielders

df['mf_controller'] = (b*df.Weak_foot + d*df.Ball_Control + a*df.Dribbling + a*df.Marking + a*df.Reactions + c*df.Vision + c*df.Composure + d*df.Short_Pass + d*df.Long_Pass)/(4*a + 2*c + 3*d)
df['mf_play_maker'] = (d*df.Ball_Control + d*df.Dribbling + a*df.Marking + d*df.Reactions + d*df.Vision + c*df.Attacking_Position + c*df.Crossing + d*df.Short_Pass + c*df.Long_Pass + c*df.Curve + b*df.Long_Shots + c*df.Freekick_Accuracy)/(1*a + 1*b + 5*c + 5*d)
df['mf_beast'] = (d*df.Agility + c*df.Balance + b*df.Jumping + c*df.Strength + d*df.Stamina + a*df.Speed + c*df.Acceleration + d*df.Short_Pass + c*df.Aggression + d*df.Reactions + b*df.Marking + b*df.Standing_Tackle + b*df.Interceptions)/(1*a + 5*b + 4*c + 4*d)

#plot - playmaker
plt.figure(figsize=(15, 6))
ss = df[(df['Club_Position'] == 'CAM') | (df['Club_Position'] == 'LAM') | (df['Club_Position'] == 'RAM')].sort_values('mf_play_maker',ascending=False)[:5]
x3 = np.array(list(ss['Name']))
y3 = np.array(list(ss['mf_play_maker']))
sns.barplot(x3, y3, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("PlayMaker Score")
plt.show()

#plot beast

plt.figure(figsize=(15, 6))
ss = df[(df['Club_Position'] == 'RCM') | (df['Club_Position'] == 'RM')].sort_values('mf_beast', ascending=False)[:5]
x3 = np.array(list(ss['Name']))
y3 = np.array(list(ss['mf_beast']))
sns.barplot(x3, y3, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("Beast Score")
plt.show()

#plot controller

plt.figure(figsize=(15, 6))
ss = df[(df['Club_Position'] == 'LCM') | (df['Club_Position'] == 'LM')].sort_values('mf_controller', ascending=False)[:5]
x1 = np.array(list(ss['Name']))
y1 = np.array(list(ss['mf_controller']))
sns.barplot(x1, y1, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("Controller Score")
plt.show()

                    #Best Attackers

df['att_left_wing'] = (c*df.Weak_foot + c*df.Ball_Control + c*df.Dribbling + c*df.Speed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.Short_Pass + b*df.Long_Pass + b*df.Aggression + b*df.Agility + a*df.Curve + c*df.Long_Shots + b*df.Freekick_Accuracy + d*df.Freekick_Accuracy)/(a + 6*b + 6*c + 2*d)
#df['att_right_wing'] =
df['att_striker'] = (b*df.Weak_foot + b*df.Ball_Control + a*df.Vision + b*df.Aggression + b*df.Agility + a*df.Curve + a*df.Long_Shots + d*df.Balance + d*df.Finishing + d*df.Heading + c*df.Jumping + c*df.Dribbling)/(3*a + 4*b + 2*c + 3*d)

# plot left wing attacker

plt.figure(figsize=(15,6))
sc = df[(df['Club_Position'] == 'LW') | (df['Club_Position'] == 'LM') | (df['Club_Position'] == 'LS')].sort_values('att_left_wing', ascending=False)[:5]
x4 = np.array(list(sc['Name']))
y4 = np.array(list(sc['att_left_wing']))
sns.barplot(x4, y4, palette=sns.diverging_palette(255, 133, l=60, n=5, center='dark'))
plt.ylabel('Left Wing Attacker')
plt.show()

#plot right attacker

plt.figure(figsize=(15,6))
sc = df[(df['Club_Position'] == 'RW') | (df['Club_Position'] == 'RM') | (df['Club_Position'] == 'RS')].sort_values('att_left_wing', ascending=False)[:5]
x4 = np.array(list(sc['Name']))
y4 = np.array(list(sc['att_left_wing']))
sns.barplot(x4, y4, palette=sns.diverging_palette(255, 133, l=60, n=5, center='dark'))
plt.ylabel('Left Wing Attacker')
plt.show()

#plot striker

plt.figure(figsize=(15, 6))
sd = df[(df['Club_Position'] == 'ST') | (df['Club_Position'] == 'LS') | (df['Club_Position'] == 'RS')].sort_values('att_striker', ascending=False)[:5]
x1 = np.array(list(sd['Name']))
y1 = np.array(list(sd['att_striker']))
sns.barplot(x1, y1, palette=sns.diverging_palette(255, 133, l=60, n=5, center='dark'))
plt.ylabel('Striker')
plt.show()