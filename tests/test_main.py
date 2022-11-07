from ..package.main import Solution
def test_string():

    assert Solution.upperNextToLower("ahjJa") == [2,3]
    assert Solution.upperNextToLower("aasdDknpqn") == [3,4]
    assert Solution.upperNextToLower("aAsdDknpqn") == [0,1]
    assert Solution.upperNextToLower("aasdkKJnpqn") == [4,5]
    assert Solution.upperNextToLower("aasdaknpqnN") == [9,10]
    assert Solution.upperNextToLower("apsS") == [2,3]
    assert Solution.upperNextToLower("AasdDknpqn") == [0,1]

    assert Solution.upperNextToLower("aasdgknpqn") == None
    assert Solution.upperNextToLower("") == None
    assert Solution.upperNextToLower("E") == None








