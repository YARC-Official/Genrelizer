import json
import os
import sys

hasError = False
keys = []


def CI(message, is_error=False):
    global hasError
    if is_error:
        hasError = True
    if os.getenv("CI") == "true":
        print(message)


def addKey(key, file):
    global keys
    if key in keys:
        print(f"ERROR: {key} generated redundantly in {file}")
        CI(f"::error file={file}::[mappings] {key} generated redundantly in {file}", True)
    else:
        keys.append(key)


def addAllKeys(name, data, file):
    results = []
    substitutions = data.get("substitutions", {})
    prefixes = data.get("prefixes", [])
    suffixes = data.get("suffixes", [])

    substitution_sets = [[]]
    for substring in substitutions.keys():
        substitution_list = substitutions[substring]
        substitution_sets_to_add = []
        for substitutionSet in substitution_sets:
            for substitution in substitution_list:
                substitution_sets_to_add.append(substitutionSet + [(substring, substitution)])
        substitution_sets.extend(substitution_sets_to_add)

    for substitutionSet in substitution_sets:
        result = name
        for substitution in substitutionSet:
            result = result.replace(substitution[0], substitution[1])
        results.append(result)

        for suffix in suffixes:
            results.append(result + suffix)
            for prefix in prefixes:
                results.append(prefix + result + suffix)

        for prefix in prefixes:
            results.append(prefix + result)

    for key in results:
        addKey(key, file)



def scanFile(file):
    filedata = json.load(open(file, mode="r", encoding="utf-8"))
    addAllKeys(filedata["name"].lower(), filedata, file)
    for key in filedata["subgenres"].keys():
        addAllKeys(key.lower(), filedata["subgenres"][key], file)


for file in os.listdir("mappings"):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        scanFile("mappings/" + file)
    else:
        print(f"ERROR: Unexpected non-JSON file {file}")
        CI(f"::error file={file}::[mappings] Unexpected non-JSON file {file}", True)

if hasError == True:
    sys.exit(1)