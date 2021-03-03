def mapper(fnc):
    def inner(list_of_values):
        if type(list_of_values) == str: return list_of_values
        if type(list_of_values) == list: return [fnc(value) for value in list_of_values]
    return inner
@mapper # decorator
def camelcase(s):
    '''Rurn strings_like_this into StringsLikeThis'''
    return ''.join([word .capitalize() for word in s.split('_')])

print(camelcase('some_string'))

names = [
    'abc_def',
    'ghi_ghi'
]

print(camelcase(names))
