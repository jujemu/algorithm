tag = []
title = []
inTag, tagName = False, None
inP, para = False, []
for c in input():
    if c == "<":
        inTag = True
        tagName = []
        continue

    if c == ">":
        inTag = False
        tagName = "".join(tagName)

        if inP:
            if tagName == "/p":
                inP = False
            continue

        if tagName[:3] == "div" and not inP:
            try:
                titleIndex = tagName.index("=")
                title.append(tagName[titleIndex+2:-1])
                tagName = "div"
            except ValueError:
                # 'tagName'에 '='이 없는 경우
                pass
        elif tagName[:4] == "/div" and not inP:
            para.append("newBlock")
        elif tagName == "p":
            inP = True
            para.append([])
        tag.append(tagName)

    else:
        if inTag:
            tagName.append(c)
        else:
            if c == " " and para and para[-1] and para[-1][-1] == " ":
                continue
            if para:
                para[-1].append(c)

# print(*tag)
# for p in para:
#     print("".join(p))
# print(title)

p_i = 0
for t in title:
    print("title :", t)
    while p_i < len(para) and para[p_i] != "newBlock":
        p = "".join(para[p_i]).strip()
        while p and p[-1] == " ":
            p = p[:-1]
        while p and p[0] == " ":
            p = p[1:]
        print(p)
        p_i += 1
    if p_i < len(para):
        p_i += 1

