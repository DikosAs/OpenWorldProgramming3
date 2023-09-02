slovo = "Statistics"

# def strcount(sis: str):
#     simvols = []
#     for s in sis.lower():
#         if s not in simvols:
#             simvols.append(s)
#             col = 0
#             for c in sis:
#                 if c == s:
#                     col += 1
#             print(s, col)

def v2(s):
    sims = {}
    for sim in s:
        sims[sim] = sims.get(sim, 0)+1
    print(sims.items())


# strcount(slovo)
v2(slovo)