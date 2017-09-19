
# coding: utf-8

# In[1]:

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

critics['Lisa Rose']['Lady in the Water']


# In[7]:

#critics['Toby']['Snakes on a Plane'] = 4.5
critics['Toby']


# In[8]:

#from math import sqrt
sqrt(pow(4.5-4,2)+pow(1-2,2))


# In[10]:

1/(1+sqrt(pow(4.5-4,2)+pow(1-2,2)))


# In[36]:

def sim_distance(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
    if len(si) == 0:return 0 
    
    sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
   
    return 1/(1+sqrt(sum_of_squares))


# In[37]:

sim_distance(critics,'Lisa Rose','Gene Seymour')


# In[38]:

sim_distance(critics,'Lisa Rose','Toby')


# In[39]:

# def sim_distance(prefs,person1,person2):#验证item与si
#     si = {}
#     for item in prefs[person1]:
#         #print(item)
#         if item in prefs[person2]:
#             si[item] = 1
#             print('\n',si)
# sim_distance(critics,'Lisa Rose','Gene Seymour')


# In[ ]:



