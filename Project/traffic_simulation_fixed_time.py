
#import some important
import time
from tkinter import *
import random



###########################----Reinforcement learning to find the best Q-table------#############################
#the sum of all the horizontal lines
sum_h = 72
#the sum of all the vertical lines
sum_v = 72
#0 for green horizontally, 1 for green vertically
light = 2
#the dealy time of a car cross th intersection
delay = 4
#0 for not switch, 1 for switch
action = 2
#the Q table
Q = [[[[[0] * action] * delay] * light] * sum_v] * sum_h

cur = [71, 71, 0, 0, 0]
next = [None, None, None, None, None]
########################################----Simulating the traffic------##########################################
random.seed(0)
color1 = 'green'
color2 = 'red'
color3 = 'green'
color4 = 'red'
color5 = 'green'
color6 = 'red'
color7 = 'green'
color8 = 'red'

tk = Tk()
canvas = Canvas(tk, width = 400 , height = 400)
canvas.pack()
#line-structures
canvas.create_line(0,133,400,133, fill = 'black')
canvas.create_line(0,266,400,266, fill = 'black')
canvas.create_line(133,0,133,400, fill = 'black')
canvas.create_line(266,0,266,400, fill = 'black')
canvas.create_rectangle( 0, 0, 123, 123, fill = 'green')
canvas.create_rectangle(143, 0, 256, 123, fill = 'green')
canvas.create_rectangle(276, 0, 400, 123, fill = 'green')
canvas.create_rectangle(0, 143, 123, 256, fill = 'green')
canvas.create_rectangle(143, 143, 256, 256, fill = 'green')
canvas.create_rectangle(276, 143, 400, 256, fill = 'green')
canvas.create_rectangle(0, 276, 123, 400, fill = 'green')
canvas.create_rectangle(143, 276, 256, 400, fill = 'green')
canvas.create_rectangle(276,276,400,400, fill = 'green')
#time and personal information
canvas.create_text(200,180,text = 'YUCHEN YAN', fill = 'yellow')
canvas.create_text(200,200,text = 'z5146418', fill = 'yellow')
canvas.create_text(200,50,text = 'Assignment2', fill = 'yellow')
times = canvas.create_text(40, 20, text = 'Time:', fill = 'yellow')
#traffic lights
light_1 = canvas.create_oval(119, 123, 123, 127,fill = color1)
light_2 = canvas.create_oval(139, 119, 143, 123,fill = color2)
light_3 = canvas.create_oval(119, 256, 123, 260,fill = color3)
light_4 = canvas.create_oval(139, 252, 143, 256,fill = color4)
light_5 = canvas.create_oval(252, 123, 256, 127,fill = color5)
light_6 = canvas.create_oval(272, 119, 276, 123,fill = color6)
light_7 = canvas.create_oval(252, 256, 256, 260,fill = color7)
light_8 = canvas.create_oval(272, 252, 276, 256,fill = color8)
cars1 = []
cars2 = []
cars3 = []
cars4 = []
cars5 = []
cars6 = []
cars7 = []
cars8 = []

#Doing the 1000 time step traffic simulation

switch  = 0
count = 0
for t in range(1000):
    #change time
    canvas.itemconfig(times, text = 'Time:' + str(t))
    
    if Q[cur[0]][cur[1]][cur[2]][cur[3]][0] != Q[cur[0]][cur[1]][cur[2]][cur[3]][1]:
        if Q[cur[0]][cur[1]][cur[2]][cur[3]][0] > Q[cur[0]][cur[1]][cur[2]][cur[3]][1]:
            cur[4] = 0
            switch = 0
        else:
            cur[4] = 1
            switch = 1
    else:
        #not done
        switch = 0
        cur[4] = 0

    #change the color of light
#if switch:
    if t%10==0:
        c = color1
        color1 = color2
        color2 = c
        canvas.itemconfig(light_1, fill = color1)
        canvas.itemconfig(light_2, fill = color2)
        
        c2 = color3
        color3 = color4
        color4 = c2
        canvas.itemconfig(light_3, fill = color3)
        canvas.itemconfig(light_4, fill = color4)
    
        c3 = color5
        color5 = color6
        color6 = c3
        canvas.itemconfig(light_5, fill = color5)
        canvas.itemconfig(light_6, fill = color6)

        c4 = color7
        color7 = color8
        color8 = c4
        canvas.itemconfig(light_7, fill = color7)
        canvas.itemconfig(light_8, fill = color8)




    #horizontal-1---when the time is time%(rnd.nextInt(10)+5)==0, create a new car.
    if t % (random.randint(0,9)+5) == 0:
        new = canvas.create_rectangle(0,128,4,132, fill = 'yellow')
        cars1.append(new)
    #horizontal-1---move the cars
    for i in range(len(cars1)):
        A1,B1,C1,D1 = canvas.coords(cars1[i])
        E1,F1,G1,H1 = canvas.coords(cars1[i-1])
        if  ((A1,B1,C1,D1) == (116.0,128.0,120.0,132.0) and color1 == 'red') or ((A1,B1,C1,D1) == (248.0,128.0, 252.0,132.0) and color5 == 'red') or ((A1+4,B1,C1+4,D1) == (E1,F1,G1,H1)):
            count += 1
            continue
        else:
            canvas.move(cars1[i],4,0)
            if canvas.coords(cars1[i]) == (396, 128, 400, 132):
                canvas.delete(cars1[i])

    #horizontal-2---when the time is time%(rnd.nextInt(10)+5)==0, create a new car.
    if t % (random.randint(0,9)+5) == 0:
        new = canvas.create_rectangle(396,134,400,138, fill = 'yellow')
        cars2.append(new)
    #horizontal-2---move the cars
    for i in range(len(cars2)):
        A2,B2,C2,D2 = canvas.coords(cars2[i])
        E2,F2,G2,H2 = canvas.coords(cars2[i-1])
        if  ((A2,B2,C2,D2) == (140.0,134.0,144.0,138.0) and color1 == 'red') or ((A2,B2,C2,D2) == (272.0,134.0, 276.0,138.0) and color5 == 'red') or ((A2-4,B2,C2-4,D2) == (E2,F2,G2,H2)):
            count += 1
            continue
        else:
            canvas.move(cars2[i],-4,0)
            if canvas.coords(cars2[i]) == (0, 134, 4, 138):
                canvas.delete(cars2[i])

    #horizontal-3---when the time is time%(rnd.nextInt(10)+5)==0, create a new car.
    if t % (random.randint(0,9)+5) == 0:
        new = canvas.create_rectangle(0,261,4,265, fill = 'yellow')
        cars3.append(new)
    #horizontal-3---move the cars
    for i in range(len(cars3)):
        A3,B3,C3,D3 = canvas.coords(cars3[i])
        E3,F3,G3,H3 = canvas.coords(cars3[i-1])
        if  ((A3,B3,C3,D3) == (116.0, 261.0, 120.0, 265.0) and color3 == 'red') or ((A3,B3,C3,D3) == (248.0, 261.0, 252.0, 265.0) and color7 == 'red') or ((A3+4,B3,C3+4,D3) == (E3,F3,G3,H3)):
            count += 1
            continue
        else:
            canvas.move(cars3[i],4,0)
            if canvas.coords(cars3[i]) == (396, 261, 400, 265):
                canvas.delete(cars3[i])

    #horizontal-4---when the time is time%(rnd.nextInt(10)+5)==0, create a new car.
    if t % (random.randint(0,9)+5) == 0:
        new = canvas.create_rectangle(396,267,400,271, fill = 'yellow')
        cars4.append(new)
    #horizontal-4---move the cars
    for i in range(len(cars4)):
        A4,B4,C4,D4 = canvas.coords(cars4[i])
        E4,F4,G4,H4 = canvas.coords(cars4[i-1])
        if  ((A4,B4,C4,D4) == (140.0,267.0,144.0,271.0) and color3 == 'red') or ((A4,B4,C4,D4) == (272.0, 267.0, 276.0, 271.0) and color7 == 'red') or ((A4-4,B4,C4-4,D4) == (E4,F4,G4,H4)):
            count += 1
            continue
        else:
            canvas.move(cars4[i],-4,0)
            if canvas.coords(cars4[i]) == (0, 267, 4, 271):
                canvas.delete(cars4[i])

    #vertical-1---when the time is time%(rnd.nextInt(10)+5)==0, create a new car.
    if t % (random.randint(0,9)+5) == 0:
        new = canvas.create_rectangle(124,396,128,400, fill = 'yellow')
        cars5.append(new)
    #vertical-1---move the cars
    for i in range(len(cars5)):
        A5,B5,C5,D5 = canvas.coords(cars5[i])
        E5,F5,G5,H5 = canvas.coords(cars5[i-1])
        if  ((A5,B5,C5,D5) == (124.0,144.0,128.0,148.0) and color2 == 'red') or ((A5,B5,C5,D5) == (124.0, 276.0, 128.0, 280.0) and color4 == 'red') or ((A5,B5-4,C5,D5-4) == (E5,F5,G5,H5)):
            count += 1
            continue
        else:
            canvas.move(cars5[i], 0, -4)
            if canvas.coords(cars5[i]) == (124,0,128,4):
                canvas.delete(cars5[i])

    #vertical-2--when the time is time%(rnd.nextInt(10)+5)==0, create a new car.
    if t % (random.randint(0,9)+5) == 0:
        new1 = canvas.create_rectangle(134,0,138,4, fill = 'yellow')
        cars6.append(new1)
    #vertical-2--move the cars
    for i in range(len(cars6)):
        A6,B6,C6,D6 = canvas.coords(cars6[i])
        E6,F6,G6,H6 = canvas.coords(cars6[i-1])
        if  ((A6,B6,C6,D6) == (134, 116, 138, 120) and color2 == 'red') or ((A6,B6,C6,D6) == (134, 252, 138, 256) and color4 == 'red') or ((A6,B6+4,C6,D6+4) == (E6,F6,G6,H6)):
            count += 1
            continue
        else:
            canvas.move(cars6[i],0,4)
            if canvas.coords(cars6[i]) == (134, 396, 138, 400):
                canvas.delete(cars6[i])

    #vertical-3--when the time is time%(rnd.nextInt(10)+5)==0, create a new car.
    if t % (random.randint(0,9)+5) == 0:
        new1 = canvas.create_rectangle(258,396,262,400,fill = 'yellow')
        cars7.append(new1)
    #vertical-3--move the cars
    for i in range(len(cars7)):
        A7,B7,C7,D7= canvas.coords(cars7[i])
        E7,F7,G7,H7 = canvas.coords(cars7[i-1])
        if  ((A7,B7,C7,D7) == (258,144,262,148) and color6 == 'red') or ((A7,B7,C7,D7) == (258,276,262,280) and color8 == 'red') or ((A7,B7-4,C7,D7-4) == (E7,F7,G7,H7)):
            count += 1
            continue
        else:
            canvas.move(cars7[i],0,-4)
            if canvas.coords(cars7[i]) == (258,0,262,4):
                canvas.delete(cars7[i])

    #vertical-4--when the time is time%(rnd.nextInt(10)+5)==0, create a new car.
    if t % (random.randint(0,9)+5) == 0:
        new1 = canvas.create_rectangle(267,0,271,4, fill = 'yellow')
        cars8.append(new1)
    #vertical-4--move the cars
    for i in range(len(cars8)):
        A8,B8,C8,D8 = canvas.coords(cars8[i])
        E8,F8,G8,H8 = canvas.coords(cars8[i-1])
        if  ((A8,B8,C8,D8) == (267,116,271,120) and color6 == 'red') or ((A8,B8,C8,D8) == (267,252,271, 256) and color8 == 'red')  or ((A8,B8+4,C8,D8+4) == (E8,F8,G8,H8)):
            count += 1
            continue
        else:
            canvas.move(cars8[i],0,4)
            if canvas.coords(cars8[i]) == (267,396,271,400):
                canvas.delete(cars8[i])
    tk.update()
    time.sleep(0.01)






##############################-----Process of Update the Q table---#############################
#get the reward for this action
    reward = 0
    for i in cars1:
        a,b,c,d = canvas.coords(i)
        if  (a,b,c,d) == (116.0,128.0,120.0,132.0) or (a,b,c,d) == (248.0,128.0, 252.0,132.0):
            reward = -1
            break
    for i in cars2:
        a,b,c,d = canvas.coords(i)
        if (a,b,c,d) == (140.0,134.0,144.0,138.0) or (a,b,c,d) == (272.0,134.0, 276.0,138.0):
            reward = -1
            break
    for i in cars3:
        a,b,c,d = canvas.coords(i)
        if (a,b,c,d)== (116.0, 261.0, 120.0, 265.0) or (a,b,c,d) ==(248.0, 261.0, 252.0, 265.0):
            reward = -1
            break
    for i in cars4:
        a,b,c,d = canvas.coords(i)
        if (a,b,c,d) == (140.0,267.0,144.0,271.0) or (a,b,c,d) ==(272.0, 267.0, 276.0, 271.0):
            reward = -1
            break
    for i in cars5:
        a,b,c,d = canvas.coords(i)
        if (a,b,c,d) == (124.0,144.0,128.0,148.0) or (a,b,c,d) == (124.0, 276.0, 128.0, 280.0):
            reward = -1
            break
    for i in cars6:
        a,b,c,d = canvas.coords(i)
        if (a,b,c,d) == (134, 116, 138, 120) or (a,b,c,d) ==(134, 252,138, 256):
            reward = -1
            break
    for i in cars7:
        a,b,c,d = canvas.coords(i)
        if (a,b,c,d) == (258,144,262,148) or (a,b,c,d) == (258,276,262,280):
            reward = -1
            break
    for i in cars8:
        a,b,c,d = canvas.coords(i)
        if (a,b,c,d) == (267,116,271,120) or (a,b,c,d) ==(267,252,271, 256):
            reward = -1
            break

#find the new cur state
#sum_h
    value = 0
    C = [(116,128.0,120,132),(112,128,116,132),(108,128,112,132),(104,128,108,132),(100,128,104,132),(96,128,100,132),(92,128,96,132),(88,128,92,132)]
    flag = 0
    for i in range(len(C)):
        for j in cars1:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(248.0,128.0, 252.0,132.0),(244,128,248,132),(240,128,244,132),(236,128,240,132),(232,128,236,132),(228,128,232,132),(224,128,228,132),(220,128,224,132)]
    flag = 0
    for i in range(len(C)):
        for j in cars1:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(140.0,134.0,144.0,138.0),(144,134,148,138),(148,134,152,138),(152,134,156,138),(156,134,160,138),(160,134,164,138),(164,134,168,138),(168,134,172,138)]
    flag = 0
    for i in range(len(C)):
        for j in cars2:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(272.0,134.0, 276.0,138.0),(276,134,280,138),(280,134,284,138),(284,134,288,138),(288,134,292,138),(292,134,296,138),(296,134,300,138),(300,134,304,138)]
    flag = 0
    for i in range(len(C)):
        for j in cars2:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(116.0,261.0,120.0,265.0),(112,261,116,265),(108,261,112,265),(104,261,108,265),(100,261,104,265),(96,261,100,265),(92,261,96,265),(88,261,92,265)]
    flag = 0
    for i in range(len(C)):
        for j in cars3:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(248.0,261.0, 252.0,265.0),(244,261,248,265),(240,261,244,265),(236,261,240,265),(232,261,236,265),(228,261,232,265),(224,261,228,265),(220,261,224,265)]
    flag = 0
    for i in range(len(C)):
        for j in cars3:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(140.0,267.0,144.0,271.0),(144,267,148,271),(148,267,152,271),(152,267,156,271),(156,267,160,271),(160,267,164,271),(164,267,168,271),(168,267,172,271)]
    flag = 0
    for i in range(len(C)):
        for j in cars4:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9


    C = [(272.0,267.0, 276.0,271.0),(276,267,280,271),(280,267,284,271),(284,267,288,271),(288,267,292,271),(292,267,296,271),(296,267,300,271),(300,267,304,271)]
    flag = 0
    for i in range(len(C)):
        for j in cars4:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9
    next[0] = value-1

#sum_v
    value = 0
    C = [(124.0,144.0,128.0,148.0),(124,148,128,152),(124,152,128,156),(124,156,128,160),(124,160,128,164),(124,164,128,168),(124,168,128,172),(124,172,128,176)]
    flag = 0
    for i in range(len(C)):
        for j in cars5:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(124.0, 276.0, 128.0, 280.0),(124,280,128,284),(124,284,128,288),(124,288,128,292),(124,292,128,296),(124,296,128,300),(124,300,128,304),(124,304,128,308)]
    flag = 0
    for i in range(len(C)):
        for j in cars5:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(134,116,138,120),(134,112,138,116),(134,108,138,112),(134,104,138,108),(134,100,138,104),(134,96,138,100),(134,92,138,96),(134,88,138,92)]
    flag = 0
    for i in range(len(C)):
        for j in cars6:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(134,252,138,256),(134,248,138,252),(134,244,138,248),(134,240,138,244),(134,236,138,240),(134,232,138,236),(134,228,138,232),(134,224,138,228)]
    flag = 0
    for i in range(len(C)):
        for j in cars6:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(258,144,262,148),(258,148,262,152),(258,152,262,156),(258,156,262,160),(258,160,262,164),(258,164,262,168),(258,168,262,172),(258,172,262,176)]
    flag = 0
    for i in range(len(C)):
        for j in cars7:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(258,276,262,280),(258,280,262,284),(258,284,262,288),(258,288,262,292),(258,292,262,296),(258,296,262,300),(258,300,262,304),(258,304,262,308)]
    flag = 0
    for i in range(len(C)):
        for j in cars7:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(267,116,271,120),(267,112,271,116),(267,108,271,112),(267,104,271,108),(267,100,271,104),(267,96,271,100),(267,92,271,96),(267,88,271,92)]
    flag = 0
    for i in range(len(C)):
        for j in cars8:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9

    C = [(267,252,271, 256),(267,248,271,252),(267,244,271,248),(267,240,271,244),(267,236,271,240),(267,232,271,236),(267,228,271,232),(267,224,271,228)]
    flag = 0
    for i in range(len(C)):
        for j in cars8:
            a,b,c,d = canvas.coords(j)
            if (a,b,c,d) == C[i]:
                value += i
                flag = 1
                break
        if flag:
            break
    if flag == 0:
        value += 9
    next[1] = value-1
#light
    if color1 == 'green':
        next[2] = 0
    else:
        next[2] = 1
#delay
    next[3] = 3
#action
    next[4] = 0
    n = max(Q[next[0]][next[1]][next[2]][next[3]])
    o_Q = Q[cur[0]][cur[1]][cur[2]][cur[3]][cur[4]]
    Q[cur[0]][cur[1]][cur[2]][cur[3]][cur[4]] += 0.2 * (reward + 0.9 * n - o_Q)
    cur = next
print('the sum of the number of time-steps the number of cars is queued in a period of time: ',count)
#tk.mainloop()
    

