
def send_tcp():
    import socket


    # 创建 socket 对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    port = 8080
    host = "10.12.50.174"

    # 连接服务，指定主机和端口
    client_socket.connect((host, port))
    
    # 发送数据
    while True:
        
        msg='start...\n'
        client_socket.send(msg.encode('utf-8'))
        response = client_socket.recv(1024)
        print("send successly")
        operate= response.decode('utf-8').rstrip("\n")
        from gpio import pin13
        
        if operate == 'on':
            pin13.on()
        elif operate == 'off':
            pin13.off()
        else:
            client_socket.send('unkown...\n\n'.encode('utf-8'))
#         msg=input("send:")
#         msg+='\n'
#         client_socket.send(msg.encode('utf-8'))
#         # 接收服务器的响应
#         response = client_socket.recv(1024)
#         print("response:",response.decode('utf-8'))
        

    

