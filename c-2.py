g = []
def add(g):
    #{'g':[5]}  locals added to dict first element
    a = locals().pop('g')[0]
    #{'g':[5], 'a':5}  locals added to dict "a"
    b = 5
    #{'g':[5], 'a':5, 'b':5}  locals added to dict "b"
    try:
        #{'g':[5], 'a':5, 'b':5}  nothing here still same dict
        t=(g,)
        #{'g':[5], 'a':5, 'b':5, 't':([5],)}  locals stored "t" as key and tuple as value to  dict
        t[0] += [4]     #here locals stored 4 to list of t[0] and to list g as it mansioned above in line 10
        #line 12 error, becuse we can not change/modify tuple
    except:
        #dict is {'g': [5, 4], 'a': 5, 'b': 5, 't': ([5, 4],)}
        #as in line 12 was the error function jumped to except
        c = 6
        #{'g': [5, 4], 'a': 5, 'b': 5, 't': ([5, 4],), 'c': 6} locals stored c element
        del b   #here function deleted b element from dict
    return vars()               #vars here acts like locals, because no argument passed

result = add([5])   #final result is {'g': [5, 4], 'a': 5, 't': ([5, 4],), 'c': 6}