#import openpyxl
import numpy as np

deck = np.array(['alpha','alpha','alpha','zeta','zeta','zeta','gamma','gamma','delta','delta','nova','nova','nova',
        'fafnir','fafnir','fafnir','emergency','emergency','emergency','foolish','called',
        'prep','prep','prep','jack','jack','jack',
        'met','diviner','benten','benten','benten','natasha','draconids','pain','shot','shot','shot','ariadne',
        'ne','ne','ne',
        'ne','ne','ne',
        'ne','ne','ne'])
print("deck size: %d" % len(deck))
hand = []
playable = 0
count = 0
pper = 0.00
nibprot = 0
nibper = 0.00
eyy = 0
delbric = 0
dbper = 0.00
nfaf = 0
nfafper = 0
nfafbric = 0
nfafbricper = 0
necom = 0
necomper = 0
nonames = 0

for run in range(0,100000):
    hand = []
    count += 1
    a = 0
    z = 0
    g = 0
    d = 0
    names = 0
    dupenames = 0

    em = 0
    no = 0
    #nfaf = 0
    faf = 0
    novaih = 0
    jack = 0
    search = 0
    dupsearch = 0

    ben = 0
    pain = 0
    drac = 0
    nat = 0
    freerit = 0
    efb = 0
    
    prot = 0
    a_nib = 0
    cross = 0
    drag = 0
    
    n = 0
    nib = 0
    ash = 0
    ht = 0
    dht = 0
    
    div = 0
    fool = 0
    freefool = 0
    met = 0
    ariadne = 0
    trap = 0
    
    combo = 0
    
    ne = 0



    np.random.shuffle(deck)

    #0print(len(deck))
    for i in range(0,5):
        hand.append(deck[i])
    #print(hand)
    
    for i in range(0,5):
        if hand[i] == 'alpha':
            a = 1
            names += 1
        if hand[i] == 'zeta':
            z = 1
            names += 1
        if hand[i] == 'gamma':
            g = 1
            names += 1
        if hand[i] == 'delta':
            d = 1
            names += 1
        if hand[i] == 'emergency':
            em = 1
            #search += 1
        if hand[i] == 'nova' or hand[i] == 'fafnir' or hand[i] == 'tera':
            no = 1
            #nfaf +=1
            #search += 1
            if hand[i] == 'nova':
                novaih += 1
            if hand[i] == 'fafnir' or hand[i] == 'tera':
                faf += 1
        if hand[i] == 'foolish':
            fool = 1
        if hand[i] == 'benten' or hand[i] == 'prep':
            ben += 1
            freerit = 1
        if hand[i] == 'pain':
            pain += 1 
            freerit = 1
        if hand[i] == 'draconids':
            drac += 1
            freerit = 1
        if hand[i] == 'natasha':
            nat += 1 
        if hand[i] == 'diviner':
            div += 1
        """
        if hand[i] == 'called' or hand[i] == 'instant' or hand[i] == 'crossout' or hand[i] == 'dragged':
            prot += 1
            if hand[i] == 'crossout' or hand[i] == 'dragged':
                a_nib = 1
                cross += 1
        if hand[i] == 'nibiru':
            n = 1
            nib += 1
            ht += 1
        if hand[i] == 'ash':
            ash = 1
            ht += 1
        """
        if hand[i] == 'met':
            met += 1
        if hand[i] == 'shot' or hand[i] == 'ariadne':
            trap += 1
        if hand[i] == 'jack':
            jack = 1
        if hand [i] == 'efb' and efb == 0:
            efb = 1
            if ben == 0:
                ben += 1
            elif ben > 0 and pain == 0:
                pain == 1
            elif pain == 1 and drac == 0:
                drac += 1
            elif pain == 1 and drac == 1:
                ben += 1
        if hand[i] == 'ne':
            ne += 1
        """
        if hand[i] == 'dragged':
            drag = 1
        if hand[i] == 'ariadne':
            ariadne += 1
        """
        dupenames = names - (a + z + g + d)
        names -= dupenames
        """
        dupesearch = search - (em + no)
        search -= dupesearch
        dht = ht - (n + ash)
        print("names: %d" % names)
        print("dupe names: %d" % dupenames)
        print("searchers: %d" % search)
        print("dupe searchers: %d" % dupesearch)
        print("protections: %d" % prot)
        print("nib protected?: %d" % a_nib)
        print("handtraps: %d" % ht)
        print("dupe handtraps: %d" % dht)
        """
    if jack == 1:
        if z == 0:
            z = 1
        elif g == 0:
            g = 1
        elif d == 0:
            d = 1
        else:
            dupenames += 1    
    if fool == 1 and a == 0:
        a = 1
    elif fool == 1 and a == 1 and (dupenames > 1 or freerit >= 1):
        freefool += 1
    
    if a == 1 and (z == 1 or g == 1 or d == 1 or em == 1 or no == 1 or ben >= 1):
        combo += 1
    elif (z == 1 or g == 1 or d == 1 or ben >= 1 or div == 1) and (em == 1 or no == 1):
        combo += 1
    elif em == 1 and no == 1:
        combo += 1
    elif z == 1 and (ben >= 1 or div == 1):
        combo += 1
    elif g == 1 and names >= 2 and ben > 0:
        combo += 1
    elif d == 1 and ben >= 1 and (a == 1 or z == 1 or g == 1 or em == 1 or no == 1):
        combo += 1
    elif d == 1 and ben >= 1 and (a == 1 or z == 1 or g == 1 or em == 1 or no == 1):
        combo += 1
    elif d == 1 and (a == 1 or em == 1 or no == 1) and (pain == 1 or met == 1):
        combo += 1
    elif d == 1 and (div == 1 or ben > 0) and (z == 1 or g == 1 or em == 1 or no == 1):
        combo += 1
    elif trap == 1 and z == 1 and g == 1 and (pain == 1 or drac == 1 or nat == 1):
        combo += 1
    elif trap == 1 and z == 1 and g == 1 and (pain == 1 or drac == 1 or nat == 1):
        combo += 1
    elif trap == 1 and (met == 1 or div == 1) and pain == 1 and drac == 1:
        combo += 1
    elif trap == 1 and met == 1 and (pain == 1 or div == 1) and drac == 1:
        combo += 1
    elif trap == 1 and met == 1 and pain == 1 and (drac == 1 or div == 1):
        combo += 1
    elif trap == 1 and g == 1 and d == 1 and (pain == 1 or div == 1):
        combo += 1
    elif trap == 1 and met == 1 and d == 1 and dupenames > 0 and pain == 1:
        combo += 1

    if trap == 1 and met == 1 and pain == 1 and drac == 1:
        eyy += 1
        
    if (ben > 0 or pain == 1 or drac == 1 or div == 1) and (a == 1 or em == 1) and z == 1:
        a_nib = 1
    elif (ben > 0 or pain == 1 or drac == 1 or div == 1) and a == 1 and (z == 1 or em == 1):
        a_nib = 1
    elif no == 1 and ben > 0 and (a == 1 or z == 1 or em == 1):
        a_nib = 1
    elif ben > 0 and (((z == 1 or em == 1) and (g == 1 or d == 1)) or (z == 1 and (g == 1 or d == 1 or em == 1))):
        a_nib = 1
    
    if combo >= 1:
        playable += 1   
    if d == 1 and combo == 0:
        delbric += 1
    if novaih + faf > 1:
        nfaf += 1
    if (novaih+faf>1) and combo == 0:
        nfafbric += 1
    if a_nib == 1 and combo >= 1:
        nibprot += 1
        #print('playable\n')
    if ne > 0 and combo >= 1:
        necom += 1
    if a == 0 and z == 0 and g == 0 and d == 0 and no == 0 and em == 0:
        nonames += 1
        
pper = (playable/count)*100
nibper = (nibprot/count)*100
dbper = (delbric/count)*100
nfafper = (nfaf/count)*100
nfafbricper = (nfafbric/count)*100
necomper = (necom/count)*100
nonameper = (nonames/count)*100
"""
print(eyy)
print(playable)
"""
print("percentage playable: %d" % pper + "%" + "  %d" % playable)
print("percentage playable through nib: %d" % nibper + "%" + "  %d" % nibprot)
print("percentage playable with non-engine in hand: %d" % necomper + "%" + "  %d" % necom)
print("percentage hands with zero names: %d" % nonameper + "%" + " %d" % nonames)
"""
print("percentage bricks with delta: %d" % dbper +"%")
print("percentage hands with 2 fafnir: %d" % nfafper +"%" + "  %d" % nfaf)
print("percentage bricks with 2 fafnir: %d" % nfafbricper +"%" + "  %d" % nfafbric)
"""