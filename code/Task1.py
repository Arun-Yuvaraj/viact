#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import json
import pandas as pd


# In[ ]:


# Reading Bbox_labels_600_hierarchy json
with open('C:\\Users\\Arun Yuvaraj\\Desktop\\new\\wheat\\new\\Regan - Full Time AI Engineer - Technical test\\interview\\task1\\bbox_labels_600_hierarchy.json') as json_file:
    data = json.load(json_file)


# In[ ]:


# Reading Oidv6-class-descriptions.csv to map ids with class name
reference = pd.read_csv('C:\\Users\\Arun Yuvaraj\\Desktop\\new\\wheat\\new\\Regan - Full Time AI Engineer - Technical test\\interview\\task1\\oidv6-class-descriptions.csv')

# creating 2 dictionaries, in first dictionary, id is the key and in second, class name is the key
reference_dict = dict(zip(reference.DisplayName, reference.LabelName))
reference_dict_1 = dict(zip(reference.LabelName, reference.DisplayName))


# In[ ]:


# i have downloaded a new csv file from Open Image 6, will use these names to fetch parent, ancestor and sibling class
df = pd.read_csv('C:\\Users\\Arun Yuvaraj\\Desktop\\new\\wheat\\new\\class-descriptions-boxable.csv')
name_list = df["Label"].tolist()
name_list


# In[ ]:


# Flattened json
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# In[ ]:


# functions to fetch parent,ancestor and sibling
def get_parent(mid):
    count = []
    parent_id = []
    for key, value in flat_data.items():
        if mid == value:
            count.append(key)
    
    for m in range(len(count)):
        parent_name = []
    
        name = count[m]
        string = ''
        d = name.split('_')
        if len(d) == 3:
            parent_name.append(d[-1])
            
        elif len(d) == 1:
            return None
        else:
            for i in range(len(d) - 3):
                string = string + d[i] + '_'
            string += 'LabelName'
            parent_name.append(string)
        
        for y in range(len(parent_name)):
            if flat_data[parent_name[y]] not in parent_id:
                parent_id.append(flat_data[parent_name[y]])
    return (parent_id)
    
def get_ancestors(mid):
    count = []
    
    ancestors_name = []
    ancestors_id = []
    for key, value in flat_data.items():
        if mid == value:
            count.append(key)
    
    for m in range(len(count)):
        ancestors_name = []
        name = count[m]
        d = name.split('_')
        length = len(d)
        while length > 3:
            string = ''
            for i in range(length - 3):
                string = string + d[i] + '_'
            string += 'LabelName'
            ancestors_name.append(string)
            length = length - 2
        else:
            if length == 3 or length == 1:
                ancestors_name.append(d[-1])
        if len(ancestors_name) > 1:
            ancestors_name = ancestors_name[1:]
        else:
            ancestors_name = None
        
        if ancestors_name:
            for y in range(len(ancestors_name)):
                if flat_data[ancestors_name[y]] not in ancestors_id:
                    ancestors_id.append(flat_data[ancestors_name[y]])
    return ancestors_id

def get_sibling(mid):
    
    count = []
    sib_id = []
    for key, value in flat_data.items():
        if mid == value:
            count.append(key)
    #print(count)
    for m in range(len(count)):
        i = 0
        sib_name = []
        name = count[m]
        d = name.split('_')
        length = len(d)
        if length > 1:
            while True:
                d[length-2] = str(i)
                name = '_'.join(d)
                if name not in flat_data:
                    break
                else:
                    sib_name.append(name)
                    i += 1
            for y in range(len(sib_name)):
                if flat_data[sib_name[y]] not in sib_id:
                    sib_id.append(flat_data[sib_name[y]])

        else:
            return None
    return(sib_id)


# ## Option1 : TO get parent, ancestor and sibling class name of the class given in csv

# In[ ]:


parent = []
ancestor = []
sibling = []
df_new = pd.DataFrame()

#creating a new data frame with all the class name, its parent, ancestor and sibling class name

for e in range(len(name_list)):
    name = name_list[e]
    id = reference_dict[name]
    parent_id = get_parent(id)

#     print('Parent Name')
    parent_name = []
    for i in range(len(parent_id)):
        if parent_id[i] == '/m/0bl9f':
            continue
        parent_name.append(reference_dict_1[parent_id[i]])

    parent.append(parent_name)



    ances_id = get_ancestors(id)
#     print('Ancestors Name')
    ances_name = []
    for i in range(len(ances_id)):
        if ances_id[i] == '/m/0bl9f':
            continue
        ances_name.append(reference_dict_1[ances_id[i]])
    
    ancestor.append(ances_name)
    # if len(at(None)

#     print('Sibling Name')
    sibling_id = get_sibling(id)

    if sibling_id:
        idx = sibling_id.index(id)
        sibling_id = sibling_id[:idx] + sibling_id[idx+1 :]
        sibling_name = []
        for i in range(len(sibling_id)):
            if sibling_id[i] == '/m/0bl9f':
                continue
            sibling_name.append(reference_dict_1[sibling_id[i]])
        sibling.append(sibling_name)
    else:
        sibling.append('None')

df_new['Class'] = name_list
df_new['Parent'] = parent
df_new['Ancestor'] = ancestor
df_new['Sibling'] = sibling


# ## Option2: TO get parent, ancestor and sibling class name of single class

# In[ ]:


# Put the class name below and execute, after execution the parent class, sibling and ancestor class will be printed.
name = 'Chopsticks'
id = reference_dict[name]
parent_id = get_parent(id)

# print('Parent Name')
parent_name = []
for i in range(len(parent_id)):
    if parent_id[i] == '/m/0bl9f':
        continue
    parent_name.append(reference_dict_1[parent_id[i]])
print(parent_name)



ances_id = get_ancestors(id)
# print('Ancestors Name')
ances_name = []
for i in range(len(ances_id)):
    if ances_id[i] == '/m/0bl9f':
        continue
    ances_name.append(reference_dict_1[ances_id[i]])
print(ances_name)
# if len(at(None)

# print('Sibling Name')
sibling_id = get_sibling(id)

if sibling_id:
    idx = sibling_id.index(id)
    sibling_id = sibling_id[:idx] + sibling_id[idx+1 :]
    sibling_name = []
    for i in range(len(sibling_id)):
        if sibling_id[i] == '/m/0bl9f':
            continue
        sibling_name.append(reference_dict_1[sibling_id[i]])
    print(sibling_name)
else:
    print('None')
# print(len(sibling))


# ## to get classes with same ancestor

# In[ ]:


df_final = pd.DataFrame()
anc = []
cla = []
for ind in df_new.index:
    a1 = df_new['Ancestor'][ind]
    print(a1)
    if not a1:
        continue
    a1_s = set(a1)
    c1 = df_new['Class'][ind]
    for ind in df_new.index:
        a2 = df_new['Ancestor'][ind]
        c2 = df_new['Class'][ind]
        a2_s = set(a2)
        if a2_s == a1_s:
            if c1 == c2:
                continue
            anc.append(str(a2))
            cla.append((c1,c2))
df_final['Ancestor'] = anc
df_final['Class'] = cla
            

