class Solution:
    def interpret(self, command: str) -> str:
        output = command.replace('()', 'o').replace('(al)', 'al')
        return output