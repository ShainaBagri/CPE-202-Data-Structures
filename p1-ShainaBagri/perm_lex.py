# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):

    #Base case accounting for empty string
    if len(str_in)==0:
        return []

    #Base case when string gets narrowed down to 1 character
    elif len(str_in)==1:
        return [str_in]

    #Recursion section
    else:
        ans = []
        for i in range(len(str_in)):
            #Removes a letter from string
            letter = str_in[i]
            #Recombines string to form a new string without the removed letter
            news = str_in[:i] + str_in[i+1:]
            #Recursion with the new string
            x = perm_gen_lex(news)
            for j in range(len(x)):
                #Adds removed letter to front of string and appends new permutation to list of permutations
               ans.append(letter + x[j])
        return ans
