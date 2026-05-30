# 工具函数库
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    """除法函数"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
