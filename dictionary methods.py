a = {0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:0}
c = {0:(9,8),1:(7,6),2:(5,4),3:(3,2),4:(1,0)}
b = {10:11,11:12,12:13,13:14,14:15,15:16,16:17,17:18,18:19,19:10}
print(a,"Value of a")
print(a.copy(), "value of .copy")
print(a.fromkeys(a, 555555), "value of .fromkeys")
print(a.get(1), " value of .get")
print(a.items(), "value of .items")
print(a.keys(), "value of .keys")
print(a.pop(1), "Value of .pop")
print(a.popitem(), "value of .popitem")
print(a.setdefault(1), "value of .setdefault")
print(a.update(a), "value of .update")
print(a.values(),"value of .values")
print(a.clear(),"value of .clear")