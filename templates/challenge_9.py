def checkflag(flag):

    
    f=flag[:5]
   
    l=flag[5:11]    
    l_list=[]
    for l_i in l:
       
        l_i=ord(l_i)+5
        l_i=chr(l_i)
        l_list.append(l_i)
    l="".join(l_list)
    
    a_list=[]
    a=flag[11:16]   
    for aj in a:
        aj=hex(ord(aj))
        if len(aj)==1:
            aj='0'+aj            
        a_list.append(aj)        
    a="".join(a_list)

    g=flag[16:25] 
    g_list=[]
    for index,gk in enumerate(g):
        if index % 2 ==0:          
            gk = ord(gk) ^ 7
            gk=chr(gk)
            g_list.append(gk)

        else:
            g_list.append(gk)
    g="".join(g_list)
    return '0x650x2d0x450x6e0x67FLAG{nnbeuiigzWj{jwx'


