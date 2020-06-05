import os
import grpc
import echo_pb2
import echo_pb2_grpc

echoService_addr = os.getenv("ECHO_SERVER","localhost:50051")

def invoke_echo(stub, input_msg):
    messages = []
    messages.append(echo_pb2.EchoRequest(msg=input_msg, log=True))
    responses = stub.echo(iter(messages))
#    responses = stub.EchoService(iter(messages))
    for response in responses:
        print('### Reply from EchoService: {}'.format(response.resp))

def run():
    with grpc.insecure_channel(echoService_addr) as channel:
        stub = echo_pb2_grpc.EchoServiceStub(channel)
        print('--- echoClient Start ---')
        while True:
            st = input("Type message to get echoed >> ")
            invoke_echo(stub, st)

if __name__ == '__main__':
    run()
