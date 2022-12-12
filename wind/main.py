from datetime import datetime


def wind(filepathcase, filepathoverdusecase, annualinterestrate=36, deferral=30, reportdate=datetime.today()):
    caselist = open(filepathcase, "r", encoding="utf-8")
    overdusecaselist = open(filepathoverdusecase, "r", encoding="utf-8")

    lines = caselist.readlines()
    lines2 = overdusecaselist.readlines()

    result = []

    for line in lines:
        x = line.split("    ")
        date_time = x[2]
        date_time_obj = datetime.strptime(date_time, '%Y-%m-%d')
        diff = reportdate - date_time_obj
        if diff.days > deferral:
            debt = int(x[3]) * diff.days * (annualinterestrate/360)
            result.append(x[1]+"    "+str(debt) + "\n")

    result.extend(lines2)
    stringresult = "".join(result)
    overdusecaselist = open(filepathoverdusecase, "w", encoding="utf-8")
    overdusecaselist.write(stringresult)
    caselist.close()
    overdusecaselist.close()
    return len(result)


wind("dane.txt", "dane2.txt")
