# Draw the following pattern by taking n number of rows as input from the user:

#         * * * * * * * * * 
#          * * * * * * * *
#            * * * * * *
#             * * * * *
#              * * * *
#               * * *
#                * *
#                 *
n=int(input())
for i in range(0,n):
	print(" "*i,end="")
	for j in range(1,((n-i)-1)+1):
		print("*", end=" ")
	print()