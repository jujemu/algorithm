def solution(numbers):
    result = []
    for number in numbers:
        b_n = bin(number)[2:]
        
        length = len(b_n)
        tree_length = find_tree_length(length)
        b_n = "0"*(tree_length-length) + b_n
        
        left, right = 0, tree_length-1
        root = b_n[(left+right)//2] != "1"
        if dfs(b_n, left, right, root):
            result.append(1)
        else:
            result.append(0)
    return result
        
        
def find_tree_length(length):
    k = 1
    while True:
        k *= 2
        if length <= k - 1:
            return k-1
        
          
def dfs(b_n, left, right, no_parent):
    if left == right:
        if no_parent:
            if b_n[left] == "0":
                return True
            else:
                return False
        else:
            return True
    
    mid = (left+right)//2
    if no_parent:
        if b_n[mid] == "1":
            return False
        return dfs(b_n, mid+1, right, True) and dfs(b_n, left, mid-1, True)
    else:
        if b_n[mid] == "0":
            no_parent = True
        return dfs(b_n, mid+1, right, no_parent) and dfs(b_n, left, mid-1, no_parent)
    