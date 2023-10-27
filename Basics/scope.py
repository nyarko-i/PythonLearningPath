

name = "King"


# def greeting(name):
#     color = "Blue"
#     print(color)
#     print(name)


# greeting("King")
count = 1


def another():
    color = 'Blue'
    global count
    count += 1
    print(count)

    def greeting(name):
        color = "Blue"
        print(color)
        print(name)

    greeting("King")


another()
