#!/usr/bin/python3
# -*- coding: utf-8 -*-

from aiohttp import web
import json


def _get_credentials(request):
    try:
        user = request.headers["User"]
        pwd = request.headers["Pass"]

        return user == "Dewitt" and pwd == "12345"
    except KeyError as kerr:
        return False


def _make_fail_response(status: int, reason: str) -> {}:
    return {"status": status, "reason": reason}


def auth_error():
    response = _make_fail_response(401, "Authentication Fail")

    return web.Response(text=json.dumps(response), status=response["status"])


routes = web.RouteTableDef()


@routes.get("/", name="API_Index")
async def index(request):
    if _get_credentials(request):
        resources = {name: str(resource.url_for()) for name, resource in api.router.named_resources().items()}

        response = {"status": 200, "resources": resources}

        return web.Response(text=json.dumps(response), status=200)
    else:
        return auth_error()


@routes.post("/user", name="User_login")
async def user_login(request):
    if _get_credentials(request):
        try:
            j_dict = await request.json()

            user = j_dict["name"]
            pwd = j_dict["pwd"]

            print(f"Creating new user {user} with password {pwd}...")
            response = {"status": 200}
        except Exception as ex:
            response = {"status": 500, "reason": str(ex)}

        return web.Response(text=json.dumps(response), status=response["status"])
    else:
        return auth_error()

api = web.Application()
api.add_routes(routes)

web.run_app(api)
