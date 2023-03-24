import asyncio
import websockets
import extensions

async def serve_client(uri, data, time_span):
    async with websockets.connect(uri) as websocket:
        for _ in range(10):
            # await websocket.send(",".join(str(pt) for pt in extensions.PTLATLNG))
            # print(f"(client) send to server: {dummy.PTLATLNG}")
            await websocket.send(data)
            _recv = await websocket.recv()
            print(f"(client) recv from server {_recv}")
            await asyncio.sleep(time_span)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(serve_client('ws://192.168.50.109:5566/Echo'))

# asyncio.get_event_loop().run_until_complete(
#     foo('ws://192.168.50.109:5566/Echo'))

