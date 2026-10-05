working_year=int(input("enter the working year:"))
performance_rating=int(input("enter the performance rating:"))
if performance_rating>=4 and working_year>=2:
    print("eligible for bones")
else:
    print("not eligible for bones")