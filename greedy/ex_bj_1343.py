pol = input().split(".")
for idx, p in enumerate(pol):
    if p:
        if len(p) % 2:
            pol = False
            break
        
        pol[idx] = "AAAA" * (len(p) // 4) + "BB" * (1 if len(p) % 4 else 0)
print(".".join(pol) if pol else -1)