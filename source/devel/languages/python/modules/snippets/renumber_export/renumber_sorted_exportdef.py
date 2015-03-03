"""
Python2.6 script to renumber and sort the functions from a visual C++ export file.
"""

list_functions=[]

# read the list of functions
with open('export.def', 'r') as f:
    for line in f.readlines():
        line2 = line.split('@')
        if (len(line2)>=2):
            function=line2[0].strip()
            list_functions += [function]

# to suppress the possible duplicates
set_functions=set(list_functions)
# sorting the functions
list_functions_sorted=sorted(set_functions,reverse=False)

# write the sorted functions 
with open('renumber_sorted_export.def', 'w') as f:
    for i, function in enumerate(list_functions_sorted):
        s="\t{0:65}@{1}\n".format(function,i+1)
        f.write(s)

