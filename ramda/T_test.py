from ramda.T import T


def T_test():
    assert T(1, 2, 3, 4), "Should be True"
    assert T(False), "Should be True"
    assert T(True), "Should be True"
    assert T({}), "Should be True"
