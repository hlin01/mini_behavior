OBJECTS = [
    "apple", "ashcan",
    "backpack", "ball", "banana", "basket", "beach_ball", "bed", "beef", "bin", "blender", "book", "bow", "box", "bread", "broom", "broom_set", "bucket", "bucket_toy",
    "cabinet", "cake", "calculator", "candle", "candy", "car", "cart_toy", "carton", "carving_knife", "casserole", "chicken", "chip", "cookie", "countertop",
    "date", "dustpan", # door
    "egg", "electric_refrigerator",
    "farm_toy", "fish", "folder", "fork", # "floor",
    "gear", "gear_pole",
    "gym_shoe",
    "hamburger", "hammer", "hardback",
    "jar", "jewelry", "juice",
    "kettle", "knife",
    "lemon", "lettuce",
    "mallet", "music_box", # New object for infantRL
    "necklace", "notebook",
    "olive",
    "package", "pan", "pen", "pencil", "plate", "piggie_bank", "plywood", "pop", "printer",
    "rattle", "radish", "rag", "ring_toy",
    "salad", "sandwich", "saw", "scrub_brush", "shape_sorter", "shelf", "shoe", "shower", "sink", "soap", "sock", "sofa", "soup", "spiky_ball", "spoon", "stove", "strawberry", "stroller",
    "table", "tea_bag", "teapot", "tree_busy_box", "toilet", "tomato", "towel",
    "vegetable_oil",
    "water", "window", "winnie", "winnie_cabinet",
    "pot_plant", "marker", "chair", "document", "oatmeal", "sugar"
    "water", "window",
    "pot_plant", "marker", "chair", "document", "oatmeal", "sugar",
    "rattle", "red_spiky_ball"
]

FURNITURE = ['ashcan', 'bed', 'bin', 'box', 'bucket', 'cabinet', 'chair', 'car', 'countertop', 'electric_refrigerator', 'gear_pole', 'music_box', 'shelf', 'shower', 'sink', 'sofa', 'stove', 'table', 'window']
# Map of object type to integers
OBJECT_TO_IDX = {
    'unseen': 0,
    'empty': 1,
    "apple": 2,
    "ashcan": 3,
    "backpack": 4,
    "ball": 5,
    "banana": 6,
    "basket": 7,
    "bed": 8,
    "beef": 9,
    "bin": 10,
    "blender": 11,
    "book": 12,
    "bow": 13,
    "bread": 14,
    "broom": 15,
    "bucket": 16,
    "cabinet": 17,
    "cake": 18,
    "calculator": 19,
    "candy": 20,
    "car": 21,
    "carton": 22,
    "carving_knife": 23,
    "casserole": 24,
    "chicken": 25,
    "chip": 26,
    "cookie": 27,
    "countertop": 28,
    "date": 29,
    "door": 30,
    "dustpan": 31,
    "egg": 32,
    "electric_refrigerator": 33,
    "fish": 34,
    "floor": 35,
    "folder": 36,
    "fork": 37,
    "gym_shoe": 38,
    "hamburger": 39,
    "hammer": 40,
    "highlighter": 41,
    "jar": 42,
    "jewelry": 43,
    "juice": 44,
    "kettle": 45,
    "knife": 46,
    "lemon": 47,
    "lettuce": 48,
    "necklace": 49,
    "notebook": 50,
    "olive": 51,
    "package": 52,
    "pan": 53,
    "pen": 54,
    "pencil": 55,
    "plate": 56,
    "plywood": 57,
    "pop": 58,
    "printer": 59,
    "radish": 60,
    "rag": 61,
    "salad": 62,
    "sandwich": 63,
    "saw": 64,
    "scrub_brush": 65,
    "shelf": 66,
    "shoe": 67,
    "shower": 68,
    "sink": 69,
    "soap": 70,
    "sock": 71,
    "sofa": 72,
    "soup": 73,
    "spoon": 74,
    "stove": 75,
    "strawberry": 76,
    "table": 77,
    "tea_bag": 78,
    "teapot": 79,
    "toilet": 80,
    "tomato": 81,
    "towel": 82,
    "vegetable_oil": 83,
    "wall": 84,
    "water": 85,
    "window": 86,
    "pot_plant": 87,
    "marker": 88,
    "chair": 89,
    "document": 90,
    "oatmeal": 91,
    "sugar": 92,
    "candle": 93,
    "box": 94,
    "hardback": 95,
    "goal": 96,
    "agent": 97,
    "mallet": 98,
    "music_box": 99,
    "gear": 100,
    "gear_pole": 101,
    "beach_ball": 102,
    "broom_set": 103,
    "bucket_toy": 104,
    "cart_toy": 105,
    "farm_toy": 106,
    "ring_toy": 107,
    "shape_sorter": 108,
    "spiky_ball": 109,
    "stroller": 110,
    "tree_busy_box": 111,
    "winnie": 112,
    "winnie_cabinet": 113,
    "rattle": 114,
    "red_spiky_ball": 115
}


IDX_TO_OBJECT = dict(zip(OBJECT_TO_IDX.values(), OBJECT_TO_IDX.keys()))


OBJECT_TO_STR = {
    "apple": "A",
    "ashcan": "A",
    "backpack": "B",
    "ball": "B",
    "banana": "B",
    "basket": "B",
    "bed": "B",
    "beef": "B",
    "bin": "B",
    "blender": "B",
    "book": "B",
    "bow": "B",
    "bread": "B",
    "broom": "B",
    "bucket": "B",
    "cabinet": "C",
    "cake": "C",
    "calculator": "C",
    "candy": "C",
    "car": "C",
    "carton": "C",
    "carving_knife": "C",
    "casserole": "C",
    "chicken": "C",
    "chip": "C",
    "cookie": "C",
    "countertop": "C",
    "date": "D",
    "door": "D",
    "dustpan": "D",
    "egg": "E",
    "electric_refrigerator": "E",
    "fish": "F",
    "floor": "F",
    "folder": "F",
    "fork": "F",
    "gear": "G",
    "gear_pole": "G",
    "gym_shoe": "G",
    "hamburger": "H",
    "hammer": "H",
    "highlighter": "H",
    "jar": "J",
    "jewelry": "J",
    "juice": "J",
    "kettle": "K",
    "knife": "K",
    "lemon": "L",
    "lettuce": "L",
    "mallet": "M",
    "music_box": "M",
    "necklace": "N",
    "notebook": "N",
    "olive": "O",
    "package": "P",
    "pan": "P",
    "pen": "P",
    "pencil": "P",
    "plate": "P",
    "plywood": "P",
    "pop": "P",
    "printer": "P",
    "radish": "R",
    "rag": "R",
    "salad": "S",
    "sandwich": "S",
    "saw": "S",
    "scrub_brush": "S",
    "shelf": "S",
    "shoe": "S",
    "shower": "S",
    "sink": "S",
    "soap": "S",
    "sock": "S",
    "sofa": "S",
    "soup": "S",
    "spoon": "S",
    "stove": "S",
    "strawberry": "S",
    "table": "T",
    "tea_bag": "T",
    "teapot": "T",
    "toilet": "T",
    "tomato": "T",
    "towel": "T",
    "vegetable_oil": "V",
    "wall": "W",
    "water": "W",
    "window ": "W",
    "pot_plant": "P",
    "marker": "M",
    "chair": "C",
    "oatmeal": "O",
    "sugar": "S",
    "box": "B",
    "hardback": "H",
    "candle": "C",
    "rattle": "R",
    "red_spiky_ball": "R"
}

FURNITURE_CANNOT_ON = ['ashcan', 'bed', 'bin', 'chair', 'shower', 'car', 'sink', 'window']
