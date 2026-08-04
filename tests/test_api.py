from httk.core.report import collect_reports

from httk.placeholder import atomic_number


def test_known_symbol() -> None:
    assert atomic_number("He") == 2


def test_unknown_symbol_is_reported() -> None:
    with collect_reports() as collection:
        assert atomic_number("Xx") is None

    assert len(collection.records) == 1
    assert collection.records[0].getMessage() == "unknown element symbol 'Xx'"


def test_dataset_loader_is_cached() -> None:
    from httk.placeholder.data import _example_dataset

    assert _example_dataset() is _example_dataset()
