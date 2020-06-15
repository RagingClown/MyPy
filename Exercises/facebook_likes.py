# initial version
def likes(names):
    if len(names) == 0:
        message = "no one likes this"
    elif len(names) == 1:
        message = names[0] + " likes this"
    elif len(names) == 2:
        message = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        message = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        message = f'{names[0]}, {names[1]} and {len(names) - 2} others like this'
    return message

# Dictionary version


def likes_d(names):
    phrases = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} like this"

    }
    length = len(names)

    return phrases[min(4, length)].format(*names, others=length - 2)

