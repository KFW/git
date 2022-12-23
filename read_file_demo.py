import datetime as dt

events = []

with open('events.txt') as f:
    for line in f:
        events.append(line.strip().split(","))

print(events)