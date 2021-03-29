import os, argparse
parser = argparse.ArgumentParser("Python Initializer")
parser.add_argument("-question", help="LeetCode Question ")
args = parser.parse_args()

if not os.path.exists(args.question):
    os.makedirs(args.question)

path = os.path.join(args.question, "solution.py")

with open(path, "w") as w:
    camelCase = f"{args.question[0].lower()}{args.question[1:]}"
    w.writelines(f"#Code for question {args.question} in LeetCode\n\n")
    w.writelines(f"class Solution:\n\tdef {camelCase}(self):\n\t\tpass\n\n")
    w.writelines(f"if __name__ == '__main__':\n\tsolution = Solution()\n\tsolution.{camelCase}()\n\n")
