
#---------- List Example -------------


list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 4th 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists


list.extend(["new_item",1,4.6]);
list.append("Hello");
list.append([1,3,4])

tinylist[0] = "Surya"
tinylist.insert(0,1233333L)
tinylist.insert(0,"ek aur")

print tinylist;

print "\n\n\n"
print list;
del list[2];
print list;

print "\n\n"
# print len(list);
# print cmp(list,tinylist)
# print min(tinylist);

# print sorted(list)


aStringList = [ 'john','abcd', 'new_item','Hello'];
aStringList.sort();
# list.reverse();
print aStringList


# value = list[1];
# print "\n\n\n"
# print value*2;