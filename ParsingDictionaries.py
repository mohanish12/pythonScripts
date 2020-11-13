def check_value(dct, strg):
    for ky in dct:

            try:
                if (int(dct[strg])):
                    return("Integer!")
                    break
            except (ValueError):
                pass
            except (KeyError):
                return("Not Found!")
                break
            try:
                if (float(dct[strg])):
                    return("Float!")
                    break
            except (ValueError):
                pass
            except (KeyError):
                return("Not Found!")
                break
            try:
                if ((dct[strg])):
                    return("string")
                    break
            except (KeyError):
                return("Not Found!")
                break




d = {"k1": "1.1", "k2": "1", "k3": "1.4.6", "k4": "a"}

print(check_value(d, "k5"))

#check_value({"key1": "test", "key2": "value2"}, "test")
