
f = open('sherlock.txt', 'r')
#print f 
sherlock_content=f.read()
#print sherlock_content

sherlock_dict = {} 
#print sherlock_dict
sherlock_word_list=[]
#print sherlock_word_list

sherlock_word_list = sherlock_content.split()

#print sherlock_word_list [0:10]
input_list = sherlock_word_list #[0:10]
#list_len=len(sherlock_word_list)
#print list_len
#print len(input_list)
#print input_list

def find_bigrams(input_list):
  bigram_list = []
  for i in range(len(input_list)-2):
    #print i 
    bigram_list.append((input_list[i], input_list[i+1]))
  return bigram_list 

def find_vals(input_list):
  val_list=[]
  for i in range(len(input_list)-2):
    #print i   
    val_list.append(input_list[i+2])
  return val_list

b_list=find_bigrams(input_list)
#print b_list, len(b_list)
v_list=find_vals(input_list)
#print v_list, len(v_list)

sherlock_dict= dict(zip(b_list, v_list))
print sherlock_dict