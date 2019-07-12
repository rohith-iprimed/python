
import re
for _ in range(int(input())):
    print(re.sub(r' [|]{2}(?= )', ' or', re.sub(r' [&]{2}(?= )', ' and', input())))
