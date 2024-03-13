import asyncio
import websockets
import blockchain as bc
import pickle

# connected clients
clients = set()

# This is the blockchain that will store the votes
blockchain = [bc.create_genesis_block()]
previous_block = blockchain[0]

# This is the server that will listen for incoming votes from the voting screen
async def handle_client(websocket, path):
    global previous_block
    
    try:
        print(f"Voting Screen Live:")

        # list of clients
        clients.add(websocket)

        # Continuously listen for messages from the client
        while True:
            message = await websocket.recv()
            if not message:
                break  
            
            if len(message) == 1:
                new_block = bc.create_new_block(previous_block, message)
                blockchain.append(new_block)
                previous_block = new_block

                # forward the block to another receiver
                await forward_message(websocket, f"{new_block}")

                # storing the blocks in a encrypted file
                with open("./Polling_Records/encrypted_blockchain.bin", "ab") as file:
                    pickle.dump(blockchain, file)
            else:
                with open("./Polling_Records/registered_candidates.txt", "r") as file:
                    if message not in file.read():
                        # with open("./Polling_Records/registered_candidates.txt", "a") as file:
                        #     file.write(f"{message}\n")
                        await websocket.send("0")
                    else:
                        for client in clients:
                            await client.send("1")
    except websockets.exceptions.ConnectionClosedError:
        print(f"Client disconnected: {websocket}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Remove the client from the set of connected clients upon disconnection
        clients.remove(websocket)

async def forward_message(websocket, message):
    # forward the message to all connected clients
    for client in clients:
        if client != websocket:
            await client.send(message)


async def start_server():
    server = await websockets.serve(handle_client, "192.168.5.55", 8765)
    print("Server listening on ws://localhost:8765")
    
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_server())









