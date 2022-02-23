from HashLinear import HashLinear

def main():
    hash = HashLinear(4, 5)
    print(hash.h_level(31, 0))

    hash.insert(4,4)
    hash.insert(8,8)
    hash.insert(12,12)
    hash.insert(16,16)
    hash.insert(20,20)
    hash.insert(24,24)
    hash.insert(6,6)
    hash.insert(5,5)
    hash.insert(10,10)
    hash.insert(17,17)
    hash.insert(27,27)
    hash.print_hash()



if __name__ == '__main__':
    main()




