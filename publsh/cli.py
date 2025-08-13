#!/usr/bin/env python3
import click

# Extend click.Group class so that the base command invokes if no subcommand is entered.
class DefaultGroup(click.Group):
    def __init__(self, *args, **kwargs):
        self.default_cmd_name = kwargs.pop("default_cmd_name", None)
        super().__init__(*args, **kwargs)

    def parse_args(self, ctx, args):
        if not args and self.default_cmd_name:
            args.insert(0, self.default_cmd_name)
        super().parse_args(ctx, args)

@click.group(cls=DefaultGroup, default_cmd_name="post")
def cli():
    """Test."""
    pass

@cli.command()
def post():
    """Post an entry on the publsh site."""
    click.echo("Open Editor")
    click.echo("New post added!")

@cli.command()
@click.argument('id')
def edit(id):
    """Edit an existing post with its number."""
    click.echo(f"Editing post #{id}")

if __name__ == '__main__':
    cli()

