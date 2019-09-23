#!/usr/bin/env python3

from multiprocessing import Pipe, Process

conn1, conn2 = Pipe()

def send():
    data = 'hello shiyanlou'
    conn1.send(data)
    print('send data:{}'.format(data))

def recv():
    data = conn2.recv()
    print('Recevie data:{}'.format(data))

def main():
    Process(target=send).start()
    Process(target=recv).start()

if __name__ == '__main':
    main()


