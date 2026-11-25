# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers): #this is the coroutine
    # Outline (write your plan here first):
    # 1. An async function must be defined so then it can be turned into a couroutine function (which basically means that it can pause a certain functions execution so then other tasks can run in the meantime)
    # 2. Must include return n * 2 in order to double the value
    # 3. Assign coroutine objects(coroutine objects can be paused and resumed) to a list (since numbers is a list and the function needs to return a list)
    #
    # TODO (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.
    # 
    async def double(n): #async function defined with n as a parameter. n being the value of a single number in numbers
        return n * 2 # doubles the value of n

    coros = [double(n) for n in numbers] # stores coroutine objects that will be run later. [double(n) for n in numbers] is equivalent to calling the function double(n) for each value in numbers.
    return await asyncio.gather(*coros) # await waits for all the coroutines to finish running THEN it will return the results. asyncio.gather(*coros) can be broken down into two parts. asyncio.gather() means that it takes the coroutines and runs them concurrently while *coros basically unpacks all the courotinue objects (ex. double(1))


async def fastest(jobs):
    # Outline:
    #  1. Define the async function
    #  2. Create a helper coroutine function (similar to the first exercise where double(n) was the helper function)
    #  3. Use await asyncio.sleep(delay) to start everything at once and then return the label of the job that must be done first
    #  4. Use coros as the list where all the coroutine objects will be assigned to run the helper function for each label
    #  5. Use asyncio.as_completed(coros) in order to loop through all the results as they finish and the first one will be the winner/which job is the fastest
    #  6. The first result will be the fastest job.
    #
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)
    async def run_job(label, delay): #defined async function / coroutine
        await asyncio.sleep(delay) # runs all the jobs at the same time not one after the other.
        return label #returns the label of the job

    coros = [run_job(label, delay) for label, delay in jobs] #stores all the coroutine objects and runs the helper function run_job for each label/delay for each job

    for finished in asyncio.as_completed(coros): #loops over the result once its finished it doesn't wait for every job to be finished
        return await finished #therefore, the first one returned is the fastest job


def echo_once(host, port, message):
    # Outline:
    #   1. Define a function that takes the host, port, and message as parameters
    #   2. Create TCP socket
    #   3. Connect the socket to the host and port
    #   4. Use sendall() to send it into the server after the message has been encoded into bytes since sockets can only carry bytes
    #   5. Close the socket and decode the bytes back into the string using .decode
    #   6. Return the decoded string after the decoding has been complete 
    # 
    # 
    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(message.encode())
    data = s.recv(1024)
    s.close()
    
    return data.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()
