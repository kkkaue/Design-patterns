from developer_expression import DeveloperExpression
from team_lead_expression import TeamLeadExpression
from accounting_expression import AccountingExpression
from context import Context


class JobManager:
    @staticmethod
    def create_expression_tree(formula: str):
        tree = []
        for role in formula:
            if role.lower() == 'd':
                tree.append(DeveloperExpression())
            elif role.lower() == 'c':
                tree.append(AccountingExpression())
            elif role.lower() == 'l':
                tree.append(TeamLeadExpression())
            else:
                print(role)
                raise Exception("Unexpected role!")
        return tree

    def run_expression(self, context: Context):
        for expression in self.create_expression_tree(context.formula):
            expression.interpret(context)