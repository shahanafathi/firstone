# d={1:'red',2:'green',"color":'blue'}
# # print(d)
# # print(d['color'])
# # d['day']="fri"
# # print(d)
# # d['color']="yello"
# # print(d)
# # del d[1]
# # print(d)
# # for i in d:
# #     print(d[i])
# # num=[1,2,3,4]
# # a=[i for i in [1,2,3,4,5,6,7,8,9,10] if i%2==0]
# # print(a)
# b=[[i for i in range(3)] for i in range(4)]
# print(b)
# l=[1,2,3,4,5,6,7,8,9,10]
# set={ i*3 for i in l if i%2==0 }
# print(set)
# a=['a','b','c']
# b=[1,2,3]
# # s={i:j for (i,j) in zip(a,b)}
# # print(s)
# # s=dict(zip(a,b))
# # print(s)
# # a={x.upper():x*3 for x in 'coding'}
# # print(a)

a="ABc"
dic={i:{y:i+y for y in a} for i in a}
print(dic)