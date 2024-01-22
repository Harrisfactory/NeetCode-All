class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:


        unique_emails = []

        for email in emails:
            email = email.split('@')
            username = email[0]
            domain = email[1]
            #clean username
            non_extended_username = username.split('+')[0]
            non_extended_username = non_extended_username.replace('.','')
            cleaned_email = non_extended_username + '@' + domain
            if cleaned_email not in unique_emails:
                unique_emails.append(cleaned_email)
        
        return len(unique_emails)
        
