student={"Anu":[59,56,90],"Gowri":[45,89,90],"Vishnu":[95,80,67]}
for name,marks in student.items():
    total=sum(marks)
    average=sum(marks)/len(marks)
    print(f"Student : {name}")
    print(f"Average Marks : {average}")
    print(f"Total Marks : {total}")
    print(f"Average Marks : {average:.2f}")
    print("."*20)