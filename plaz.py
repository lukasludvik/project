class Table:
     def __init__(self, x, y, start, end, pl):
         self.x = x
         self.y = y
         self.aval = abs(self.x - start[pl] + (self.y - start[pl + 1]))
         self.bval = abs(self.x - end[pl] + (self.y - end[pl + 1]))
         self.cval = self.aval + self.bval

start = []
end = []
sand = []

area = int(input()) #5

#Making quicksand
while True:
    x, y = [int(x) for x in input().split() if input()]
    start.append(x)
    start.append(y)
    if isinstance(x, int):
        continue
    else:
        break

print(x, y)