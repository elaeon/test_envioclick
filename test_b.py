
def move(position, move_x, unit):
    if move_x is True:
        position[0] = position[0] + unit
    else:
        position[1] = position[1] + unit
    return position


def position2str(position):
    return "".join(map(str, position))


def doesCircleExist(commands):
    anwsers = []
    for command in commands:
        if len(command) == 1 and command == "L" or command == "R":
            command = "G" + command
        position = [0, 0]
        move_x = False
        unit = 1
        visited = set([position2str(position)])
        for run in command*4:  # multiply by 4 to check cycles
            if run == 'G':
                position = move(position, move_x, unit)
                key = position2str(position)
                if key in visited:
                    anwsers.append("YES")
                    break
                else:
                    visited.add(key)
            elif run == 'L' and move_x is False:
                move_x = True
                unit = -1 * unit
            elif run == 'L' and move_x is True:
                move_x = False
                unit = 1 * unit
            elif run == 'R' and move_x is False:
                move_x = True
                unit = 1 * unit
            elif run == 'R' and move_x is True:
                move_x = False
                unit = -1 * unit
        else:
            anwsers.append("NO")
    return anwsers
            


def test_case0():
    commands = ["GRGL"]
    assert doesCircleExist(commands) == ["NO"]


def test_case1():
    commands = ["GRGLGLGR"]
    assert doesCircleExist(commands) == ["NO"]


def test_case2():
    commands = ["GRGLGLGRGRGL"]
    assert doesCircleExist(commands) == ["NO"]


def test_case3():
    commands = ["GRGLGLGL"]
    assert doesCircleExist(commands) == ["YES"]


def test_case4():
    commands = ["GRGLGR"]
    assert doesCircleExist(commands) == ["YES"]


def test_case5():
    commands = ["GLGLGL"]
    assert doesCircleExist(commands) == ["YES"]


def test_case6():
    commands = ["GRGLGRGR"]
    assert doesCircleExist(commands) == ["YES"]


def test_case7():
    commands = ["GRGLGRGLGLGR"]
    assert doesCircleExist(commands) == ["NO"]


def test_caseA():
    commands = ["G", "L", "R"]
    assert doesCircleExist(commands) == ["NO", "YES", "YES"]


def get_name_fn(fn):
    def view(*args):
        fn(*args)
        return fn.__name__
    return view()


if __name__ == '__main__':
    test_cases = [test_caseA, test_case0, test_case1, test_case2, test_case3,
                  test_case4, test_case5, test_case6, test_case7]

    for test_case in test_cases:
        print(get_name_fn(test_case), "OK")
