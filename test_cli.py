from click.testing import CliRunner
from cli import statushealth


def test_statushealth():
    """Testing cli for click"""


runner = CliRunner()
result = runner.invoke(statushealth)
assert result.exit_code == 0
assert 1.0 or 2.0 or 3.0 in result.output