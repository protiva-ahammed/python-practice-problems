from cpProblems.prefix_sufix_sum import Solution1
from cpProblems.longest_consecutive_consequnce import Solution2
from cpProblems.two_sum import Solution3
from cpProblems.three_sum_two_pointer import Solution5
from cpProblems.maximum_water_container import Solution6

def main():
      # Take input from user
    input_str = input("Enter numbers separated by spaces: ")
    
    # Convert string input to list of integers
    nums = list(map(int, input_str.strip().split()))
    
    print("Running problem :")
    solve = Solution6()
    # res = solve.longestConsecutive(nums)
    res = solve.maxArea(nums)
    print(res)



if __name__ == "__main__":
    main()
