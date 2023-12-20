# 李佳朗
# 开发时间：2023
import multiprocessing

def sender(conn):
    messages = ['Message 1', 'Message 2', 'Message 3']
    for message in messages:
        conn.send(message)
        print(f'Sent: {message}')
    conn.close()

def receiver(conn):
    while True:
        message = conn.recv()
        if message is None:
            break
        print(f'Received: {message}')
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = multiprocessing.Pipe()

    # 创建发送者进程和接收者进程
    sender_process = multiprocessing.Process(target=sender, args=(parent_conn,))
    receiver_process = multiprocessing.Process(target=receiver, args=(child_conn,))

    # 启动进程
    sender_process.start()
    receiver_process.start()

    # 等待发送者进程结束
    sender_process.join()

    # 向管道发送一个 None 值，表示数据已经全部发送完毕
    parent_conn.send(None)

    # 等待接收者进程结束
    receiver_process.join()
