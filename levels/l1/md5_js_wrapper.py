#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：yuanrenxue 
@File    ：md5_js_wrapper.py
@IDE     ：PyCharm 
@Author  ：Allen.Wan
@Date    ：2024/8/26 下午3:47 
@explain : 文件说明
"""
import execjs


class MD5JSWrapper:
    def __init__(self, js_file_path):
        # 加载并编译 JavaScript 文件
        with open(js_file_path, 'r', encoding='utf-8') as file:
            self.ctx = execjs.compile(file.read())

    def hex_md5(self, input_str):
        # 调用 JavaScript 中的 hex_md5 方法
        return self.ctx.call('hex_md5', input_str)

    def core_md5(self, x, len):
        # 调用 JavaScript 中的 core_md5 方法
        return self.ctx.call('core_md5', x, len)

    def str2binl(self, input_str):
        # 调用 JavaScript 中的 str2binl 方法
        return self.ctx.call('str2binl', input_str)

    def binl2hex(self, binarray):
        # 调用 JavaScript 中的 binl2hex 方法
        return self.ctx.call('binl2hex', binarray)

    # 你可以继续添加其他 JS 方法的包装函数


# 使用示例
# if __name__ == "__main__":
#     md5_wrapper = MD5JSWrapper(r'E:\SpiderProject\yuanrenxue\levels\l1\md5_mogai.js')
#
#     input_str = '1724762749000'
#
#     # 调用 hex_md5
#     md5_hash = md5_wrapper.hex_md5(input_str)
#     print(f"MD5 Hash: {md5_hash}")

