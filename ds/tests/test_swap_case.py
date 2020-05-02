import pytest
from ds.ds.swap_case import convert_pybites_chars


@pytest.mark.parametrize('provided, expected', [
    ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do",
     "LorEm IPSum dolor SIT amET, conSEcTETur adIPIScIng ElIT, SEd do"),
    ("Vestibulum morbi blandit cursus risus at ultrices",
     "VESTIBulum morBI BlandIT curSuS rISuS aT ulTrIcES"),
    ("Aliquet nibh praesent tristique magna sit amet purus gravida quis",
     "AlIquET nIBh PraESEnT TrISTIquE magna SIT amET PuruS gravIda quIS"),
    ("Fames ac turpis egestas maecenas pharetra",
     "FamES ac TurPIS EgESTaS maEcEnaS PharETra"),
    ("Vitae purus faucibus ornare suspendisse sed nisi lacus",
     "VITaE PuruS faucIBuS ornarE SuSPEndISSE SEd nISI lacuS"),
    ("Pharetra massa massa ultricies mi quis",
     "pharETra maSSa maSSa ulTrIcIES mI quIS")
])
def test_check_case_conversion(provided, expected):
    assert convert_pybites_chars(provided) == expected
