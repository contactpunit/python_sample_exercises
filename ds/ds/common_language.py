def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    languages = [set(language) for language in programmers.values()]
    return set.intersection(*languages)
