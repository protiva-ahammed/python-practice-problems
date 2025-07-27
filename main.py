from cpProblems.prefix_sufix_sum import Solution
def main():
      # Take input from user
    input_str = input("Enter numbers separated by spaces: ")
    
    # Convert string input to list of integers
    nums = list(map(int, input_str.strip().split()))
    
    print("Running problem 1:")
    solve = Solution()
    res = solve.productExceptSelf(nums)
    print(res)



if __name__ == "__main__":
    main()
