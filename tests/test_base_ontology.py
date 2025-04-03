import base_ontology


def test_import() -> None:
    """Test that the package can be imported without errors."""
    assert isinstance(base_ontology.__name__, str)
