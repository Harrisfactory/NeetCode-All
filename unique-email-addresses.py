class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        #we can ignore/strip out '.'
        #we remove anything after + locally

        fin_mails = {}

        for i in range(len(emails)):

            splimail = emails[i].split('@')

            clean_mail = splimail[0].replace('.','')

            clean_mail = clean_mail.partition('+')
            
            fin_mail = clean_mail[0]+ '@' + splimail[1]

            if fin_mail not in fin_mails:
                fin_mails[fin_mail] = 1
            else:
                continue


        
        return len(fin_mails)