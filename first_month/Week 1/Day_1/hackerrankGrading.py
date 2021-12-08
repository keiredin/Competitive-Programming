def gradingStudents(grades):
    g = []
    for grade in grades:
        if(grade % 5 > 2 and grade > 37):
            g.append(grade + (5 - (grade % 5)))
        elif(grade < 38):
            g.append(grade)
        else:
            g.append(grade)
            
    return g


s = [4, 73 ,67, 38, 33]

print(gradingStudents(s))