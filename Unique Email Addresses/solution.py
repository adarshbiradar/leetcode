class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        lst = []
        for mail in emails:
            extension = mail[mail.index("@"):]
            starting = mail[:mail.index("@")]   
            starting = starting.replace(".","")
            try :
                starting = starting[:starting.index("+")]
            except:
                pass
            lst.append(starting+extension)
        lst = set(lst)
        return len(lst)
