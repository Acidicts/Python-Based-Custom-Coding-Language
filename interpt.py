import sys
import re


class Ev:
    def __init__(self):
        self.vars = {}
        self.funcs = {}

    def ev(self, s):
        lines = [x for x in s.split("\n") if x.strip() != ""]
        pc = 0
        pcl = 0

        while pc < len(lines):
            line = lines[pc]
            match line.split(maxsplit=1)[0]:
                case 'while':
                    if self.ev_expr(line.split(maxsplit=1)[1]):
                        pc += 1
                    else:
                        while lines[pc].split(maxsplit=1)[0] != "end":
                            pc += 1
                        pc += 1
                case 'end':
                    while lines[pc].split(maxsplit=1)[0] != "while":
                        pc -= 1
                case 'print':
                    try:
                        expr = line.split(maxsplit=1)[1]
                        parts = re.findall(r'\".*?\"|\'.*?\'|\S+', expr)
                        result = ""
                        for part in parts:
                            if (part.startswith('"') and part.endswith('"')) or (
                                    part.startswith("'") and part.endswith("'")):
                                result += part[1:-1]
                            else:
                                result += str(self.ev_expr(part))
                        print(result)
                    except Exception as e:
                        print(e)
                    pc += 1
                case 'func':
                    func_name = line.split(maxsplit=1)[1]
                    self.funcs[func_name] = pc + 1
                    while lines[pc].split(maxsplit=1)[0] != "funcend":
                        pc += 1
                    pc += 1
                case 'funcend':
                    pc = pcl
                case 'call':
                    func_name = line.split(maxsplit=1)[1]
                    pcl = pc + 1
                    pc = self.funcs[func_name]
                case _:
                    (name, _, expr) = line.split(maxsplit=2)
                    self.vars[name] = self.ev_expr(expr)
                    pc += 1

    def ev_expr(self, s):
        toks = s.split()
        stack = []

        for tok in toks:
            if tok.isdigit():
                stack.append(int(tok))
            elif tok in self.vars:
                stack.append(self.vars[tok])
            else:
                rhs = stack.pop()
                lhs = stack.pop()

                if tok == "+": stack.append(lhs + rhs)
                elif tok == "*": stack.append(lhs * rhs)
                elif tok == "-": stack.append(lhs - rhs)
                elif tok == ">=": stack.append(int(lhs >= rhs))
                elif tok == "<=": stack.append(int(lhs <= rhs))

        return stack[0]

Ev().ev(open(sys.argv[1]).read())
