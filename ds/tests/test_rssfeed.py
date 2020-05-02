from ds.ds.rssfeed import get_games, Game
import pytest


@pytest.fixture()
def run_get_games():
    return get_games()


@pytest.mark.parametrize('expected_value', [
    Game(title='Now Available on Steam Early Access - X Rebirth VR Edition',
         link='http://store.steampowered.com/news/31132/'),
    Game(title='Now Available on Steam - Nidhogg 2, 10% off!',
         link='http://store.steampowered.com/news/31694/')
])
def test_check_games_namedtuple(expected_value, run_get_games):
    assert expected_value in run_get_games


def test_check_total_results(run_get_games):
    assert run_get_games[0].title == 'Midweek Madness - RiME, 33% Off'
