# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from snakeskin.protos.discovery import protocol_pb2 as snakeskin_dot_protos_dot_discovery_dot_protocol__pb2


class DiscoveryStub(object):
  """Discovery defines a service that serves information about the fabric network
  like which peers, orderers, chaincodes, etc.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Discover = channel.unary_unary(
        '/discovery.Discovery/Discover',
        request_serializer=snakeskin_dot_protos_dot_discovery_dot_protocol__pb2.SignedRequest.SerializeToString,
        response_deserializer=snakeskin_dot_protos_dot_discovery_dot_protocol__pb2.Response.FromString,
        )


class DiscoveryServicer(object):
  """Discovery defines a service that serves information about the fabric network
  like which peers, orderers, chaincodes, etc.
  """

  def Discover(self, request, context):
    """Discover receives a signed request, and returns a response.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DiscoveryServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Discover': grpc.unary_unary_rpc_method_handler(
          servicer.Discover,
          request_deserializer=snakeskin_dot_protos_dot_discovery_dot_protocol__pb2.SignedRequest.FromString,
          response_serializer=snakeskin_dot_protos_dot_discovery_dot_protocol__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'discovery.Discovery', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
