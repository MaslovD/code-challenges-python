def solution(a):
    tmp_dict = {}

    for idx, num in enumerate(a):
        if num in tmp_dict.keys():
            del tmp_dict[num]
        else:
            tmp_dict[num] = 1

    # print(tmp_dict)
    if len(tmp_dict) > 0:
        return next(iter(tmp_dict))
    else:
        return None


if __name__ == '__main__':
    print(solution_v2([0, 2, 1, 0, 2, 1, 7]))
