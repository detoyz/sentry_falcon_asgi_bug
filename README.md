# Test case project for sentry_sdk 1.16 bug

## Setup

### Install project

1. Install poetry if not installed
2. Run `poetry install`
3. Run `poetry shell` to active virtual environment

### Reproduse the error

1. Run `falcon-inspect-app main:create_app`
2. See error `TypeError: _patch_prepare_middleware.<locals>.sentry_patched_prepare_middleware() takes from 0 to 2 positional arguments but 3 were given`

### Current workaround

1. Downgrade sentry by running `poetry add sentry-sdk@1.15.0`
2. Run `falcon-inspect-app main:create_app`
3. See expected output:

    ```shell
    Falcon App (ASGI)
    • Routes:
        ⇒ /health-check - HealthCheckController:
        └── GET - on_get
    ```
