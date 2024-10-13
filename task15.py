from datetime import datetime


def sort(x):
    def parse_date(student):
        return datetime.strptime(student[1] , '%d.%m.%y') 
    return tuple (sorted(x , key=parse_date))

students = (["Орос Максим Ярославович", '19.02.07'], ['Бобіта Ігор Олександрович', '13.10.07'], ['Грига Анна Ярославівна', '06.06.07'])
sorted = sort(students)
print(sorted)