from typing import List, Tuple
import json

NAME_COLLABORATIVE = "collaborative"
NAME_CONTENT = "content_based"
NAME_RANDOM = "random"
NAME_COLLAB_CLUSTER = "collaborative-clustering"

def write_recoms_by_movie(recoms: dict):
    with open("results/recoms-by-movie.json", 'w') as f:
        json_str = json.dumps(recoms)
        f.write(json_str)

def read_recoms_by_movie() -> dict:
    with open("results/recoms-by-movie.json", 'r') as f:
        return json.load(f)

def filename(name: str) -> str:
    return f"results/{name}.txt"
                       
def write_results(name: str, predicted: List[List[str]], actual: List[List[str]]):
    with open(filename(name), 'w') as f:
        f.write(list_list_to_string(predicted)+"\n")
        f.write(list_list_to_string(actual)+"\n")

def write_col_result(user_id: int, predicted: list, actual: list):
    write_results_new_format(NAME_COLLABORATIVE)
    
def write_results_new_format(name: str, user_id: int, predicted: list, actual: list):
    with open(filename(name), 'a') as f:
        actual_str = list_to_string(actual)
        pred_str = list_to_string(predicted)

        f.write(f"{user_id}|{pred_str}|{actual_str}\n") 

        
def read_results(name: str) ->  Tuple[List[List[str]], List[List[str]]]:
    with open(filename(name), 'r') as f:
        content = f.read()
        lines = content.split('\n')
        predicted = parse_list_list(lines[0])
        actual = parse_list_list(lines[1])
        
        return predicted, actual

def read_col_results() -> Tuple[List[List[str]], List[List[str]]]:
    with open(filename(NAME_COLLABORATIVE), 'r') as f:
        content = f.read()
        lines = content.rstrip().split('\n')
        predicted = []
        actual = []
        
        for line in lines:
            l = line.split('|')
            # user|predicted|actual
            pred = parse_list(l[1])
            act = parse_list(l[2])

            predicted.append(pred)
            actual.append(act)
        
        return predicted, actual

def read_processed_users_for(name: str) -> List[str]:
    with open(filename(name), 'r') as f:
        content = f.read()
        if content == "":
            print("No processed users")
            return []
        lines = content.rstrip().split('\n')
        users = map(lambda l: int(l.split('|')[0]), lines)

    return list(users)
    
def read_processed_users() -> List[str]:
    return read_processed_users(NAME_COLLABORATIVE)
    
def list_list_to_string(ll: List[List[str]]):
    # [["1", "2", "3"], ["4"], ["5"]]
    # 1,2,3|4|5
    line = ""
    for l in ll:
        line += list_to_string(l) + "|"
    line = line[:-1]
    return line

def list_to_string(l: List[int]):
    # ["1", "2", "3"]
    # 1,2,3
    res = ""
    for s in l:
        res += str(s) + ","
    return res[:-1]

def parse_list_list(line: str):
    raw_lists = line.split('|')
    ll = []
    for raw_list in raw_lists:
        ll.append(parse_list(raw_list))
       
    return ll

def parse_list(s: str) -> list:
    return s.split(',')