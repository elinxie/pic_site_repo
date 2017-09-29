def string_gen(lst, lst2):
    		for l, k in zip(lst, lst2):
            		print("<div>\n<img src='color_output/color_{0}.jpg' height=342px width=390px>\n<p>\n{1}\n</p>\n</div>".format(l[0:-4], k))

names = ['cathedral.jpg', 'harvesters.tif', 'icon.tif', 'lady.tif', 'monastery.jpg', 'nativity.jpg', 'self_portrait.tif', 'settlers.jpg', 'three_generations.tif', 'train.tif', 'turkmen.tif', 'boy_bridge.jpg', 'fortress.jpg','mosque.jpg', 'woman_gate.jpg', 'emir.tif', 'village.tif']

coordinates = ["green displacement: x = 5, y = 2 red displacement: x = 12, y = 3",
"green displacement: x = 59, y = 17 red displacement: x = 124, y = 15",
"""green displacement: x = 41, y = 18
red displacement: x = 90, y = 23""",
"""green displacement: x = 54, y = 8
red displacement: x = 116, y = 10""",
"""green displacement: x = -3, y = 2
red displacement: x = 3, y = 2""",
"""green displacement: x = 3, y = 1
red displacement: x = 8, y = 0""",
"""green displacement: x = 78, y = 29
red displacement: x = 175, y = 37""",
"""green displacement: x = 7, y = 0
red displacement: x = 15, y = -1""",
"""green displacement: x = 50, y = 14
red displacement: x = 110, y = 12""",
"""green displacement: x = 42, y = 6
red displacement: x = 86, y = 32""",
"""green displacement: x = 56, y = 22
red displacement: x = 117, y = 29""",
"""green displacement: x = 4, y = -2
red displacement: x = 10, y = -1""",
"""green displacement: x = 3, y = 0
red displacement: x = 10, y = 0""",
"""green displacement: x = 2, y = 1
red displacement: x = 7, y = 1""",
"""green displacement: x = 2, y = 1
red displacement: x = 9, y = 1""",
"""green displacement: x = 51, y = 28
red displacement: x = 108, y = 43""",
"""green displacement: x = 68, y = 16
red displacement: x = 139, y = 26"""]
string_gen(names,coordinates)
