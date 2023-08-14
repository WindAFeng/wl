from util import IOUtil
import json
import logging
import khl

# index.py 是否打算做成启动类？

if __name__ == '__main__':
    logging.basicConfig(level='INFO')  # 设置日志输出

    configData = IOUtil.readYamlFileToDict('./config/config.yml')  # 读取config设置

    bot = khl.Bot(token=configData['token'])  # 创建bot对象

    # Bot 初始化方法
    @bot.on_startup
    async def bot_init(bot: khl.Bot):
        # 这里对bot的各种消息、事件响应进行注册

        pass

    bot.run()
