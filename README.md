# Telegram Chat Recovery

## 项目简介
本项目是一个 Python 脚本，帮助找回 **Telegram 账号被盗** 后 **之前加入的群聊** 的链接。

如果你曾经 **在 PC 端使用过 Telegram Web**（`web.telegram.org`），并且 **没有清除浏览器历史记录**，那么可以通过 Chrome 的历史数据库提取之前访问过的群组链接。

## 适用场景
- Telegram 账号被盗，无法找回
- 重新注册新账号后，想要重新加入之前的群组
- 曾经在 PC 端使用 Telegram Web，并且没有清理浏览器历史记录

## 使用环境
### 1. 运行环境要求
- 操作系统：Windows 10/11
- Python 版本：3.6 及以上

### 2. 依赖库
本脚本不依赖任何外部库，使用 Python 内置的 `sqlite3` 和 `os`。

## 安装与使用
### 1. 安装 Python（如果未安装）
从[官方网站](https://www.python.org/downloads/)下载安装 Python，并在安装时勾选 **"Add Python to PATH"**。

### 2. 修改脚本中的 `History` 路径
Chrome 的历史记录数据库路径因用户配置不同而不同，需要手动修改 `extract_telegram_links.py` 中的 `history_db` 路径。例如：
```python
history_db = r"C:\Users\你的用户名\AppData\Local\Google\Chrome\User Data\Default\History"
```
请根据你的实际情况调整路径（例如 `Profile 1`, `Profile 2`）。

### 3. 运行脚本
1. 下载 `extract_telegram_links.py` 并放在任意位置
2. **以管理员身份** 打开命令提示符（CMD）
3. 进入脚本所在目录：
   ```sh
   cd 你的脚本路径
   ```
4. 运行脚本：
   ```sh
   python extract_telegram_links.py
   ```
5. 终端会输出所有访问过的 Telegram 群聊链接，可以手动复制并重新加入。

## 代码逻辑
1. 读取 Chrome 浏览器的历史记录数据库 (`History` 文件)
2. 查找所有包含 `web.telegram.org/k/#@` 的记录
3. 自动去重，并输出所有找到的群组链接

## 重要提醒
- **必须在 Chrome 浏览器中使用过 Telegram Web**，否则不会有相关历史记录。
- **不要清除浏览器历史记录**，否则数据将无法恢复。
- **必须关闭 Chrome 浏览器**，否则数据库文件可能被锁定，无法读取。

## 免责声明
本脚本仅用于帮助用户找回自己曾访问过的 Telegram 群聊链接，**请勿用于非法用途**。

