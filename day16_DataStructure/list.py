# Shopping Cart
cart = ['apple','banana','banana','orange']
cart.append('grapes')  # Add to end
print("After Append : ",cart) #output => ['apple', 'banana', 'banana', 'orange', 'grapes']

cart.insert(1, 'mango') # insert at index 1
print("After insert : ", cart)  #output => After insert :  ['apple', 'mango', 'banana', 'banana', 'orange', 'grapes']

cart.remove('banana')  # remove first banana by name
print("After remove : ", cart)  #output =>After remove :  ['apple', 'mango', 'banana', 'orange', 'grapes']

cart.pop() #remove last item
print("After pop : ", cart)  #output =>After pop :  ['apple', 'mango', 'banana', 'orange']

cart.sort() #sort alphabetically
print("After sort : ", cart)  #output =>After sort :  ['apple', 'banana', 'mango', 'orange']

cart.reverse()#reverse the list
print("After Reverse : ", cart)  #output =>After Reverse :  ['orange', 'mango', 'banana', 'apple']

print("count Of Banana : ",cart.count('banana')) #count the banana   #output => count Of Banana :  1

print("Index Of Orange : ",cart.index('orange')) # find index   #output => Index Of Orange :  0



# Playlist of Songs
playlist = ['song1','song2','song3']
playlist[1] =  'New_Song'    # Replace 2nd song
print(playlist)   #output =>['song1', 'New_Song', 'song3']

playlist.append("song4")  # add at End
print("after append :",playlist)   #output => after append : ['song1', 'New_Song', 'song3', 'song4']

playlist.extend(['song5','song6']) #add multiple songs
print("after extend : ", playlist)#output =>after extend :  ['song1', 'New_Song', 'song3', 'song4', 'song5', 'song6']

playlist.remove('song1')    #remove by name
print("after remove ; ",playlist)    #output =>after remove ;  ['New_Song', 'song3', 'song4', 'song5', 'song6']

last_song =playlist.pop()    # remove and return last
print("Popped Song : ",last_song)    #output =>Popped Song :  song6

print("final playlist: ",playlist)    #print list #output =>final playlist:  ['New_Song', 'song3', 'song4', 'song5']
