import grpc
from concurrent import futures
import inventory_pb2
import inventory_pb2_grpc

class InventoryServicer(inventory_pb2_grpc.InventoryServiceServicer):
    def searchByID(self, request, context):
        # Implement searchByID logic here and return an InventoryRecord object
        response = inventory_pb2.InventoryRecord(id=request.id, name="Item 1", description="Sample Item")
        return response

    def search(self, request, context):
        # Implement search logic here and return an InventoryRecord object
        response = inventory_pb2.InventoryRecord(id="IN0001", name="Item 1", description="Sample Item")
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
