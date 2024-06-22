apps = ["Fb","Insta","Tik-tok","Moj","Mx Taka-tak"]
for i in apps:
    if i == "Moj":
        print("Moj is found")
        break
    else:
        print(i)
apps.remove("Insta")
print(apps)
z = apps.count("Tik-tok")
print(z)
apps.copy()
print(apps)
apps.insert(1,"Tinder")
print(apps)
apps.reverse()
print(apps)
apps.sort()
print(apps)
print(len(apps))
print(type(apps))
print(type(i))