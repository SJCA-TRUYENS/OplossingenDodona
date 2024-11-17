import time
huidige_tijd = time.time()

minuten = int((huidige_tijd / 60) % 60)
uren = int((huidige_tijd / 3600) % 24) + 1 #Door verschil in tijdzone GMT+1

print(str(uren) + ":" + str(minuten))