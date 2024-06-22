sports ={"bat","ball","football","Hockey","baseball"}
for x in sports:
    if x == "Hockey":
        print("Hockey is found")
        break
    else:
        print(x)


new_sports = {"soccer","Hockey"}
mix = sports.difference(new_sports)
print(mix)

z = new_sports.copy()
print(z)

#sports.remove("bat")
#print(sports)