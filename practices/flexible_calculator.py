#EACP1
import statistics as s
import time as t
print("""Welcome to the Flexible Calculator comerade
Available operations are: sum, average, product""")
operation = input("Which operation would you like to perform?: ").lower().strip()
print(" ")
nums1 = int(input("""Enter numbers
Number: """))
nums2 = int(input("Number: "))
nums3 = int(input("Number: "))
nums4 = int(input("Number: "))
nums5 = int(input("Number: "))
nums = (nums1,+ nums2, + nums3, + nums4, +nums5)
if operation == "average":
  print (f"answer is {s.mean(nums)}")
  

elif operation == "product":
  print (nums1*nums2*nums3*nums4*nums5)
    
elif operation == "sum":
  print (nums1,+ nums2, + nums3, + nums4, +nums5)



