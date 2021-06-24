"""
ci processing
"""

import argparse
import logging
from pathlib import Path

from hyp3_ci import __version__

log = logging.getLogger(__name__)


def proc_ci(greeting: str = 'Hello world!') -> Path:
    """Create a greeting product

    Args:
        greeting: Write this greeting to a product file (Default: "Hello world!" )
    """
    log.debug(f'Greeting: {greeting}')
    product_file = Path('greeting.txt')
    product_file.write_text(greeting)
    return product_file


def main():
    """proc_ci entrypoint"""
    parser = argparse.ArgumentParser(
        prog='proc_ci',
        description=__doc__,
    )
    parser.add_argument('--greeting', default='Hello world!',
                        help='Write this greeting to a product file')
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    args = parser.parse_args()

    proc_ci(**args.__dict__)


if __name__ == "__main__":
    main()
