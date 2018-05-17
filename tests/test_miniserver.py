import pytest
import nina


def test_project_defines_author_and_version():
    assert hasattr(nina, '__author__')
    assert hasattr(nina, '__version__')
