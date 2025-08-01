import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

HOST = ("127.0.0.1")
PORT = 8888

async def main():
    reader, writer = await asyncio.open_connection(HOST, PORT)

    message = "Hello MCP Server!"
    print(f"Sending: {message}")
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"[Client] Recieved: {data.decode().strip()}")

    print("[Client] Closing Connection")
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())