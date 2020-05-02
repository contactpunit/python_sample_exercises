import re

INDENTS = 4

poem = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
"""


def print_hanging_indents(poem):
    paras = poem.split('\n\n')
    clean_paras = [entry.strip() for entry in paras]
    required_paras = [re.sub("\n\s+", f"\n{INDENTS * ' '}", entry) for entry in clean_paras]
    print('\n'.join(required_paras))
    # for lines in clean_paras:
    #     for line in lines.split('\n'):
    #         print(re.sub("^\s+", "\t", line))



