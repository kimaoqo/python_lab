def format_record(rec: tuple[str, str, float]) -> str:
    try:
        fio = (rec[0].strip().lstrip()).split()
        initials = fio[0].capitalize() + ' ' + fio[1][0].upper() + '.' if len(fio) == 2 else fio[0].capitalize() + ' ' + fio[1][0].upper() + '.' + fio[2][0].upper() + '.'
        group = rec[1].strip().lstrip()
    except IndexError:
        return TypeError
    else:
        gpa = rec[2]
        if 2 <= gpa <= 5:
            return f'{initials}, гр.{group}, GPA{gpa: .2f}'
        else:
            return ValueError



student = (input(), input(), float(input()))
print(format_record(student))