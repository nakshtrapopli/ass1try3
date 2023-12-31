# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import inventory_pb2 as inventory__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.searchByID = channel.unary_unary(
                '/InventoryService/searchByID',
                request_serializer=inventory__pb2.InventoryRequest.SerializeToString,
                response_deserializer=inventory__pb2.InventoryRecord.FromString,
                )
        self.search = channel.unary_unary(
                '/InventoryService/search',
                request_serializer=inventory__pb2.InventorySearchRequest.SerializeToString,
                response_deserializer=inventory__pb2.InventoryRecord.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def searchByID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def search(self, request, context):
        """Add other RPC methods for searching, updating, etc.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'searchByID': grpc.unary_unary_rpc_method_handler(
                    servicer.searchByID,
                    request_deserializer=inventory__pb2.InventoryRequest.FromString,
                    response_serializer=inventory__pb2.InventoryRecord.SerializeToString,
            ),
            'search': grpc.unary_unary_rpc_method_handler(
                    servicer.search,
                    request_deserializer=inventory__pb2.InventorySearchRequest.FromString,
                    response_serializer=inventory__pb2.InventoryRecord.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def searchByID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/searchByID',
            inventory__pb2.InventoryRequest.SerializeToString,
            inventory__pb2.InventoryRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/search',
            inventory__pb2.InventorySearchRequest.SerializeToString,
            inventory__pb2.InventoryRecord.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
