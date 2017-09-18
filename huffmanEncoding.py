__author__ = 'yiqingxu'

from collections import defaultdict


def find2minIndices(weights):
    if weights[weights.keys()[0]] <= weights[weights.keys()[1]]:
        index1, index2 = weights.keys()[0], weights.keys()[1]
    else:
        index1, index2 = weights.keys()[1], weights.keys()[0]

    for i in weights.keys()[2:]:
        if weights[i] < weights[index2]:
            if weights[i] < weights[index1]:
                index2 = index1
                index1 = i
            else:
                index2 = i
    return index1, index2


def huffmanAlgo(weights):
    count = len(weights)
    if count < 3:
        return [1, 1]

    dict_index_depths = defaultdict(int)

    while count > 2:
        index_min_1, index_min_2 = find2minIndices(weights)

        updated = weights[index_min_1] + weights[index_min_2]
        del weights[index_min_1], weights[index_min_2]
        temp = list(index_min_1)
        temp.extend(index_min_2)
        index_min_1 = tuple(temp)
        weights[index_min_1] = updated

        for item in index_min_1:
            dict_index_depths[item] += 1
        count -= 1
    maxlength = max(dict_index_depths.values()) + 1
    minlength = min(dict_index_depths.values()) + 1
    return maxlength, minlength


def main():
    with open('/Users/yiqingxu/Google Drive/Algorithm1_Stanford/input_random_30_1000.txt') as f:
        count = int(f.readline().strip('\n'))
        inputs = f.readlines()
        inputs = [int(w.strip('\n')) for w in inputs]
        weights = {(x,): inputs[x] for x in xrange(count)}
        if count > 0:
            maxlength, minlength = huffmanAlgo(weights)
            print 'Maximum Length: {}'.format(maxlength)
            print 'Minimum Length: {}'.format(minlength)

if __name__ == '__main__':
    main()