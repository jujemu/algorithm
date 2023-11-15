def solution(survey, choices):
    d = {
        "rion": 0,
        "corn": 0,
        "jay-g": 0,
        "apeach": 0
    }
    
    answer = []
    for s, c in zip(survey, choices):
        if s in ["AN", "NA"]:
            d["apeach"] += c-4 if s == "NA" else 4-c
        if s in ["JM", "MJ"]:
            d["jay-g"] += c-4 if s == "MJ" else 4-c
        if s in ["CF", "FC"]:
            d["corn"] += c-4 if s == "FC" else 4-c
        if s in ["RT", "TR"]:
            d["rion"] += c-4 if s == "TR" else 4-c
    
    for character in d:
        if character == "rion":
            answer.append("R" if d[character] >= 0 else "T")
        elif character == "corn":
            answer.append("C" if d[character] >= 0 else "F")
        elif character == "jay-g":
            answer.append("J" if d[character] >= 0 else "M")
        else:
            answer.append("A" if d[character] >= 0 else "N")
                
    return "".join(answer)