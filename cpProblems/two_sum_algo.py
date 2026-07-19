def two_sum(a, b):
    if 0 <= a <= 9 and 0 <= b <= 9:
        return a + b
    return 0
 
a, b = map(int, input().split())
print(two_sum(a, b))


# def two_sum(a, b):
#     if 0 <= a <= 9 and 0 <= b <= 9: 
#         return a + b
#     return 0

# def main():
#     try:
#         a , b = map(int,input())
#         result = two_sum(a, b)
#         print(result)
#     except ValueError:
#         print('err')

# if __name__ == "__main__":
#     main()