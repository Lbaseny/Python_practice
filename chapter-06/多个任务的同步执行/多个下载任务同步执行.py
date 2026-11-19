"""编写一个 Python 程序，模拟同时下载 5 个文件。"""
import asyncio
from datetime import datetime


# 任务要求：
# 1. 有 5 个文件，名称分别为：
#    - file1
#    - file2
#    - file3
#    - file4
#    - file5
# 2. 每个文件下载需要的时间分别为 2、4、1、3、2 秒。
# 3. 每个文件开始下载时，打印文件名称和开始信息。
# 4. 每个文件下载完成时，打印文件名称和完成信息。
# 5. 5 个文件必须同步执行。
# 6. 所有文件下载完成后，打印：全部文件下载完成。

async def download(txt,time):
    print(f'{txt}:开始下载，预计耗时{time}s')
    await asyncio.sleep(time)
    print(f'{txt}:下载完成')
async def main():
    start = datetime.now()
    await asyncio.gather(download('file1', 2),
                  download('file2', 4),
                  download('file3', 1),
                  download('file4', 3),
                  download('file5', 2))
    print(f'全部文件下载完成，总耗时{datetime.now()-start}')

if __name__ == '__main__':
    asyncio.run(main())