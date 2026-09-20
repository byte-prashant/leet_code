class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        

        def get_line(line_len,line_words,maxWidth,is_last_line =False):
            if len(line_words)==1  or is_last_line:

                remaining = maxWidth-line_len
                fix_space = remaining/(len(line_words)-1) if len(line_words)>1 else 0
                extra_space = remaining%(len(line_words)-1) if len(line_words)>1 else remaining
                
                i = 0
                line_str = ""
                while i<len(line_words):
                    line_str+=line_words[i]
                    if  i < len(line_words)-1:
                        line_str+=" "* int(1)
                        remaining -=1
                    #line_str+=" "*int(fix_space)
                    i+=1

                if remaining>0:
                    line_str+= " "*int(remaining)

                

            else:
                remaining = maxWidth-line_len
                fix_space = int(remaining/(len(line_words)-1))
                extra_space = int(remaining%(len(line_words)-1))
                
                i = 0
                line_str = ""
                while i<len(line_words):
                    line_str+=line_words[i]
                    if  i < len(line_words)-1:
                        line_str+=" "* int(fix_space)
                    if extra_space>0:
                        line_str+=" "
                        extra_space-=1
                    i+=1

                    print(line_str,extra_space)
                
            return line_str
            
                
                   
                
        pos = 0
        lines = []
        while pos <len(words):

            line_start = pos
            line_len = 0
            spaces_req = maxWidth
            cur_space = 0
            line_words = []
            while line_start<len(words) and line_len+cur_space+len(words[line_start])<=maxWidth:

                cur_space+=1
              
                line_len +=len(words[line_start])
                line_words.append(words[line_start])
                line_start+=1

            is_last_line = False
            if  line_start>=len(words):
                is_last_line = True

            lines.append(get_line(line_len,line_words,maxWidth,is_last_line))

            pos = line_start

        return lines
                





        
        