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

result = get_checksum()
print 'the checksum is ', result