from HashLinear import HashLinear

def main():
    hash = HashLinear(4, 4)
    print(hash.h_level(31, 0))

    hash.insert(32, 32)
    hash.insert(44,44)
    hash.insert(36,36)
    hash.insert(9,9)
    hash.insert(25,25)
    hash.insert(5,5)
    hash.insert(14,14)
    hash.insert(18,18)
    hash.insert(10,10)
    hash.insert(30,30)
    hash.insert(31,31) 
    hash.insert(35,35) 
    hash.insert(7, 7) 
    hash.insert(11,11) 
    hash.insert(43,43) 
    hash.insert(37,37) 
    hash.insert(29,29) 
    hash.insert(22,22)
    hash.print_hash()



if __name__ == '__main__':
    main()




