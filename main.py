from aiohttp import web
from apis import get_state, settings, wraper
import asyncio

def create_app(loop) -> web.Application:
    app = web.Application(loop=loop)
    app.add_routes([web.get('/', index_handle),
                    web.static('/static', 'public/'),
                    web.get('/info', info_handle),
                    web.post('/settings', settings_handle),
                    web.post('/auth', login)])
    return app


def init_loop():
    loop = asyncio.get_event_loop()
    # thread = asyncio.(wraper)
    loop.create_task(wraper())
    return loop


async def index_handle(request: web.Request):
    return web.FileResponse('public/login.html')


async def login(request: web.Request):
    data = await request.json()
    print(data)

    return web.Response(text='oki')


async def info_handle(request: web.Request):
    response = get_state()
    return web.json_response(response)


async def settings_handle(request: web.Request):
    data = await request.json()
    settings.set_items(**data)
    return web.json_response({'one': 1})


if __name__ == '__main__':
    loop = init_loop()
    app = create_app(loop)
    web.run_app(app)


















