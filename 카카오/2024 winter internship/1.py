def solution(friends, gifts):
    give_whom = {name: [0]*len(friends) for name in friends}
    get_give = {name: [0, 0] for name in friends}
    friend_index = {name: idx for idx, name in enumerate(friends)}

    for gift in gifts:
        giver, getter = gift.split()
        
        give_whom[giver][friend_index[getter]] += 1
        get_give[giver][1] += 1
        get_give[getter][0] += 1

    result = [0] * len(friends)
    for cur in friends:
        for friend in friends:
            if cur == friend:
                continue

            f_idx = friend_index[friend]
            c_idx = friend_index[cur]

            cur_number = give_whom[cur][f_idx]
            friend_number = give_whom[friend][c_idx]

            if cur_number > friend_number:
                result[c_idx] += 1
            else:
                c_score = get_gift_score(cur, get_give)
                f_score = get_gift_score(friend, get_give)

                if c_score > f_score:
                    result[c_idx] += 1
    
    return max(result)


def get_gift_score(name, get_give):
    return get_give[name][1] - get_give[name][0]
