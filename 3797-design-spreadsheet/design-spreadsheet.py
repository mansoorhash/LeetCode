class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = defaultdict(int)
        

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        c1, c2 = formula.strip("=").split("+")
        c1_value = int(c1) if c1.isdigit() else self.sheet[c1]
        c2_value = int(c2) if c2.isdigit() else self.sheet[c2]
        return c1_value + c2_value


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)