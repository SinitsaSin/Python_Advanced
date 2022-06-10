def qshtml(qs):
    lst = []
    if qs is not None:
        for line in qs:
            lst.append(str(line))
    else:
        lst.append("QuerySet is empy")

    return '<br>'.join(lst)
