import re
import sys

class TweetCleaner:

    def clean_all(self, data):
        """
        Method utilizing all class methods, removing
        urls, emojis, special characters and usernames
        :param data:
        :return:
        """
        if not data:
            return data
        return self.remove_special_characters(
            self.remove_emojis(
                self.remove_urls(
                    self.remove_usernames(data)
                )
            )
        )

    def remove_emojis(self, data):
        """
        Method removing graphical 'emojis' from text
        :param data: Tweet message to process
        :return: Tweet cleared of all possible emojis
        """
        if not data:
            return data
        try:
            # UCS-4
            highpoints = re.compile(u'([\U00002600-\U000027BF])|([\U0001f300-\U0001f64F])|([\U0001f680-\U0001f6FF])')
        except re.error:
            # UCS-2
            highpoints = re.compile(
                u'([\u2600-\u27BF])|([\uD83C][\uDF00-\uDFFF])|([\uD83D][\uDC00-\uDE4F])|([\uD83D][\uDE80-\uDEFF])')

        return highpoints.sub(u'', data)

    def remove_urls(self, data):
        """
        Method removing Twitter-style user tags for example @user
        :param data: Tweet message to process
        :return: Tweet cleared of all user tags
        """
        if not data:
            return data
        return re.sub(r"http\S+", '', data, flags=re.MULTILINE)

    def remove_special_characters(self, data):
        """

        :param data: Tweet message to process
        :return: Tweet cleared of all defined unwanted characters
        """
        if not data:
            return data
        # TODO add or not to add '#'
        return re.sub("""[*:/\|`~;>"<+=_&'}{$^%@]""", '', data)

    def remove_usernames(self, data):
        """
        Method removing Twitter-style user tags for example @user
        :param data: Tweet message to process
        :return: Tweet cleared of all user tags
        """
        if not data:
            return data
        return re.sub('(\s)@\w+', '', data)

