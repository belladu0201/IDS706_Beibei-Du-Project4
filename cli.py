import click
import statistics
from mylib.runhealth import health_generator


@click.command()
@click.option("--health", help="Health status to add")
def statushealth(df):
    """Pass in additional fruit"""

    chosen_random_ten = health_generator(df)
    for i in chosen_random_ten:
        click.echo(
            click.style(
                f"Your choice was randomly selected: {statistics.mode(set(i))}", fg="red", bold=True
            )
        )


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    statushealth()
