import pytest
from project import choose_villain, battle, check_level, final_boss_battle

def test_choose_villain():
    villains = ["Tomura Shigaraki", "Kurogiri", "Dabi", "Himiko Toga", "Stain"]
    villain = choose_villain()
    assert villain in villains

def test_battle():
    hero_name = "Izuku Midoriya"
    villain_name = "Test Villain"
    hero_level = 5
    battle_result, earned_xp = battle(hero_name, villain_name, hero_level)
    assert isinstance(battle_result, bool)
    assert isinstance(earned_xp, int)
    assert earned_xp >= 0

def test_check_level():
    hero_xp = 400
    level = check_level(hero_xp)
    assert isinstance(level, int)
    assert level == 5

def test_final_boss_battle():
    hero_name = "Izuku Midoriya"
    hero_level = 10
    final_boss_result = final_boss_battle(hero_name, hero_level)
    assert isinstance(final_boss_result, bool)
