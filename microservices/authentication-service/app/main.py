import asyncio
import logging

import grpc

import pb.auth_pb2_grpc as auth_pb_grpc
from core.logger import configure_logging
from services import AuthServicer

logger = logging.getLogger(__name__)


async def serve() -> None:
    server = grpc.aio.server()
    auth_pb_grpc.add_AuthServiceServicer_to_server(AuthServicer(), server)
    listen_addr = "[::]:50052"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    configure_logging()
    asyncio.run(serve())
