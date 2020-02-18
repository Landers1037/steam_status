# steam_status
一款简易steam好友在线状态爬虫工具，同时是一款CLI工具

## 环境

python3.6+

## 下载

```bash
git clone https://github.com/Landers1037/steam_status.git
```

## 使用

### CLI工具

```bash
steam_status.py run --name=用户名
```

非精准抓取，仅抓取符合名称的第一个结果

```bash
steam_status.py run --url=用户主页地址
```

精准抓取，返回并打印出在线状态

### 服务端工具

```bash
python main.py
```

服务端默认使用redis对状态进行缓存，默认的抓取频率为5min/次

你可以参考说明文档修改抓取频率和关闭redis缓存，改为其他的方式保存在线状态

## 使用范例

```bash
Usage: steam_cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  run      指定用户名称或准确的用户主页地址
  version  版本信息
```

按用户名抓取

```bash
steam_status.py run --name=用户名
#if not work try
python steam_status.py run --name=用户名
```

按地址抓取

```bash
steam_status.py run --url=https://steamcommunity.com/profiles/xxxx
#if not work try
python steam_status.py run --url=https://steamcommunity.com/profiles/xxxx
```

版本信息

```bash
steam_status.py version
```

## 许可证

📄 [Apache License](https://github.com/Landers1037/steam_status/blob/master/LICENSE)