g = []


def add(g):
    # {'g':[5]}  locals added to dict first element
    a = locals().pop('g')[0]
    # {'g':[5], 'a':5}  locals added to dict "a"
    b = 5
    # {'g':[5], 'a':5, 'b':5}  locals added to dict "b"
    try:
        # {'g':[5], 'a':5, 'b':5}  nothing here still same dict
        t = (g,)
        # {'g':[5], 'a':5, 'b':5, 't':([5],)}  locals stored "t" as key
        # and tuple as value to  dict

        # here locals stored 4 to list of t[0] and
        # to list g as it mansioned above in line 10
        t[0] += [4]
        # line 12 error, becuse we can not change/modify tuple
    except:
        # dict is {'g': [5, 4], 'a': 5, 'b': 5, 't': ([5, 4],)}
        # as in line 12 was the error function jumped to except
        c = 6

        # {'g': [5, 4], 'a': 5, 'b': 5, 't': ([5, 4],), 'c': 6}
        # locals stored c element

        # here function deleted b element from dict
        del b
    # vars here acts like locals, because no argument passed
    return vars()

# final result is {'g': [5, 4], 'a': 5, 't': ([5, 4],), 'c': 6}
result = add([5])
