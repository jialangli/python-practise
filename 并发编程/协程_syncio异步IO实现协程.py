# 李佳朗
# 开发时间：2023
import asyncio

async def my_coroutine():
    # 执行异步操作
    await asyncio.sleep(1)
    print('协程执行完成')

# 创建事件循环
loop = asyncio.get_event_loop()

# 在事件循环中运行协程
loop.run_until_complete(my_coroutine())

# 关闭事件循环
loop.close()
