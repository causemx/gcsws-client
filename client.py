import asyncio
import websockets
import dummy

async def foo(uri):
    async with websockets.connect(uri) as websocket:
        for _ in range(10):
            await websocket.send(",".join(str(pt) for pt in dummy.PTLATLNG))
            # print(f"(client) send to server: {dummy.PTLATLNG}")
            _recv = await websocket.recv()
            print(f"(client) recv from server {_recv}")
            await asyncio.sleep(1)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(foo('ws://192.168.50.109:5566/Echo'))

# asyncio.get_event_loop().run_until_complete(
#     foo('ws://192.168.50.109:5566/Echo'))

