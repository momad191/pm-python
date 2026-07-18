from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a simple mathematical expression.
    """

    try:
        result = eval(expression)

        return str(result)

    except Exception as ex:
        return f"Error: {ex}"