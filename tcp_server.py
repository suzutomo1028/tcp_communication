# -*- coding: utf-8 -*-

import socket

#------------------------------------------------------------------------------
# PythonでTCP通信する（サーバ側）
#
# 2020-11-05, v0, suzutomo
#

#------------------------------------------------------------------------------
# 受信電文を折返し送信するTCPサーバ
#
def tcp_server(address: str, port: int):
  # サーバソケットを作成する
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # サーバアドレスをソケットに接続する
    server.bind((address, port))

    # クライアントの接続を待機する
    server.listen(1)
    server_address = server.getsockname()
    print('{} - {}'.format('Server started', server_address))

    while True:
      # クライアントの接続を受入れる
      client, client_address = server.accept()
      print('{} - {}'.format('Client connected', client_address))

      with client:
        while True:
          # クライアントから電文を受信する
          data = client.recv(1024)
          print('{} - {}'.format('Recv', data))

          # クライアントが切断したら終了する
          if not data:
            # クライアントソケットを閉じる
            client.shutdown(socket.SHUT_RDWR)
            client.close()
            print('{} - {}'.format('Client disconnected', client_address))
            break

          # クライアントへ電文を送信する
          client.sendall(data)
          print('{} - {}'.format('Send', data))


#------------------------------------------------------------------------------
#
tcp_server('localhost', 8888)
