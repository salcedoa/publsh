#!/usr/bin/env python3
import click
from .controller import create_post, delete_post, get_post_data, edit_post

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
    content = click.edit(editor="vim")  # or omit editor= to just use $EDITOR
    
    if content is None:
        click.echo("No content entered. Post aborted.")
        return
    content = content.strip()
    return create_post(content.splitlines())

@cli.command()
@click.argument('post_id')
def edit(post_id):
    """Edit an existing post with its id"""
    original_text = get_post_data(post_id)
    if original_text:
        click.echo(f"Editing post #{post_id}")
        edited_text = click.edit(original_text, editor="vim")
        if edited_text is None:
            click.echo(f"All text deleted so deleting post")
            delete(post_id)
            return
    
    lines = edited_text.strip().splitlines()
    edit_post(post_id, lines)


@cli.command()
@click.argument('post_id', type=int)
def delete(post_id):
    """Delete post with given ID"""
    result = delete_post(post_id)
    click.echo(result)

if __name__ == '__main__':
    cli()

