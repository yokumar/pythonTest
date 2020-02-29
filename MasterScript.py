'''
Created on 29-Feb-2020

@author: Yogesh
'''
from lib2to3.pgen2.token import OP
create_all_table ="CREATE ALL TABlES"
create_all_stored_proc ="CREATE ALL STORED PROCEDURES"
replicate_schema ="REPLICATE SCHEMA"

optionMap = {
  "1": create_all_table,
  "2": create_all_stored_proc,
  "3": replicate_schema
}


def fun_replicate_schema():
    print('========= REPLICATION OF SCHEMA STARTS ============')
    
##---------------------------------------------------------------------##


if __name__ == "__main__":
    print('================= SCRIPT STARTS===============')
    print('')
    print('Please Choose options  number from below List: ')
    
for x, y in optionMap.items():
    print(x,y)

print('')

option = input("Enter your Option :")

if option in optionMap:
    usrInput=optionMap[option];
    print('you have Chosen to : '+ usrInput)
    if (usrInput == replicate_schema):
        fun_replicate_schema();
    elif usrInput == create_all_table:
        print('Fuction to be written for the create all tables ')
    elif usrInput == create_all_stored_proc:
        print('Fuction to be written for the create all procedures ')
else:
    print('======  WRONG SELECTION ========')

