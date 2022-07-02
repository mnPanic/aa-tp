from typing import List, Tuple
import json

NAME_COLLABORATIVE = "collaborative"
NAME_CONTENT = "content_based"
NAME_RANDOM = "random"


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

def read_results(name: str) -> Tuple[List[List[str]], List[List[str]]]:
    with open(filename(name), 'r') as f:
        content = f.read()
        lines = content.split('\n')
        predicted = parse_list_list(lines[0])
        actual = parse_list_list(lines[1])
        
        return predicted, actual

def list_list_to_string(ll: List[List[str]]):
    # [["1", "2", "3"], ["4"], ["5"]]
    # 1,2,3|4|5
    line = ""
    for l in ll:
        for s in l:
            line += s + ","
        line = line[:-1]
        line += "|"
    line = line[:-1]
    return line

def parse_list_list(line: str):
    raw_lists = line.split('|')
    ll = []
    for raw_list in raw_lists:
        l = raw_list.split(',')
        ll.append(l)
       
    return ll  