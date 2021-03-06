from commands.command import Command
from fbchat import Message
from fbchat import Mention

class a_chance_at_uni(Command):

    def run(self):
        if len(self.user_params) > 0:
            uni = " ".join(self.user_params)
            response_text = "@" + self.author.first_name + "\nu op guaranteed acceptance at " + uni
        else:
            response_text = "@" + self.author.first_name + "\nu op guaranteed acceptance at HYPSM"
        mentions = [Mention(self.author_id, length=len(self.author.first_name) + 1)]

        self.client.send(
            Message(text=response_text, mentions=mentions),
            thread_id=self.thread_id,
            thread_type=self.thread_type
        )

    def define_documentation(self):
        self.documentation = {
            "parameters": "UNIVERSITY_NAME (OPTIONAL)",
            "function": "Reminds you that you're good enough."
        }
