# python-hello-evolution

To run type
```bash
python hello.py
```

To run with custom parameters
```bash
python hello.py -t MyHelloString -p 100
```
where
- `-p` is number of population (default is 10000)
- `-t` is looked string (default `Hello-Evolution`)

Sample output
```
Generation | Fitness | Phenotype
--------------------------------------
         1 |   148.0 | ?itti*Bb}tWzl`y
         2 |   122.0 | ?Xpm|4Hs]{v~Xpu
         3 |    93.0 | Ha]gr2<stcvlQpo
         4 |    63.0 | =ii_t.Nvoiswgjl
         5 |    46.0 | Iamtt.Nvoiswgjl
         6 |    33.0 | Cfhon.Fpplypinm
         7 |    26.0 | Helgn(Hvimwtinl
         8 |    23.0 | Ielmo.Broiswgnl
         9 |    16.0 | Helqp*Cvonvtinm
        10 |    10.0 | Helmo.Bvpiutioo
        11 |     6.0 | Helmo.Gvomutinn
        12 |     4.0 | Helmo.Fvolutioo
        13 |     2.0 | Hello.Dvolution
        14 |     2.0 | Hello.Dvolution
        15 |     0.0 | Hello-Evolution
```

To run test type
```bash
py.test tests.py
```