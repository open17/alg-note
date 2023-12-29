import sys
def fstream(func):
    def wrapper():
        input_file = open('data.in', 'r')
        sys.stdin = input_file
        output_file = open('data.out', 'w')
        sys.stdout = output_file
        func()
        input_file.close()
        sys.stdin = sys.__stdin__
        output_file.close()
        sys.stdout = sys.__stdout__
    return wrapper

input = lambda: sys.stdin.readline().rstrip("\r\n")

def I():
    return input()
 
def II():
    return int(input())
 
def MII():
    return map(int, input().split())
 
def LI():
    return list(input().split())
 
def LII():
    return list(map(int, input().split()))

def for_t(func):
    def wrapper():
        T=II()
        for _ in range(T):
            func()
    return wrapper

@fstream
@for_t
def solve():
    pass


# def read():
#     """
#     似乎有点问题
#     """
#     x = 0
#     f = 1
#     ch = sys.stdin.buffer.read(1).decode()
#     while ch < '0' or ch > '9':
#         if ch == '-':
#             f = -1
#         ch = sys.stdin.buffer.read(1).decode()
#     while ch >= '0' and ch <= '9':
#         x = x * 10 + int(ch)
#         ch = sys.stdin.buffer.read(1).decode()
#     return x * f