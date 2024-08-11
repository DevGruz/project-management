PROTO_DIR=../protos
APP_DIR=app

all: user

user:
	python -m grpc_tools.protoc -Ipb=$(PROTO_DIR) --python_out=$(APP_DIR) --grpc_python_out=$(APP_DIR) $(PROTO_DIR)/auth.proto
	python -m grpc_tools.protoc -Ipb=$(PROTO_DIR) --python_out=$(APP_DIR) --grpc_python_out=$(APP_DIR) $(PROTO_DIR)/user.proto