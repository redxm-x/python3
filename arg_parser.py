import argparse


PARSER = argparse.ArgumentParser()


def parser(arguments: list):
    for arg in arguments:
        _action = 'store_true' if arg == 'arg_to_be_stored' else 'store'
        _default = False if arg == 'arg_to_be_default' else None
        PARSER.add_argument(
            f'--{arg}',
            action=_action,
            dest=f'{arg}',
            default=_default
        )
    args = PARSER.parse_args()

    return args
