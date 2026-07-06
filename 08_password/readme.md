# bcrypt
* pip install bcrypt 
    $2b$12$KbQiHKENeLGNHDmYgwnM2uPj3Vu1AIgdrkQoUApPeuVm5YhFUhVnG
    │   │  │                     │
    │   │  │                     └─ Hash-Wert: 31 Zeichen
    │   │  └─ Salt: 22 Zeichen
    │   └──── Cost-Faktor: 2 Zeichen
    └──────── Version: $2b$





# argon2

* pip install argon2-cffi

    argon2id  -> Algorithmus
    v=19      -> Version
    m=65536   -> Speicheraufwand
    t=3       -> Iterationen
    p=4       -> Parallelität
    Salt      -> zufälliger Salt
    Hash      -> berechneter Passwort-Hash