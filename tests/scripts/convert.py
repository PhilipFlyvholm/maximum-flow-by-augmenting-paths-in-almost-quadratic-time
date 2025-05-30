inp = """
0-(11)>1
0-(24)>2
0-(3)>3
0-(24)>4
1-(17)>5
2-(5)>1
2-(7)>6
3-(5)>7
3-(1)>8
4-(20)>9
5-(20)>10
5-(15)>11
6-(3)>5
6-(5)>11
7-(7)>11
8-(7)>12
9-(1)>13
9-(24)>14
10-(2)>16
10-(5)>17
11-(5)>17
11-(20)>18
12-(15)>18
13-(19)>19
14-(15)>13
14-(7)>15
14-(9)>20
15-(7)>20
16-(5)>21
17-(15)>21
18-(15)>22
19-(15)>12
19-(15)>23
20-(19)>19
21-(19)>24
22-(20)>24
23-(19)>24
""".strip()

for line in inp.split("\n"):
    u, rem = line.split("-(")
    cap, v = rem.split(")>")

    print(f'{u} -> {v} [label="{cap}"];')
