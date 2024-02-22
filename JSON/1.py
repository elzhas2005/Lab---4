import json 

with open("sample-data.json",'r') as file:
  xxx = json.load(file)

print("Interface Status")
print("="*80)
print("mdix                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  -----")

for y in xxx['imdata'] :
   mdix = y['l1PhysIf']['attributes']["mdix"]
   Description = y["l1PhysIf"]['attributes']['descr'] 
   Speed = y["l1PhysIf"]['attributes']['speed']
   MTU = y["l1PhysIf"]['attributes']['mtu']
   if len(mdix) == 1 :
       print(mdix , Description ,"                            " , Speed , MTU)
   else:
       print(mdix , Description ,"                             ",Speed,MTU)