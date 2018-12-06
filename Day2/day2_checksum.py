from collections import defaultdict
def get_checksum():
    def get_2_3s(line):
        count_2s = 0
        count_3s = 0
        char_ct = defaultdict(int)
        for c in line:
            if c != '\n':
                char_ct[c] += 1
                if char_ct[c] == 2:
                    count_2s += 1
                elif char_ct[c] == 3:
                    count_3s += 1
                    count_2s -= 1
                elif char_ct[c] == 4:
                    count_3s -= 1
        return count_2s, count_3s

    line_2s = 0
    line_3s = 0
    with open("input.txt") as file:
        for line in file:
            ct_2s, ct_3s = get_2_3s(line)
            if ct_2s:
                line_2s += 1
            if ct_3s:
                line_3s +=1
    return line_2s * line_3s


def get_one_diff():
    with open("input.txt", "r") as file:
        differences = None

        for line in file:
            line = line.strip()
            max_ln = len(line)
            print max_ln
            if not differences:
                differences = [defaultdict(list)] * max_ln

            for i in range(max_ln):
                if i == 0:
                    remove_i = line[1:]
                elif i == max_ln - 1:
                    remove_i = line[:-1]
                else:
                    remove_i = line[:i] + line[i+1:]

                print remove_i, 'at', i
                def_dict_i = differences[i]
                if remove_i in def_dict_i:
                    return remove_i, def_dict_i
                else:
                    differences[i][remove_i].append(line)
        return ""


result = get_one_diff()
print 'the one diff is ', result