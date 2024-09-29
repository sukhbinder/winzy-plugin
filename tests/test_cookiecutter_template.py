from cookiecutter.main import cookiecutter
import pathlib

TEMPLATE_DIRECTORY = str(pathlib.Path(__file__).parent.parent)


def test_generated_files(tmpdir):
    generate(
        tmpdir,
        {
            "plugin_name": "winzy-foo",
            "description": "blah",
        },
    )
    assert paths(tmpdir) == {'winzy-foo\\.github', 'winzy-foo\\.github\\workflows\\test.yml', 'winzy-foo', 'winzy-foo\\LICENSE', 'winzy-foo\\README.md', 'winzy-foo\\tests', 'winzy-foo\\winzy_foo', 'winzy-foo\\.github\\workflows\\publish.yml', 'winzy-foo\\.github\\workflows', 'winzy-foo\\tests\\test_winzy_foo.py', 'winzy-foo\\winzy_foo\\__init__.py', 'winzy-foo\\pyproject.toml', 'winzy-foo\\.gitignore'}

def generate(directory, context):
    cookiecutter(
        template=TEMPLATE_DIRECTORY,
        output_dir=str(directory),
        no_input=True,
        extra_context=context,
    )


def paths(directory):
    paths = list(pathlib.Path(directory).glob("**/*"))
    paths = [r.relative_to(directory) for r in paths]
    return {str(f) for f in paths if str(f) != "."}
