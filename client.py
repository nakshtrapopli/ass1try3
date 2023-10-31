import grpc
import inventory_pb2
import inventory_pb2_grpc

class InventoryClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')  # Replace with your server address and port
        self.stub = inventory_pb2_grpc.InventoryServiceStub(self.channel)

    def searchByID(self, inventory_id):
        try:
            response = self.stub.searchByID(inventory_pb2.InventoryRequest(id=inventory_id))
            print("Search By ID Response received:", response)
        except grpc.RpcError as e:
            print("Error:", e)

    def search(self, key_name, key_value):
        try:
            response = self.stub.search(inventory_pb2.InventorySearchRequest(key_name=key_name, key_value=key_value))
            print("Search Response received:", response)
        except grpc.RpcError as e:
            print("Error:", e)


if __name__ == '__main__':
    client = InventoryClient()
    # Test client methods
    client.searchByID("IN0001")
    client.search("Name", "Item 1")
