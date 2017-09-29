def img_and_disc(lst1, lst2):
    site = ""
    site += "<!doctype html>\n\t<html>\n\t\t<head>\n\t\t\t<title>CS194 project 1</title>\n\t\t</head>\n\t<body>"
    if (len(lst1) != len(lst2)):
        return
    for a, b in zip(lst1, lst2):
        site += "\n\t<div>\n\t\t<img src='{0}'>\n\t\t<p>\n\t\t\t{1}\n\t\t</p>\n\t</div>".format(a,b)
    site += "\n\t</body>\n</html>"
    return site


lst1 = [
"kramersface.jpg",
"mattjang.png",
"mewithmickeycho.jpg"
]

def picture_dir_prefix(lst):
    return ["../pictures/{0}".format(a) for a in lst]

lst2 = ["An old silent pond...",
"A frog jumps into the pond",
"splash! Silence again."]

site = img_and_disc(picture_dir_prefix(lst1), lst2)
webpage = open("index2.html","w")
webpage.write(site)
webpage.close()