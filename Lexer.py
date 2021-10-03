from sly import Lexer

class Lexer(Lexer):
    # Set of token names.   This is always required
    tokens = { PROGRAM, CTE_F, CTE_INT, CTE_CHAR, VARS, TYPE, ID, WHILE, FOR, IF, ELSE, THEN, TO, RETURN,
               FUNCTION, VOID, READ, WRITE,DO, MEDIA, MODA, VARIANZA, REGRESION, PLOTXY,
               PLUS, MINUS, TIMES, DIVIDE, ASSIGN,
               EQ, LT, GT, DT, AND, OR}


    literals = { '(', ')', '{', '}', ';', ':' , ',', '[', ']', '"'}

    # String containing ignored characters
    ignore = ' \t'

    # Regular expression rules for tokens
    PLUS    = r'\+'
    MINUS   = r'-'
    TIMES   = r'\*'
    DIVIDE  = r'/'
    EQ      = r'=='
    ASSIGN  = r'='
    LT      = r'<'
    GT      = r'>'
    DT      = r'!='
    AND = r'&'
    @_(r'\d+')
    # def CTE_F(self, t):
    #     t.value = float(t.value)
    #     return t

    @_(r'\d+')
    def CTE_INT(self, t):
        t.value = int(t.value)
        return t

    # Identifiers and keywords
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    CTE_CHAR = r'\w'
    ID['or'] = OR
    ID['then'] = THEN
    ID['if'] = IF
    ID['else'] = ELSE
    ID['while'] = WHILE
    ID['for'] = FOR
    ID['Program'] = PROGRAM
    ID['VARS'] = VARS
    ID['int'] = TYPE
    ID['float'] = TYPE
    ID['char'] = TYPE
    ID['return'] = RETURN
    ID['function'] = FUNCTION
    ID['void'] = VOID
    ID['write'] = WRITE
    ID['read'] = READ
    ID['do'] = DO
    ID['Media'] = MEDIA
    ID['Moda'] = MODA
    ID['Varianza'] = VARIANZA
    ID['Regresion'] = REGRESION
    ID['PlotXY'] = PLOTXY

    ignore_comment = r'\#.*'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

if __name__ == '__main__':
    data = '''
    Program MyRLike;
    VARS
    int: i, j, p, arreglo[10];
    float: valor;
    
    function int fact(int: j)
    VARS int i;;
    { i = j + (p - j*2+j)
    if (j==1) then 
        { return (j); }
    else 
        { return (j * fact(j-1); }
    }
    
    function void calcula (int y)
    VARS int x;
    { x = 1;
     while (x < 11) do
     { y = y * arreglo[x]
       x = x+1; }
       write (arreglo[x])
       }
    write("acumulado",y);
    }
    
    principal()
    { read (p) ; j = p * 2;
    i = fact(p);
    for i = 1 to 10 do
        { arreglo[i] = p + i ; }
    p = Media (arreglo) ;
    while (i < 0) do
        { calcula(p-i)
          j = fact(arreglo[i]);
          write(j , i);
          i = i + 1;
        }
    }
'''
    lexer = Lexer()
    for tok in lexer.tokenize(data):
        print(tok)