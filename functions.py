#1

def flatten_dict(obj, parent=None, new_dict=None, sep='.'):
    if new_dict is None:
        new_dict = {}
    for key, value in obj.items():
        if parent:
            key = f"{parent}{sep}{key}"
        #print(key)
        if isinstance(value, dict):
            #print(value)
            flatten_dict(value, parent= key, new_dict=new_dict)
            continue
        new_dict[key] = value
        
        
    return new_dict



flattened_dict = flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4})
print(flattened_dict)

def unflatten_dict(obj):
    result_dict = dict()
    for key, value in obj.items():
        halfs = key.split('.')
        #print(halfs)
        d = result_dict
        for half in halfs[:-1]:
            #print(half)
            if half not in d:
                d[half] = dict()
            d = d[half]
        d[halfs[-1]] = value
    return result_dict

unflattened_dict = unflatten_dict(flattened_dict)
print(unflattened_dict)

#couldn't figure this one out
def treemap(list1):
    mapped_list = []
    i = 0
    for L in list1:
        if isinstance(L, list):
            while i < len(L):
                print(L[i])
                mapped_list.append(L[i].value * L[i].value)
                i += 1
            i=0
        else:
            print(L)
            value = L * L
            mapped_list.append(value)
    return mapped_list


treemap([1, 2, [3, 4, [5]]])