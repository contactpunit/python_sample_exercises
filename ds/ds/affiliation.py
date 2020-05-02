def generate_affiliation_link(url):
    parts = url.rsplit('dp/')
    required = parts[-1].split('/')
    return f'http://www.amazon.com/dp/{required[0]}/?tag=pyb0f-20'

print(generate_affiliation_link('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/?keywords=war+of+art'))