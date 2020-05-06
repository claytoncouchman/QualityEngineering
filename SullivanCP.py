#!/usr/bin/env python
# coding: utf-8

# In[2]:


def ChangePoint(data):
    import numpy as np
    from math import sqrt
    def MinDist(groups):
        for key,group in tuple(groups.items())[:-1]:
            try:
                if mini > group.dist:
                    mini = group.dist
                    loc = key
            except: 
                mini = group.dist
                loc = key
        return (loc, mini)
    class Group:
        def __init__ (self, values, dist = None):
            self.values = np.array(values)
            self.mean = self.values.mean()
            try:
                self.size = len(self.values)
            except:
                self.size = 1
            self.dist = dist
    def CalcDist(group1, group2):
        if k < .2*m:
            s = 1
        else:
            var = 0
            for key in groups.keys():
                var += np.var(groups[key].values)
            s = sqrt((1/(m-.2*m-1))*(var))
        return abs(group1.mean-group2.mean)/(s*sqrt((group1.size+group2.size)/(group1.size*group1.size)))

    def MinDist(groups):
        for key,group in tuple(groups.items())[:-1]:
            try:
                if mini > group.dist:
                    mini = group.dist
                    loc = key
            except: 
                mini = group.dist
                loc = key
        return (loc, mini)

    # declare variables
    k = 1
    m = len(data)
    boundaries = [i for i in range(1,m+1)]
    groups = {b-1: Group(d) for (b,d) in zip(boundaries, np.array(data))}
    for key in list(groups.keys())[:-1]:
        groups[key].dist = CalcDist(groups[key],groups[key+1])

    lstar = []
    dstar = []
    
    while (m-k)> 0:
        # Find Min Distance
        (loc,dist) = MinDist(groups)

        # Save changes
        lstar.insert(0,loc+1)
        dstar.insert(0,dist)

        # Update new cluster values
        nextpos = list(groups.keys())[(list(groups.keys()).index(loc)+1)]
        groups[nextpos].values = np.append(groups[nextpos].values,groups[loc].values)
        groups[nextpos].mean = groups[nextpos].values.mean()
        groups[nextpos].size = len(groups[nextpos].values)

        if nextpos != list(groups.keys())[-1]:
            next2pos = list(groups.keys())[list(groups.keys()).index(loc)+2]
            groups[nextpos].dist = CalcDist(groups[nextpos],groups[next2pos])

        else:
            groups[nextpos].dist = None

        groups.pop(loc)

        k+=1
    return(dstar)


# In[ ]:




