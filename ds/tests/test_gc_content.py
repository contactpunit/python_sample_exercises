import pytest
from ds.ds.gc_content import calculate_gc_content

str1 = (
    "tagtgaaagatattcatttcgaaggccttcagcgtgtcgccgttggtgcggccctcctca"
    "gtatgccggtgcgcacaggcgacacggttaatgatgaagatatcagtaataccattcgcg"
    "ctctgtttgctaccggcaactttgaggatgttcgcgtccttcgtgatggtgatacccttc"
    "tggttcaggtaaaagaacgtccgaccattgccagcattactttctccggtaacaaatcgg"
    "tgaaagatgacatgctgaagcaaaacctcgaggcttctggtgtgcgtgtgggcgaatccc"
    "tcgatcgcaccaccattgccgatatcgagaaaggtctggaagacttctactacagcgtcg"
    "gtaaatatagcgccagcgtaaaagctgtcgtgaccccgctgccgcgcaaccgtgttgacc"
    "taaaactggtgttccaggaaggtgtgtcagctgaaatccagcaaattaacattgttggta"
    "accatgctttcaccaccgacgaactgatctctcatttccaactgcgtgacgaagtgccgt"
    "ggtggaacgtggtaggcgatcgtaaataccagaaacagaaactggcgggcgaccttgaaa"
    "ccctgcgcagctactatctggatcgcggttatgcccgtttcaacatcgactctacccagg"
    "tcagtctgacgccagataaaaaaggtatttacgtcacggtgaacatcaccgaaggcgatc"
    "agtacaagctttctggcgttgaagtgagcggcaaccttgccgggcactccgctgaaattg"
    "agcagctgactaagatcgagccgggtgagctgtataacggcaccaaagtgaccaagatgg"
    "aagatgacatcaaaaagcttctcggtcgctatggttatgcctatccgcgcgtacagtcga"
    "tgcccgaaattaacgatgccgacaaaaccgttaaattacgtgtgaacgttgatgcgggta"
    "accgtttctacgtgcgtaagatccgttttgaaggtaacgatacctcgaaagatgccgtcc"
    "tgcgtcgcgaaatgcgtcagatggaaggtgcatggctggggagcgatctggtcgatcagg"
    "gtaaggagcgtctgaatcgtctgggcttctttgaaactgtcgataccgatacccaacgtg"
    "ttccgggtagcccggaccaggttgatgtcgtctacaaggtaaaagagcgcaacaccggta"
    "gcttcaactttggtattggttacggtactgaaagtggcgtgagcttccaggctggtgtgc"
)


@pytest.mark.parametrize('param, expected', [
    (str1, 51.35)
])
def test_check_gc_score(param, expected):
    assert calculate_gc_content(param) == expected
