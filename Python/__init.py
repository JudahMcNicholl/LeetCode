import os, argparse
parser = argparse.ArgumentParser("Python Initializer")
parser.add_argument("-question", help="LeetCode Question ")
args = parser.parse_args()

if not os.path.exists(args.question):
    os.makedirs(args.question)

path = os.path.join(args.question, "solution.py")

with open(path, "w") as w:
    w.writelines(f"#Code for question {args.question} in LeetCode\n\n")
    w.writelines(f"class Solution:\n\tdef {args.question}():\n\t\tpass\n\n")
    w.writelines(f"if __name__ == '__main__()':\n\tsolution = Solution()\n\tsolution.{args.question}()\n\n")
