import pytest
from kalorien_rechner import KalorienRechner


def test_kalorienbedarf_unter_30():
    rechner = KalorienRechner()

    ergebnis = rechner.berechne_kalorienbedarf(25)

    assert ergebnis == 2500


def test_kalorienbedarf_ab_30():
    rechner = KalorienRechner()

    ergebnis = rechner.berechne_kalorienbedarf(35)

    assert ergebnis == 2200


def test_exception_bei_ungueltigem_alter():
    rechner = KalorienRechner()

    with pytest.raises(ValueError):
        rechner.berechne_kalorienbedarf(0)