#  Opera em expressões terminais na gramática.
#  Corresponde à classe TerminalExpression no diagrama UML.

from context import Context
from job_expression import JobExpressionInterface


class AccountingExpression(JobExpressionInterface):
  def interpret(self, context: Context):
    if "c" in context.formula.lower():
      context.total_point += 3000