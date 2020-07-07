"""Lambda function that executes isort, a static file linter."""
from lintipy import CheckRun


handle = CheckRun.as_handler(
    'isort',
    'isort', '--check-only', '--diff', '.'
)
