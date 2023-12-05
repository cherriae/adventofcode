string = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

#e = string.split("\n")
#final = []

#for i in e:
#    something = []
#    something2 = []
#    for x in list(i):
#        try: 
#            something.append(int(x))
#        except:
#            pass
#    if len(something) > 2:
#        something = something[:1] + something[-1:]
#    if len(something) == 1:
#        something.append(something[0])

#    for x in something:
#        something2.append(str(x))

#    final.append("".join(something2))

#number = 0

#for x in final:
#    number += int(x)

class Calibration:
    def calibrate(self, string: str):
        lines = string.split("\n")
        result = 0
        for line in lines:
            digits = [int(x) for x in line if x.isdigit()]
            if len(digits) > 2:
                digits = digits[:1] + digits[-1:]
            elif len(digits) == 1:
                digits.append(digits[0])
            result += int("".join(map(str, digits)))