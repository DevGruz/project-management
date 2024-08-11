PROTO_DIR=../protos
APP_DIR=app

all: user

user:
	python -m grpc_tools.protoc -Iapp/pb=$(PROTO_DIR) --python_out=. --grpc_python_out=. $(PROTO_DIR)/user.proto
	python -m grpc_tools.protoc -Iapp/pb=$(PROTO_DIR) --python_out=. --grpc_python_out=. $(PROTO_DIR)/auth.proto