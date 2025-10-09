import json

with open('sample-data.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")

imdata = data["imdata"]

for i in imdata[:3]:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    
    print(dn,"         ",descr,"                 ",speed,"",mtu)

