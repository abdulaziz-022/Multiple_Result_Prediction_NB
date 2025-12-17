from click import password_option
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Features:[no of Subjects,Houurs,Attendence%,PREVIOUS RESULT]
#Result =[1=pass,0=fail]

# dataset
X =[
    [1,50,0], #MATHS FAIL
    [3,70,1], #MATHS PASS
    [1,50,0], #PHYSICS FAIL
    [2,70,1],#PHYSICS PASS
    [1,50,0],#CHEMISTRY FAIL
    [3,60,1],#CHEMISTRY PASS
    [1,30,0],#ENGLISH FAIL
    [1,70,1],#ENGLISH PASS
    [2,10,0],#HINDI FAIL
    [2,65,1]#HINDI PASS
]

y = [
    0,  # Fail
    1,  # Pass
    0,  # Fail
    1,  # Pass
    0,  # Fail
    1,  # Pass
    0,  # Fail
    1,  # Pass
    0,  # Fail
    1   # Pass
]


#FOR TRANING TEST FOR EACH SUBJECT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=101
)

#MODEL TRANING
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_test, y_pred))


#NEW STUDENT DATA
#SUBJECT,HOURS,ATTENDENCE%,PREVIOUS RESULT
new_student_MATHS =[2,60,1]
new_student_PHYSICS =[2,60,0]
new_student_chemistry =[2,60,1]
new_student_english =[1,70,1]
new_student_hindi =[1,45,0]



#PREDICTION
print(new_student_MATHS)
if model.predict([new_student_MATHS])[0] ==1 :
    print("pass")
else:
    print("fail")
print(new_student_PHYSICS)
if model.predict([new_student_PHYSICS])[0] ==1 :
    print("pass")
else:
    print("fail")
print(new_student_chemistry)
if model.predict([new_student_chemistry])[0] ==1 :
    print("pass")
else:
    print("fail")
print(new_student_english)
if model.predict([new_student_english])[0] ==1 :
    print("pass")
else:
    print("fail")
print(new_student_hindi)
if model.predict([new_student_hindi])[0] ==1 :
    print("pass")
else:
    print("fail")



