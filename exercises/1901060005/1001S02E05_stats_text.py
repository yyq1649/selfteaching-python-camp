text = ''' The Zen of Python, by Tim Peters
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''


t1 = text.replace(',',' ')
t1 = t1.replace('--',' ')
t1 = t1.replace('*',' ')
t2=t1.split()
res = {}
for i in t2:
    if i in res:
        res[i] = res[i] + 1
    else:
        res[i] = 1
#print(res)
#print (sorted(res,key=str.lower))
t3 = sorted(res.items(),key=lambda x:x[1],reverse=True)
#对字典按值（value）进行排序
print(t3)


