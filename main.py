from cpProblems.binary_search import Solution8
from cpProblems.find_max_substr_len_sliding_window import Solution16
from cpProblems.prefix_sufix_sum import Solution1
from cpProblems.longest_consecutive_consequnce import Solution2
from cpProblems.search_2d_matrix import Solution9
from cpProblems.trap_rain_water import Solution7
from cpProblems.two_sum import Solution3
from cpProblems.three_sum_two_pointer import Solution5
from cpProblems.maximum_water_container import Solution6
from cpProblems.binary_search_rotated_sorted_array import Solution10
from cpProblems.time_based_key_store import TimeMap
from cpProblems.vaild_parenthesis import Solution12
from cpProblems.min_stack import __init__
from cpProblems.polish_notation import Solution13
from cpProblems.gcd_lcm_recursive import Solution14
from find_all_substring import Solution15

def main():
      # Take input from user
    # input_str = input("Enter numbers separated by spaces: ")
    
    # Convert string input to list of integers
    # nums = list(map(int, input_str.strip().split()))

    #2D matrix input taking
    # matrix = []
    # rows = int(input("row : "))
    # cols = int (input("cols : "))
    # for i in range (rows):
    #   row_input = input().split()
    #   row = [int(x) for x in row_input]
    #   matrix.append(row)
    





    
    print("Running problem :")
    solve = Solution16()
    # res = solve.longestConsecutive(nums)
    # res = solve.maxAreaTwoPointer(nums)
    # res = solve.searchMatrixBrute(matrix, 5)
    # res1 = solve.searchMatrixBinary(matrix , 3)
    # ans = solve.isValid("(}{})]")
    # ans1 = solve.gcdRec(14,8)
    # ans2 = solve.lcm(56,3)
    #search(nums , 0)
    ans = solve.lengthOfLongestSubstring("abbcd")
    print(ans," ")



if __name__ == "__main__":
    main()
