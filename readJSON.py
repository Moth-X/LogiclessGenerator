def readjs(filename=""):
    import json
    if filename != '':
        strlist = filename.split(".")
        if strlist[len(strlist)-1].lower() == "json":
            with open(filename, mode='r', encoding="utf-8") as file:
                return json.loads(file.read())
