from apriori import Apriori

data = {100: (1, 3, 4), 200: (2, 3, 5), 300:(1, 2, 3, 5), 400:(2, 51)}
db = Apriori(data)
#print ("dbase", db.dbase)
# print("candidates, S7", db.candidates_sz) 
# print ("support _history", db.support_history)
# print("candidates", db.candidates)
#print("current", db.current)

# for x in data: print(x, data[x])
# print('------')
# #for x,v in data.items(): 
data = {100:[1, 3, 4], 200:[2, 3, 5], 300:[1, 2, 3, 5], 400:[2, 5]}
db = Apriori(data)

print("current", db.current)
print('------------------------------------')
print("support(.7)", db.support(.7))
print("support(.2)", db.support(.2))
print('------------------------------------')
print("#{}#".format('='*73))
db.scan_dbase(.7)
print("support_history", db.support_history)
print("current", db.current)