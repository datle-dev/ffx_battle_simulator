import battle

def test_calc_damage_str_vs_def() -> None:
    assert battle.calc_damage_str_vs_def(15, 1) == 134

def test_calc_accuracy_party_high_accuracy() -> None:
    assert battle.calc_accuracy_party(10, 5) == 100

def test_calc_accuracy_party_low_accuracy() -> None:
    assert battle.calc_accuracy_party(10, 15) == 25

def test_calc_accuracy_monster() -> None:
    assert battle.calc_accuracy_monster(90, 10) == 80

def test_calc_hit_chance() -> None:
    assert battle.calc_hit_chance(10, 5, 5) == 10

def test_is_hit_100_pct_chance() -> None:
    assert battle.is_hit(100) == True

def test_is_hit_0_pct_chance() -> None:
    assert battle.is_hit(0) == False