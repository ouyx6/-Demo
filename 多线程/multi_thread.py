import threading

def hello(name):
    print('the son process, Id:{}'.format(threading.get_ident()))
    print('hello' + name)

def main():
    print('the main process, ID:{}'.format(threading.get_ident()))
    print('-------------------')
    t = threading.Thread(target = hello,args=('shiyanlou',))
    t.start()
    t.join()
    print('-------------------')
    print('now the main process, ID:{}'.format(threading.get_ident()))

if __name__ =='__main':
    main()
