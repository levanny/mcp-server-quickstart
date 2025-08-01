import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

HOST = "127.0.0.1"
PORT = 8888

async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"[MCP] Connection from {addr}")

    while True:
        data = await reader.read(100)
        if not data:
            print(f"[MCP] Connection closed by {addr}")
            break
        message = data.decode().strip()
        print(f"Echo: {message}\n")

        response = f"Echo: {message}"
        writer.write(response.encode())
        await writer.drain()

    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client(), HOST, PORT)
    print(f"[MCP] Server running on {HOST}:{PORT}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())