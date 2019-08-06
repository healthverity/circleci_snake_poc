# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from snakeskin.protos.orderer import cluster_pb2 as snakeskin_dot_protos_dot_orderer_dot_cluster__pb2


class ClusterStub(object):
  """Cluster defines communication between cluster members.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Submit = channel.stream_stream(
        '/orderer.Cluster/Submit',
        request_serializer=snakeskin_dot_protos_dot_orderer_dot_cluster__pb2.SubmitRequest.SerializeToString,
        response_deserializer=snakeskin_dot_protos_dot_orderer_dot_cluster__pb2.SubmitResponse.FromString,
        )
    self.Step = channel.unary_unary(
        '/orderer.Cluster/Step',
        request_serializer=snakeskin_dot_protos_dot_orderer_dot_cluster__pb2.StepRequest.SerializeToString,
        response_deserializer=snakeskin_dot_protos_dot_orderer_dot_cluster__pb2.StepResponse.FromString,
        )


class ClusterServicer(object):
  """Cluster defines communication between cluster members.
  """

  def Submit(self, request_iterator, context):
    """Submit submits transactions to a cluster member
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Step(self, request, context):
    """Step passes an implementation-specific message to another cluster member.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ClusterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Submit': grpc.stream_stream_rpc_method_handler(
          servicer.Submit,
          request_deserializer=snakeskin_dot_protos_dot_orderer_dot_cluster__pb2.SubmitRequest.FromString,
          response_serializer=snakeskin_dot_protos_dot_orderer_dot_cluster__pb2.SubmitResponse.SerializeToString,
      ),
      'Step': grpc.unary_unary_rpc_method_handler(
          servicer.Step,
          request_deserializer=snakeskin_dot_protos_dot_orderer_dot_cluster__pb2.StepRequest.FromString,
          response_serializer=snakeskin_dot_protos_dot_orderer_dot_cluster__pb2.StepResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'orderer.Cluster', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
