
def mutable_tuples():
    t1 = (1,2,[30,40])
    t2 = (1,2,[30,40])

    print("This will show true as the tuples are equal with id attributes: ", t1 == t2)
    t1[2].append(99)

    print("This will show false as the tuples are NOT equal after the mutable item in the list is changed: ", t1 == t2)

if __name__ == "__main__":
    mutable_tuples()

