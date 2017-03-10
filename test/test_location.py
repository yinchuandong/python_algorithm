import sys
import os


def main():
    lists = []
    with open('location.txt', 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            obj = line.split('|')
            obj.append('0')
            parent_id = int(obj[3])
            lists.append(obj)
            if parent_id != 0:
                lists[parent_id - 1][-1] = '1'
                # print lists[parent_id - 1]
        print len(lists)
    
    with open('location-new.txt', 'w') as f:
        for line in lists:
            f.write('|'.join(line) + '\n')
    return


if __name__ == '__main__':
    main()
