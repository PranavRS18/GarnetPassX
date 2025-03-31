import cv2
import numpy as np
import matplotlib.pyplot as plt

sig = cv2.imread("signature.jpg", cv2.IMREAD_GRAYSCALE)
form = cv2.imread("hostel_signout_form.jpg", cv2.IMREAD_GRAYSCALE)

_, sig = cv2.threshold(sig, 200, 255, cv2.THRESH_BINARY)
aspect_ratio = sig.shape[1] / sig.shape[0]

sig = cv2.resize(sig, (300, int(300 / aspect_ratio)), cv2.INTER_LANCZOS4)

X, Y = 125, 1130

sig_img = np.ones(form.shape) * 255
sig_img = np.astype(sig_img, np.uint8)
sig_img[Y : Y + sig.shape[0], X : X + sig.shape[1]] = sig
display(sig_img)

out = cv2.bitwise_and(form, form, mask = sig_img)

#Department Dictionary
dept = {
    "102" : "Chemical Engineering",
    "106" : "CSE",
    "103" : "Civil Engineering",
    "108" : "ECE",
    "110" : "ICE",
    "107" : "EEE",
    "111" : "Mechanical Engineering",
    "112" : "MME",
    "114" : "Production Engineering",
    "101" : "Architecture"
}

date = input("Enter Today's Date: ")
name = input("Enter your Name : ")
admn = str(int(input("Enter your Roll Number: ")))
course = dept[admn[:3]]
room = input("Enter Hostel and Room Number: ")
dest = input("Enter Destination: ")
purpose = input("Enter Purpose of Visit: ")
carry = input("Belongings during Travel: ")
approved = input("Whether Approved by Parents? ")
phno = input("Student's Phone Number: ")
par_phno =input("Parent's Phone Number: ")
fr_date = input("Enter From Date: ")
days = int(input("Enter Number of Days: "))
to_date = input("Enter To Date: ")

cv2.putText(out, date, (955, 200), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, name, (520, 260), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, admn, (520, 325), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.line(out, (635, 365), (1100, 365), (0, 0, 0), 1, cv2.LINE_8)
cv2.line(out, (510, 405), (1070, 405), (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, course, (670, 465), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, room, (520, 520), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, dest, (520, 575), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, purpose, (520, 630), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, carry, (520, 685), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, approved, (520, 742), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, phno, (700, 790), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, par_phno, (700, 870), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, fr_date, (590, 940), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, to_date, (860, 940), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)
cv2.putText(out, str(days), (860, 1010), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 0, 0), 1, cv2.LINE_8)

cv2.imwrite("out.jpg", out)
