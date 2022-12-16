string = "python is good language to code"
nspace = string.replace(' ', '')

dictionary  = {nspace[i]: nspace.count(nspace[i]) for i in range(len(nspace))}
print(dictionary)