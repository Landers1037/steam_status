#! /usr/bin/env/ python
# -*- coding: utf-8 -*-
# Time: 2020-02-18 10:18
# Author: Landers1037
# Mail: liaorenj@gmail.com
# File: steam_cli.py

#cli tool
import click
import json
from check_stats import check
from info import __version__,__py_version__,__project_name__

@click.group()
def steam_status():
    pass

@click.command()
@click.option('--name', help='steam user name')
@click.option('--url', help='steam user address')
def run(name,url):
    """指定用户名称或准确的用户主页地址"""
    if name or url:
        if name:
            click.echo("steam用户名："+name)
            s = check(name=name)
            if s:
                click.echo("当前用户在线")
            elif not s:
                click.echo("当前用户离线")
            else:
                click.echo("数据获取失败")
        if url:
            click.echo("steam链接：" + url)
            s = check(url=url)
            if s:
                click.echo("当前用户在线")
            elif not s:
                click.echo("当前用户离线")
            else:
                click.echo("数据获取失败")

@click.command(help="版本信息")
def version():
    out = "当前版本：{}\npython版本：{}\n程序名称：{}\n".format(__version__,__py_version__,__project_name__)
    click.echo(out)

steam_status.add_command(run)
steam_status.add_command(version)

if __name__ == '__main__':
    steam_status()