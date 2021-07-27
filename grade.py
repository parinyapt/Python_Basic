mid_score = float(input('Enter Midterm Score (30) : '))
if(mid_score >30 or mid_score<0):
    print('Error Midterm score | enter again')
    mid_score = 0.0

final_score = float(input('Enter Final Score (30) : '))
if(final_score >30 or final_score<0):
    print('Error Final Score | enter again')
    final_score = 0.0

work_score = float(input('Enter Work Score (30) : '))
if(work_score >30 or work_score<0):
    print('Error Work Score | enter again')
    work_score = 0.0

affective_score = float(input('Enter Affective Score (10) : '))
if(affective_score >10 or affective_score<0):
    print('Error Affective Score | enter again')
    affective_score = 0.0

total_score = float(mid_score + final_score + work_score + affective_score)

print('--------------------------------------')
print('Score Report')
print('Midterm Score (30) : ' , mid_score)
print('Final Score (30) : ' , final_score)
print('Work Score (30) : ' , work_score)
print('Affective Score (10) : ' , affective_score)
print('Total (100) : ' , total_score)

print('--------------------------------------')


if(total_score > 100 or total_score < 0):
    print('Grade cannot calculate')
elif(total_score >= 80):
    print('Grade Result = 4')
elif(total_score >= 75):
    print('Grade Result = 3.5')
elif(total_score >= 70):
    print('Grade Result = 3')
elif(total_score >= 65):
    print('Grade Result = 2.5')
elif(total_score >= 60):
    print('Grade Result = 2')
elif(total_score >= 55):
    print('Grade Result = 1.5')
elif(total_score >= 50):
    print('Grade Result = 1')
else:
    print('Grade Result = 0')
