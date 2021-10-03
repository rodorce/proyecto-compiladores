from sly import Parser
from Lexer import Lexer


class Parser(Parser):
    tokens = Lexer.tokens
    def __init__(self):
        self.ids = {"prueba": 10}
        self.variables = {}

    @_('IF "(" EXP ")" THEN "{" ESTATUTO "}" ELSE "{" ESTATUTO "}" ')
    def CONDICION(self, p):
        if eval("p.EXP[1]" + p.EXP[0] + "p.EXP[2]"):
            p.ESTATUTO0
        else:
            p.ESTATUTO1

    @_('IF "(" EXP ")" THEN "{" ESTATUTO "}"')
    def CONDICION(self, p):
        if eval("p.EXP[1]" + p.EXP[0] + "p.EXP[2]"):
            p.ESTATUTO
            print(p.ESTATUTO)

    @_('FOR ASIGNACION TO EXP DO "{" ESTATUTO "}"')
    def CICLO_F(self, p):
        x = p.ASIGNACION
        for x in p.EXP:
            p.ESTATUTO

    @_('ASIGNACION')
    def ESTATUTO(self, p):
        return p.ASIGNACION

    @_('VARIABLE ASSIGN EXP ";"')
    def ASIGNACION(self, p):
        self.ids[p.VARIABLE] = p.EXP
        return self.ids[p.VARIABLE]

    @_('READ "(" ID ")" ";"')
    def VARIABLE(self, p):
        print(self.ids[p.ID])

    @_('ID')
    def VARIABLE(self, p):
        if p.ID in self.ids:
            return p.ID
        else:
            self.ids[p.ID] = None
            return p.ID


    @_('T_EXP OR T_EXP')
    def EXP(self, p):
        if p.T_EXP0 or p.T_EXP1:
            return True
        else:
            return False

    @_('T_EXP')
    def EXP(self, p):
        return p.T_EXP

    @_('G_EXP AND G_EXP')
    def T_EXP(self, p):
        if p.G_EXP0 and p.G_EXP1:
            return True
        else:
            return False

    @_('G_EXP')
    def T_EXP(self, p):
        return p.G_EXP

    @_('M_EXP DT M_EXP')
    def G_EXP(self, p):
        return p.M_EXP0 != p.M_EXP1

    @_('M_EXP EQ M_EXP')
    def G_EXP(self, p):
        return p.M_EXP0 == p.M_EXP1

    @_('M_EXP LT M_EXP')
    def G_EXP(self, p):
        return p.M_EXP0 < p.M_EXP1

    @_('M_EXP GT M_EXP')
    def G_EXP(self, p):
        return ('>', p.M_EXP0, p.M_EXP1)

    @_('M_EXP')
    def G_EXP(self, p):
        return p.M_EXP

    @_('T MINUS T')
    def M_EXP(self, p):
        return p.T0 - p.T1

    @_('T PLUS T')
    def M_EXP(self, p):
        return p.T0 + p.T1

    @_('T')
    def M_EXP(self, p):
        return p.T

    @_('F TIMES F')
    def T(self, p):
        return p.F0 * p.F1

    @_('F DIVIDE F')
    def T(self, p):
        return p.F0 / p.F1

    @_('F')
    def T(self, p):
        return p.F

    @_('CTE_F')
    def F(self, p):
        return p.CTE_F

    @_('CTE_INT')
    def F(self, p):
        return p.CTE_INT

    @_('CTE_CHAR')
    def F(self, p):
        return p.CTE_CHAR

    @_('"(" EXP ")"')
    def F(self, p):
        return p.EXP

    @_('VARIABLE')
    def F(self, p):
        return self.ids[p.VARIABLE]


if __name__ == '__main__':
    lexer = Lexer()
    parser = Parser()

    while True:
        try:
            text = input('')
            result = parser.parse(lexer.tokenize(text))
            print(result)
        except EOFError:
            break
