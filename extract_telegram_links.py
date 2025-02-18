import sqlite3
import os

# Chrome 历史记录数据库路径
history_db = r"C:\Users\suixing\AppData\Local\Google\Chrome\User Data\Profile 10\History"

# 复制数据库（防止 Chrome 正在使用时锁定文件）
temp_db = r"C:\Users\suixing\Desktop\History_copy.db"
os.system(f'copy "{history_db}" "{temp_db}"')

# 连接到复制的数据库
conn = sqlite3.connect(temp_db)
cursor = conn.cursor()

# 查询所有访问过的 Telegram 群聊链接
query = "SELECT url FROM urls WHERE url LIKE '%web.telegram.org/k/#@%'"
cursor.execute(query)

# 获取结果并打印
links = cursor.fetchall()
for link in links:
    print(link[0])

# 关闭数据库连接
conn.close()

# 删除临时数据库
os.remove(temp_db)
