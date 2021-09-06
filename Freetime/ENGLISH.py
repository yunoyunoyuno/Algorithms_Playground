w = set();
u = "Great expedite adolescent affair affection fondness affluent aggravate exasperate forefather archaic apparent dispute aspire congregate assess appraise heed presence at-hand Conduct bereaved mournful brittle cessation defy circumstance occurrence relapse clash commodity merchandise convey companion correlate redeem constituent conform assurance confidential affirm conscious Great comprise confer counsel adulterate contend neutralize hazardous cope-with decline deject deprive bereave devastation destruction detest despise detrimental perilous devious perish diminutive miniature abhorrence deviate dominance drought shortage dwelling splendid enormous colossal enthusiastic zealous entrepreneur envious erode evade elude overstate scrutinize excessive surplus fatigue extinguish supreme utmost authentic famine starvation captivate enchant fare prohibit coerce oblige foremost fruitful fertile profuse dispose-of gloomy grievous graceful gradually grief affliction endorse cultivate hatch brood haunting hibernation illegible illiterate"
u2 = "elucidate aliment affliction floodlight promptly passive incessant unceasing incidence infant inferior inflamation eruption inhabit reside abide innate inborn inbred intellectual inquire unite unify severity ironic sarcastic justify jeopardize lantern literally virtually yearn-for extravagance sustenance means mode meteorology immigrate emigrate mild tender minute diminutive marvelous assorted misery agony mobile moderate mysterious puzzling bargain notable numerous numberless nourishment supplement oppose object oblivious unmindful notice remark Observable noticeable obstruction Engage offhand antique Treatment Striking surmount rout pension provident-fund perceive periodical everlasting Please delight Content ponder Reflect Post pragmatic predominance prevalent prevailing pervasive foregoing Precedence proliferate Prominent eminent asset prosperous affluent scarce Sensible recuperate reform regard relieve reluctant Distant requisite resevoir dam Resolve lodge Riches restless curriculum-vitae resign miserable self-assured self-esteem self-sustaining sentimental sluggish soothe alleviate stubborn obstinate suburb rural suffocate stifle oversee supress oppress superfluous doubtful dubious surveillance syndrome tactful diplomatic tease Device tempt allure thereby intimidate tolerate tough cue tragedy transmit virtually ulcer undergo variable assorted vending vigorous forceful severity virtue integrity welfare fringe-benefit untidy urban downtown vacant Vague obscure wander ramble endorse vanquish wither withhold keep-back withstand Decline dEcline"
u = u2.split();
#u = u.split();
for e in u: w.add(e);
while(len(w) > 0):
    print("We have",len(w),"words left for U ( •̀ ω •́ )✧\n");
    s = w.pop();
    print(s)
    n = input("y ? => ");
    if(n == 'r') : 
        print("\nSucessful Restart!\n")
        for e in u: w.add(e);
    elif(n != 'y'): print("\nToo bad... .·´¯`(>▂<)´¯`·. \n"); w.add(s);


