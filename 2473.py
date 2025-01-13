def find_three_solution_closest_to_zero(N, solutions):
  solutions.sort()
  closest_sum = float('inf')
  answer = []

  for i in range(N - 2):
    left, right = i + 1, N - 1

    while left < right:
      current_sum = solutions[i] + solutions[left] + solutions[right]

      if abs(current_sum) < abs(closest_sum):
        closest_sum = current_sum
        answer = [solutions[i], solutions[left], solutions[right]]

      if current_sum > 0:
        right -= 1
      elif current_sum < 0:
        left += 1
      else:
        return sorted(answer)

  return sorted(answer)

N = int(input())
solutions = list(map(int, input().split()))

result = find_three_solution_closest_to_zero(N, solutions)
print(" ".join(map(str, result)))