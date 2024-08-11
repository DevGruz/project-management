import asyncio
import logging

import grpc

import pb.user_pb2_grpc as user_pb2_grpc
from core.logger import configure_logging
from services import UserServicer

logger = logging.getLogger(__name__)


async def serve() -> None:
    server = grpc.aio.server()
    user_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    configure_logging()
    asyncio.run(serve())
