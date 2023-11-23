sen="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book."""

def main():
    print("text_analysis".center(100))
    def count_sentence(sen):
        c_sen=0
        c_sen=len(sen.split("."))
        print(f"Count the sentence :{c_sen}\n")
        
    count_sentence(sen)


    def no_word(sen):

        n_word=sen.lower().replace(",","").replace("!","").replace("?","").replace(".","").split()

        l_word=len(n_word)
        print(f"Number of words are {l_word}\n")
    no_word(sen)

    def comm_word(sen):
        c_word={}
        n_word=sen.lower().replace(",","").replace("!","").replace("?","").replace(".","").split()
        for i in n_word:
            
            c_word[i]=c_word.get(i,0)+1
        
        c_word=(sorted(c_word.items(),key=lambda y: y[1],reverse=True))[0:5]
        c_word=dict((x,y) for x,y in c_word)
        print("Top 5 Common words are:\n")
        
        for i,j in c_word.items():
            print(f"{i}".ljust(7),f"-".ljust(3),f"{j}")
    
    comm_word(sen)
main()

                
    


