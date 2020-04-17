# create class
class player:
    def __init__(self, play_type, opp_defect, results, last_move, avg):
        self.play_type = play_type
        self.opp_defect = opp_defect
        self.results = results
        self.last_move = last_move
        self.avg = avg
#define game function
def playGame(x, y):
    x_move = ""
    y_move = ""
    #let coop = true, defect = false
    # x moves
    if x.play_type == "tft":
        # tit for tat strategy
        if y.last_move == "":
            x_move = True
        else:
            x_move = y.last_move
    elif x.play_type == "g":
        # grudger strategy
        if y.last_move == False:
            x.opp_defect = True
        if x.opp_defect == True:
            x_move = False
        else:
            x_move = True
    elif x.play_type == "ac":
        x_move = True
    else:
        # ad
        x_move = False
    
    # y moves
    if y.play_type == "tft":
        # tit for tat strategy
        if x.last_move == "":
            y_move = True
        else:
            y_move = x.last_move
    elif y.play_type == "g":
        # grudger strategy
        if x.last_move == False:
            y.opp_defect = True

        if y.opp_defect == True:
            y_move = False
        else:
            y_move = True
    elif y.play_type == "ac":
        y_move = True
    else:
        # ad
        y_move = False
    # print("winner is " + x.play_type)
    #payouts
    if x_move == True and y_move == True:
        x.results.append(3)
        y.results.append(3)
    elif x_move == True and y_move == False:
        x.results.append(0)
        y.results.append(5)
    elif x_move == False and y_move == True:
        x.results.append(5)
        y.results.append(0)
    else:
        # both false
        x.results.append(1)
        y.results.append(1)
    # print("game complete")
players = []
# create players
for x in range(100) : 
    # 0-99
    if x <25:
        # 0-24, T4T
        result_arr = []
        obj = player("tft", False, result_arr, " ", 0)
        players.append(obj)
    elif x < 50:
        #25-49, G
        obj = player("g", False, [], "", 0)
        players.append(obj) 
    elif x < 75:
        # 50-74, AC
        obj = player("ac", False, [], "", 0)
        players.append(obj)
    else:
        # 75-99, AD
        obj = player("ad", False, [], "", 0)
        players.append(obj)

# this loop structure conducts the correct amount of loops
# n = 100, m = 5, p = 5, k = 20
gen_count = 0
# count = 0
for g in range(20):
    # reset results arrs
    for item in players:
        item.results = []
    curr = 0
    for i in players:
        index = curr
        leng = len(players)
        for j in range(index+1, leng):
            # starts at player right after, iterates through remaining
            # print("hello")
            # print(index)
            # count +=1
            # print (count)
            #game rules/code below
            # will need to be done m times
            for d in range(5):
                playGame(i, players[j])
            if i.play_type == "g":
                i.opp_defect = False
            if players[j].play_type == "g":
                players[j].opp_defect = False
            # leave below, leave as last - NEED
            index += 1
        # leave below, leave as last - NEED
        curr += 1
    # print(count)
    #results populated
    #print averages to show it works
    tft_sum = 0
    tft_count = 0
    g_sum = 0
    g_count = 0
    ac_sum = 0
    ac_count = 0
    ad_sum = 0
    ad_count = 0
    for u in players:
        if u.play_type == "tft":
            for r in u.results:
                tft_sum += r
                tft_count += 1
        elif u.play_type == "g":
            for r in u.results:
                g_sum += r
                g_count += 1
        elif u.play_type == "ac":
            for r in u.results:
                ac_sum += r
                ac_count += 1
        else:
            # ad
            for r in u.results:
                ad_sum += r
                ad_count += 1
    # calc individual player avgs for sorting
    for u in players:
        curr_av = (float(sum(u.results))/float(len(u.results)))
        # print(curr_av)
        u.avg = curr_av
    #calc percentages
    tft_perc = 0
    g_perc = 0
    ac_perc = 0
    ad_perc = 0
    for n in players:
        if n.play_type == "tft":
            tft_perc += 1
        if n.play_type == "g":
            g_perc += 1
        if n.play_type == "ac":
            ac_perc += 1
        if n.play_type == "ad":
            ad_perc += 1
    # group prints
    gen_count += 1
    print("Generation: %s" % gen_count)
    print("percentages: ")
    print("tft: " + "{0:.0%}".format(tft_perc/float(len(players))))
    print("g: " + "{0:.0%}".format(g_perc/float(len(players))))
    print("ac: " + "{0:.0%}".format(ac_perc/float(len(players))))
    print("ad: " + "{0:.0%}".format(ad_perc/float(len(players))))

    print("sums: ")
    print("tft: %s" % tft_sum)
    print("g: %s" % g_sum)
    print("ac: %s" % ac_sum)
    print("ad: %s" % ad_sum)
    print("averages: ")
    # print(tft_sum)
    # print(tft_count)
    tft_av = 0
    if tft_count > 0:
        tft_av = float(tft_sum)/float(tft_count)
    print("tft: %.2f" % tft_av)
    # print(g_sum)
    # print(g_count)
    g_av = 0
    if g_count > 0:
        g_av = float(g_sum)/float(g_count)
    print("g: %.2f" % g_av)
    # print(ac_sum)
    # print(ac_count)
    ac_av = 0
    if ac_count > 0:
        ac_av = float(ac_sum)/float(ac_count)
    print("ac: %.2f" % ac_av)
    # print(ad_sum)
    # print(ad_count)
    ad_av = 0
    if ad_count > 0:
        ad_av = float(ad_sum)/float(ad_count)
    print("ad: %.2f" % ad_av)

    #generation percentage calcs happen here
    #rank players -> remove bottom p% -> replice and add top p%
    def retAvg(e):
        return e.avg
    players.sort(key=retAvg)
    # sorted - lowest first (0), highest last (99)
    p = 5
    for rep in range(5):
        players.pop(rep)
    for rep in range(90,95):
        obj = player(players[rep].play_type, players[rep].opp_defect, 
        players[rep].results, players[rep].last_move, players[rep].avg)
        players.append(obj)

    
    #note- finish this, increment generation count, then be sure to reset results every generation
#all of this above is in a large for loop for generations



