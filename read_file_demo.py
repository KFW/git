import datetime as dt

events = []

with open('events.txt') as f:
    for line in f:
        l = line.strip().split(",")
        event = (l[0], dt.date(int(l[1]),int(l[2]), int(l[3])))
        events.append(event)
        

print(events)