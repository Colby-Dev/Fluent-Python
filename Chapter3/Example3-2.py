## Example 3 - 2

def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api':2, 'authors':[*names]}:
            return names
        case {'type':'book', 'api':1, 'author':name}:
            return name
        case {'type':'book'}:
            return ValueError(f"Invaild 'book' record: {record!r}")

author_dict = {'type':'book', 'api':2, 'authors': ['John P', 'John H']}
single_author = {'type':'book', 'api':1, 'author':'Rigby'}



if __name__ == '__main__':

    print(get_creators(author_dict))
    print(get_creators(single_author))
