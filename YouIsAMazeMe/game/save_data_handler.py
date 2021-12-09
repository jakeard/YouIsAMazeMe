import json

_loader_path = _loader_path = "YouIsAMazeMe/levels/curr_data.json"
    
def load_from_json():
    """Searches in the specified loader path for a json save data file. 
    If it's there, then it will load it into self.save_data as a dictionary.
    Otherwise, it will create a brand new file."""
    try: 
        # Is there already a file? If so, proceed.
        with open(_loader_path, 'r') as rpath:
            # Is there existing save data? If so, load it.
            save_data = json.load(rpath)

    except:
        # If not, create a new one and load as normal.
        with open(_loader_path, 'w') as wpath:
            # initializes the json file
            # If we want to add new things to be saved, we must initialize it in this dictionary here.
            # ex: new_data = {'curr_lvl':1, 'char_sel':6, 'total_score':0}
            new_data = {'curr_lvl':1}
            json.dump(new_data, wpath)

        with open(_loader_path, 'r') as rpath:
            save_data = json.load(rpath)

    return save_data

def save_to_json(save_data):
    with open(_loader_path, 'w') as wpath:
        json.dump(save_data, wpath)