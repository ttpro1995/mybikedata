import json
import os

PATH = "meta_data/unsort/jsons"


if __name__ == "__main__":
    dirlist = os.listdir(PATH)
    out = open(os.path.join(PATH, 'summary.csv'), 'w')
    for dir in dirlist:
        if  "json" in dir:
            full_path = os.path.join(PATH, dir)
            json_data = json.load(open(full_path))
            img_id = json_data["img_id"]
            count = json_data["human_num"]
            out.write(img_id+","+str(count)+"\n")
    out.close()