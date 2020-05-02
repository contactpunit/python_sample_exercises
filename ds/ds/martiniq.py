def get_index_different_char(chars):
    alnum = []
    special = []

    for index, char in enumerate(chars):
        if str(char).isalnum():
            alnum.append(index)
        else:
            special.append(index)
    if len(alnum) == 1:
        return alnum[0]
    else:
        return special[0]

