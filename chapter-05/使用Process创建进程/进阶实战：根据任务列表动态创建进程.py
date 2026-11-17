"""这道题比前两道再深入一点，重点考察你能否灵活创建多个 Process。"""

# 现在有四项任务：
# - 张三：数据分析
# - 李四：文件整理
# - 王五：数据统计
# - 赵六：报表制作
# 要求：
# 1. 定义一个 work(username, task) 函数，打印执行者和任务。
# 2. 把四项任务放进一个列表中。
# 3. 使用 for 循环遍历列表。
# 4. 每遍历一项任务，就创建一个 Process。
# 5. 每个进程都要有不同的名称，并使用 kwargs 传递参数。
# 6. 启动每一个进程。
# 这次不要手动创建四个进程，要通过循环动态创建
from multiprocessing import Process,current_process



def work(username,task):
    print(f'{current_process().name}：{username}正在进行{task}')

if __name__ == '__main__':

    tasks = [{'username':'张三',
              'task':'数据分析'},
             {'username':'李四',
              'task':'文件整理'},
             {'username': '王五',
              'task': '数据统计'},
             {'username': '赵六',
              'task': '报表制作'}
             ]
    pros = []
    for t in tasks:
        p = Process(target=work,
                    name=f'任务进程--{t['username']}',
                    kwargs={'username':t['username'],'task':t['task']}
                    )
        pros.append(p)

    for p in pros:
        p.start()