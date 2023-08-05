from jar import Jar


def test_init():
    jar = Jar(6)
    assert jar.capacity == 6
    assert jar.size == 0
    jar_2nd = Jar()
    assert jar_2nd.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6
    jar.deposit(4)
    assert jar.size == 10
    jar.deposit(2)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(3)
    assert jar.size == 9
    jar.withdraw(5)
    assert jar.size == 4
    jar.withdraw(2)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0
