def test_dict():
    dict = {'a': 1, 'b': 2}
    print("Тестування функцій словників:")
    dict.update({'c': 3})
    print("update({'c': 3}):", dict)
    del dict['a']
    print("del['a']:", dict)
    keys = dict.keys()
    print("keys():", list(keys))
    values = dict.values()
    print("values():", list(values))
    items = dict.items()
    print("items():", list(items))
    dict.clear()
    print("clear():", dict)
test_dict()