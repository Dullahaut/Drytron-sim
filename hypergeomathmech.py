import openpyxl
import numpy as np

deck = np.array(['alpha','alpha','alpha','zeta','zeta','zeta','gamma','gamma','gamma','delta','delta','delta','nova','nova','nova',
        'fafnir','fafnir','tera','emergency','emergency','emergency','foolish','called','instant','crossout','crossout','crossout',
        'met','ash','ash','nibiru','nibiru','diviner','benten','benten','benten','natasha','draconids','pain','thunder'])
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
    search = 0
    dupsearch = 0

    ben = 0
    pain = 0
    drac = 0
    nat = 0
    freerit = 0
    
    prot = 0
    a_nib = 0
    cross = 0
    
    n = 0
    nib = 0
    ash = 0
    ht = 0
    dht = 0
    
    div = 0
    fool = 0
    met = 0
    thunder = 0
    
    combo = 0



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
            search += 1
        if hand[i] == 'nova' or hand[i] == 'fafnir' or hand[i] == 'tera':
            no = 1
            #nfaf +=1
            search += 1
            if hand[i] == 'nova':
                novaih += 1
            if hand[i] == 'fafnir' or hand[i] == 'tera':
                faf += 1
        if hand[i] == 'foolish':
            fool = 1
        if hand[i] == 'benten':
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
        if hand[i] == 'called' or hand[i] == 'instant' or hand[i] == 'crossout':
            prot += 1
            if hand[i] == 'crossout':
                a_nib = 1
                cross += 1
        if hand[i] == 'nibiru':
            n = 1
            nib += 1
            ht += 1
        if hand[i] == 'ash':
            ash = 1
            ht += 1
        if hand[i] == 'met':
            met += 1
        if hand[i] == 'thunder':
            thunder += 1
        
        dupenames = names - (a + z + g + d)
        names -= dupenames
        dupesearch = search - (em + no)
        search -= dupesearch
        dht = ht - (n + ash)
        """
        print("names: %d" % names)
        print("dupe names: %d" % dupenames)
        print("searchers: %d" % search)
        print("dupe searchers: %d" % dupesearch)
        print("protections: %d" % prot)
        print("nib protected?: %d" % a_nib)
        print("handtraps: %d" % ht)
        print("dupe handtraps: %d" % dht)
        """
    if fool == 1 and a == 0:
        a = 1
    elif fool == 1 and a == 1 and (dupenames > 1 or freerit >= 1):
        search += 1
    if a == 1 and (z == 1 or g == 1 or search >= 1):
        combo += 1
    elif (z == 1 or g == 1) and search >= 1:
        combo += 1
    elif search >= 2:
        combo += 1
    elif d == 1 and no == 1:
        combo += 1
    elif z == 1 and g == 1 and div == 1:
        combo += 1
    elif g == 1 and names >= 2 and ben > 0:
        combo += 1
    elif d == 1 and ben >= 1 and (a == 1 or z == 1 or g == 1 or em == 1):
        combo += 1
    elif d == 1 and (a == 1 or em == 1) and (pain == 1 or met == 1):
        combo += 1
    elif thunder == 1 and z == 1 and g == 1 and (pain == 1 or drac == 1):
        combo += 1
    elif thunder == 1 and (met == 1 or div == 1) and pain == 1 and drac == 1:
        combo += 1
    elif thunder == 1 and met == 1 and (pain == 1 or div == 1) and drac == 1:
        combo += 1
    elif thunder == 1 and met == 1 and pain == 1 and (drac == 1 or div == 1):
        combo += 1
    elif thunder == 1 and g == 1 and d == 1 and (pain == 1 or div == 1):
        combo += 1
    elif thunder == 1 and a == 1 and ben >= 1 and (pain == 1 or met == 1 or div == 1 or ben > 1):
        combo += 1
    elif thunder == 1 and met == 1 and d == 1 and dupenames > 0 and pain == 1:
        combo += 1
    if thunder == 1 and met == 1 and pain == 1 and drac == 1:
        eyy += 1
    
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
        
pper = (playable/count)*100
nibper = (nibprot/count)*100
dbper = (delbric/count)*100
nfafper = (nfaf/count)*100
nfafbricper = (nfafbric/count)*100
print(eyy)
print(playable)
print("percentage playable: %d" % pper + "%")
print("percentage playable throught nib: %d" % nibper + "%")
print("percentage bricks with delta: %d" % dbper +"%")
print("percentage hands with 2 fafnir: %d" % nfafper +"%" + "  %d" % nfaf)
print("percentage bricks with 2 fafnir: %d" % nfafbricper +"%" + "  %d" % nfafbric)