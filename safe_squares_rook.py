def safe_squares_rooks(n, rooks):
    columns = [x for x in range(0, n)]
    rows = [x for x in range(0, n)]

    for pairs in rooks:
        if pairs[0] in rows:
            rows.remove(pairs[0])
        if pairs[1] in columns:
            columns.remove(pairs[1])

    print(len(columns) * len(rows))  ## just here for checking!


safe_squares_rooks(10 ** 6, [(r, r) for r in range(10 ** 6)])

## this seems to cause infinte loop
## otherwise good!
