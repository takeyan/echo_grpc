import os
import json
import time
from datetime import datetime
from concurrent import futures
import grpc
import echo_pb2
import echo_pb2_grpc
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


def k8s_env():
    json_dict = {
        'podname' :  os.getenv('K8S_POD_NAME','null'),
        'pod_ip' :      os.getenv('K8S_POD_IP','null'),
        'nodename' : os.getenv('K8S_NODE_NAME','null')
    }
    return json_dict


class EchoServiceServicer(echo_pb2_grpc.EchoServiceServicer):

    def __init__(self):
        pass

    def echo(self, request_iterator, context):
        for request_msg in request_iterator:
            reply_msgs = []
            
            st = json.dumps(k8s_env())
            st2 = datetime.now().isoformat()
            reply_msgs.append(echo_pb2.EchoReply(resp='### input message={}'.format(request_msg.msg)))
            reply_msgs.append(echo_pb2.EchoReply(resp='### environment={}'.format(st)))
            reply_msgs.append(echo_pb2.EchoReply(resp='### timestamp={}'.format(st2)))

            if (request_msg.log):
              logger.debug('### EchoServiceServer -- input:{}, env:{}, time:{}'.format(request_msg.msg, st, st2))

            for message in reply_msgs:
                yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    echo_pb2_grpc.add_EchoServiceServicer_to_server(EchoServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.debug('### EchoServiceServer -- Starting ...')
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
