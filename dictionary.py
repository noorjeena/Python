student={"Anu":340,"Teena":458,"john":300}
ascend=dict(sorted(student.items()))
print("sorted by name (Ascending) : ")
print(ascend)
descend=dict(sorted(student.items(),reverse=True))
print("sorted by name (Descending) : ")
print(descend)