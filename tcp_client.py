# -*- coding: utf-8 -*-

import socket

#------------------------------------------------------------------------------
# PythonでTCP通信する（クライアント側）
#
# 2020-11-05, v0, suzutomo
#

#------------------------------------------------------------------------------
# サーバに文字列を送信し、折返電文を受信するTCPクライアント
#
def tcp_client(address: str, port: int):
  # サーバソケットを作成する
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # サーバに接続する
    server.connect((address, port))
    server_address = server.getsockname()
    print('{} - {}'.format('Connected to server', server_address))

    while True:
      # 文字列の入力を促す
      line = input('$ ')

      # 'quit'が入力されたら終了する
      if line == 'quit':
        # サーバソケットを閉じる
        server.shutdown(socket.SHUT_RDWR)
        server.close()
        print('{} - {}'.format('Disconnected from server', server_address))
        break

      # サーバへ電文を送信する
      send_data = line.encode('utf-8')
      server.sendall(send_data)
      print('{} - {}'.format('Send', send_data))

      # サーバから電文を受信する
      recv_data = server.recv(1024)
      print('{} - {}'.format('Recv', recv_data))


#------------------------------------------------------------------------------
#
tcp_client('localhost', 8888)
