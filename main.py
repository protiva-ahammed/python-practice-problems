from cpProblems.binary_search import Solution8
from cpProblems.prefix_sufix_sum import Solution1
from cpProblems.longest_consecutive_consequnce import Solution2
from cpProblems.search_2d_matrix import Solution9
from cpProblems.trap_rain_water import Solution7
from cpProblems.two_sum import Solution3
from cpProblems.three_sum_two_pointer import Solution5
from cpProblems.maximum_water_container import Solution6
from cpProblems.binary_search_rotated_sorted_array import Solution10
def main():
      # Take input from user
    input_str = input("Enter numbers separated by spaces: ")
    
    # Convert string input to list of integers
    nums = list(map(int, input_str.strip().split()))

    #2D matrix input taking
    # matrix = []
    # rows = int(input("row : "))
    # cols = int (input("cols : "))
    # for i in range (rows):
    #   row_input = input().split()
    #   row = [int(x) for x in row_input]
    #   matrix.append(row)
    





    
    print("Running problem :")
    solve = Solution10()
    # res = solve.longestConsecutive(nums)
    # res = solve.maxAreaTwoPointer(nums)
    # res = solve.searchMatrixBrute(matrix, 5)
    # res1 = solve.searchMatrixBinary(matrix , 3)
    ans = solve.search(nums , 0)
    print(ans)



if __name__ == "__main__":
    main()
