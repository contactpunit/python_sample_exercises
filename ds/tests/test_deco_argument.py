import pytest
from ds.ds.deco_argument import make_html


def test_check_working_deco():
    @make_html('bold')
    def html1(text='sample1'):
        return text

    assert html1() == '<bold>sample1</bold>'

    @make_html('para')
    def html2(text='sample1'):
        return text

    assert html2(text='this is new one') == '<para>this is new one</para>'
