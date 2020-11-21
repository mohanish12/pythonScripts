def volume_and_area(inDict):
    length = inDict["length"]
    width = inDict["width"]
    height = inDict["height"]
    inDict["volume"] = length * width * height
    inDict["area"] = 2 * ((length * width) + (length * height) + (width * height))
    return inDict



rectangle = {"length": 1, "width": 2, "height": 3}
print(volume_and_area(rectangle))