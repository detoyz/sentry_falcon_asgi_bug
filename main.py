import falcon.asgi

from sentry_sdk import init


init()  # by commenting this line or downgrading to sentry-sdk@1.15 -> all works


def create_app():
    app = falcon.asgi.App()
    app.add_route("/health-check", HealthCheckController())
    return app


class HealthCheckController:
    async def on_get(self, req, resp):
        resp.media = {"status": "OK"}
