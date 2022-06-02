
def qshtml(qs):
    lst = []
    if qs is not None:
        for line in qs:
            lst.append(f'<a href="update_teachers/{line.pk}">Edit</a>&nbsp;&nbsp;{line}')
    else:
        lst.append("QuerySet is empy")

    return lst