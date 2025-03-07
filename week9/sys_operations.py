import platform
import socket
import os
import sys

print("Machine Type: " + platform.machine())

print("Processor Type: " + platform.architecture())

socket.setdefaulttimeout(50)
print("Get the default Socket Timeout in seconds")
print(socket.getdefaulttimeout())

print("OS Type: " + os.name)
print("OS Name: " + platform.system())

print("Current PID: " + os.getpid())

file_name = "fdpractice.txt"
file_handle = os.open(file_name, os.O_RDWR | os.O_CREAT)
print(f"\n[Process {os.getpid()}] Open file_handle: {file_handle}")

file_object_TextIO = os.fdopen(file_handle, "w+")
file_object_TextIO.write("Some string to write to the file, like Hello World!")
file_object_TextIO.flush()

pid = os.fork()
if pid == 0:
    print(f"\n[Child Process {os.getpid()}], [Parent Process {os.getppid()}]")
    os.lseek(file_handle, 0, 0)

    print(f"[ File Content: {os.read(file_handle, 100).decode()} ]")
    os.close(file_handle)
    sys.exit(0)
else:
    print(f"\n[Parent Process {os.getppid()}], [Child Process {os.getpid()}]")
    print("Wait for the child process to finish its task")
    os.wait()
    print("Child process has finished its task")
    os.close(file_handle)
print(f"\n[Process {os.getppid()}] File closed. Exiting now.")
sys.exit(0)