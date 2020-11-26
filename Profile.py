def complete_profile(inDict):
    inDict["name"] = inDict["first"] + " " + inDict["last"]
    inDict["full_name"] = inDict["title"]  + " " +  inDict["first"] + " " + inDict["middle"] + " " + inDict["last"]
    inDict["short_name"] = inDict["first"][0] + " " +  inDict["last"]

    return inDict


print(complete_profile({"first": "David", "middle": "Andrew", "last": "Joyner", "title": "Dr."}))