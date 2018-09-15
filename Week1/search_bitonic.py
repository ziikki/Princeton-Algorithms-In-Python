import argparse

def is_in(arr, n, verbose=False):
    l = len(arr)
    
    # base cases: if array has length 0
    if l == 0:
        if verbose: print('False at []')
        return False
    if l == 1:
        if verbose: print('{1} at {0}'.format(arr,arr[0] == n))
        return arr[0] == n
    if n < arr[0] and n < arr[-1]:
        if verbose: print('False {} under min'.format(arr))
        return False
    

    c = l // 2
    val = arr[c]
    if verbose: print(arr, c)
    # value found
    if val == n:
        if verbose: print('True at {}'.format(arr))
        return True
    # boundary 1 3 2
    elif (val >= arr[0] and val >= arr[-1]):
        return is_in(arr[:c], n, verbose) or is_in(arr[c:], n, verbose)
    # asc 1 2 3
    elif (val >= arr[0] and val <= arr[-1]):
        if val > n:
            return is_in(arr[:c], n, verbose)
        else:
            return is_in(arr[c:], n, verbose)
    # desc 3 2 1
    elif (val <= arr[0] and val >= arr[-1]):
        if val < n:
            return is_in(arr[:c], n, verbose)
        else:
            return is_in(arr[c:], n, verbose)

def test_bitonic(arr, n, verbose=False):
    print(n, arr)
    print(is_in(arr, n, verbose))

if __name__ == '__main__':
    # helps add --verbose option to program
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    args = parser.parse_args()

    test_cases = [([1,3,5,7,9,11,13,8,6,4,0], 5),
             ([1,3,5,7,9,11,13,8,6,4,0], 13),
             ([3,5,7,9,11,13,8,6,4], 1),
             ([1,3,5,7,9,11,13,8,6,4,0], 2),
             ([7, 10, 18, 19, 20, 40 ,12], 9), # 1 -  3 2
             ([7, 10, 18, 19, 20, 40 ,12], 17), # 1  - 3 2
             ([7, 10, 18, 19, 20, 40 ,12], 21)] # 1 3 - 2
    for arr, n in test_cases:
        test_bitonic(arr, n, args.verbose)
        print('--------------------------------------')
