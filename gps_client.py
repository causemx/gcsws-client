import gpsd
import client
import asyncio


gpsd.connect()
packet = gpsd.get_current()
print(packet.position())

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(client.serve_client('ws://x.x.x.x/xxx'), packet, 1)


