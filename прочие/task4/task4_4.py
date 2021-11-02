import os 
import json

def scan_folder(path):
    entries = os.listdir(path)

    if not entries:

        return None

    if len(entries) > 1:
        result = []
        for entry in entries:
            entry_path = path + '/' + entry
            if os.path.isfile(entry_path):
                result.append(entry)

            else:
                result.append(
                              {entry: scan_folder(entry_path)}
                              )
        return result


    entry = entries[0]
    entry_path = path + '/' + entry
    if os.path.isfile(entry_path):
        return entry
    else:
        return {entry: scan_folder(entry_path)}

dir = {'task4_test': scan_folder('task4_test')}

print(json.dumps(dir,indent=4, sort_keys=True).replace(": null",": None"))
