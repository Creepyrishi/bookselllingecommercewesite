def arithmetic_arranger(problems, solve=False):
  if len(problems) < 5:
    for problem in problems:

      x = problem.split(" ")[0]
      operation = problem.split(" ")[1]
      y = problem.split(" ")[2]
      print(operation)

      if operation == "+" or operation == "-":
        
        pass

      else:
        arranged_problems = "Error: Operator must be '+' or '-'."
        return arranged_problems
        break
        
  else:
    arranged_problems = "Error: Too many problems."

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))