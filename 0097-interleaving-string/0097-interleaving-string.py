class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def is_interleaving(s1_pos, s2_pos, s3_pos):
            if (s1_pos, s2_pos, s3_pos) in dp:
                return dp[(s1_pos, s2_pos, s3_pos)]
            #print(s1_pos, s2_pos, s3_pos)
            if s1_pos>=len(s1) or s2_pos>=len(s2) or s3_pos>=len(s3):
                    print(s1[s1_pos:], s2[s2_pos:], s3[s3_pos:])
                    if (s2_pos <len(s2) and s2[s2_pos:] == s3[s3_pos:]) or (s1_pos <len(s1) and s1[s1_pos:] == s3[s3_pos:]) or  (s3_pos==len(s3) and s2_pos >=len(s2) and s1_pos >=len(s1)):
                        return True
                    else:
                        return False
                
                #return False


            is_possible = False
            if s1[s1_pos] == s3[s3_pos]:
                is_possible = is_possible or is_interleaving(s1_pos+1, s2_pos, s3_pos+1)

            if s2[s2_pos] == s3[s3_pos]:
                is_possible = is_possible or is_interleaving(s1_pos, s2_pos+1, s3_pos+1)
            dp[(s1_pos, s2_pos, s3_pos)] = is_possible
            return is_possible 


        return is_interleaving(0, 0, 0)