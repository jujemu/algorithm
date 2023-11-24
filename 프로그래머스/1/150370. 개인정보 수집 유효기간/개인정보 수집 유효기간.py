def solution(today, terms, privacies):
    answer = []

    cur_y, cur_m, cur_d = map(int, today.split("."))
    term_d = {}
    for term in terms:
        term, length = term.split()
        term_d[term] = int(length)

    for idx, privacy in enumerate(privacies, start=1):
        init_term, term = privacy.split()
        y, m, d = map(int, init_term.split("."))

        length = term_d[term]
        m += length
        while m > 12:
            y += 1
            m -= 12

        if y < cur_y:
            answer.append(idx)
            continue

        if cur_y < y:
            continue

        if m < cur_m:
            answer.append(idx)
            continue

        if m > cur_m:
            continue
        
        if cur_d < d:
            continue
        answer.append(idx)

    return answer