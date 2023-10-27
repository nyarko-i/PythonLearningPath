from random import choice

capital = "Kumasi"
bird = "Dove"
flower = "RoseFlowe"
song = "Brighter Days by Sarkodie "


def randomfunfact():
    funfacts = [
        "Kumasi is considered the most beautiful City in the Ashanti Region",
        "Dove is the most cleaned bird amongst all other birds",
        "One of the most used flower for proposals  is the roseflower",
        "Brighter days is the most listened song as of october 2023"
    ]

    index = choice("1023")
    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
