import pytest
import {{ cookiecutter.underscored }} as w


def test_plugin(capsys):
    w.{{cookiecutter.entry_name}}_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``winzy`` plugin." in captured.out
