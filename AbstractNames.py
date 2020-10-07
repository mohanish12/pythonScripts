def abstract_names(listOfNames):
    dictOfNames = {}
    for list in listOfNames:
        for name in list:
            if (name.split()[0] in dictOfNames):
                #dictOfNames[name.split()[1]].append(name.split()[2])
                dictOfNames[name.split()[0]].append(name.split()[1])
                #dictOfNames.append({name.split()[0] : name.split()[1]})
                #dictOfNames.update({name.split()[0]: name.split()[1]})
                #dictOfNames[name.split()[0]].


                #print(dictOfNames)
            else:
                #dictOfNames["David"] = "Values"
                dictOfNames[name.split()[0]] = [name.split()[1]]
                #print(dictOfNames)

    return(dictOfNames)


print(abstract_names([["David Joyner", "David Tennant", "David Beckham"], ["Ananya Birla", "Ananya Agarwal", "Ananya Chatterjee", "Ananya Roy"],["Inés Sainz", "Inés Suarez", "Inés Melchor"]]))
