def middle_permutation(string):
    from itertools import permutations
    answer_list = list(permutations(string))
    if len(answer_list)%2 == 0:
        target_pos = (len(answer_list)/2) -1
    else:
        target_pos = (len(answer_list) -1 / 2)
    answer_list.sort()
    answer_set = answer_list[int(target_pos)]
    answer = ''.join(answer_set)
    return answer
