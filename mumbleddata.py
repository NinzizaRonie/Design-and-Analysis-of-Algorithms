mumbled_data = [["KATUKUNDA Rochelle","NAJJOBA Tracy","MUGANGA Charles","NKATA Joshua Luyombya","MUKISA Isaiah"],
["A94169","A96447","A95681","A94161","A94160"],
["S21B23/016","S21B23/008","J22B23/032","S21B23/007","S21B23/034"],
["Afghanistan",93],
["Tiji",679],["Bahamas","1-242"],["Tanzania",255],
["Saint Vincent and the Grenadines","1-784"],["Ukraine",380]]

def search(list, n):
 
    for i in list:#sub-lists in the entire list
        for j in i:#items in each sub-list
            if n == j:
                return i
    
    return "not found"

#linear search(mumbled_data,item)
print(search(mumbled_data,7))
print(search(mumbled_data,"A94160"))
print(search(mumbled_data,380))
print(search(mumbled_data,"Doe"))
