def swap_case(s):
    bucket = []
    for item in s:
        if item.isalpha():
            if item.isupper():
                bucket.append(item.lower())
            else:
                bucket.append(item.upper())            
        else:
            bucket.append(item)
    return ''.join(bucket)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
