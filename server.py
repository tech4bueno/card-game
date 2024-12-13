from aiohttp import web

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        await ws.send_str(f"Echo: {msg.data}")

    return ws

async def index_handler(request):
    return web.FileResponse('index.html')

app = web.Application()
app.router.add_get('/', index_handler)
app.router.add_get('/ws', websocket_handler)
web.run_app(app, port=10000)
