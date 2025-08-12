###day-21
import math
from collections import Counter
from typing import List, Tuple
import typing


##exercice-1


class StatsData:
    def __init__(self, data: List[int]):
        self.data = data

    def count(self) -> int:
        return len(self.data)

    def sum(self) -> int:
        return sum(self.data)

    def min(self) -> int:
        return min(self.data)

    def max(self) -> int:
        return max(self.data)

    def range(self) -> int:
        return self.max() - self.min()

    def mean(self) -> float:
        return self.sum() / self.count()

    def median(self) -> float:
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self) -> Tuple[int, int]:
        counter = Counter(self.data)
        most_common = counter.most_common(1)[0]
        return most_common

    def var(self) -> float:
        mean_val = self.mean()
        squared_diff = [(x - mean_val) ** 2 for x in self.data]
        return round(sum(squared_diff) / len(self.data), 1)

    def std(self) -> float:
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self) -> List[Tuple[float, int]]:
        counter = Counter(self.data)
        total = len(self.data)
        freq = [
            (round(count / total * 100, 1), value) for value, count in counter.items()
        ]
        return sorted(freq, reverse=True)

    def describe(self) -> str:
        """Returns a string with all statistical measures of the dataset"""
        mode_value, mode_count = self.mode()
        result = [
            f"Count: {self.count()}",
            f"Sum: {self.sum()}",
            f"Min: {self.min()}",
            f"Max: {self.max()}",
            f"Range: {self.range()}",
            f"Mean: {self.mean()}",
            f"Median: {self.median()}",
            f"Mode: ({mode_value}, {mode_count})",
            f"Variance: {self.var()}",
            f"Standard Deviation: {self.std()}",
            f"Frequency Distribution: {self.freq_dist()}",
        ]
        return "\n".join(result)


age = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]
data = StatsData(age)
print("Count:", data.count())
print("Sum: ", data.sum())
print("Min: ", data.min())
print("Max: ", data.max())
print("Range: ", data.range())
print("Mean: ", data.mean())
print("Median: ", data.median())
print("Mode: ", data.mode())
print("Standard Deviation: ", data.std())
print("Variance: ", data.var())
print("Frequency Distribution: ", data.freq_dist())


print("\nSummary Statistics:")
print(data.describe())
##exercice-2


# typedict add consistency to the data,
# it ensure that your dict will always have key & values you are lookig for
# namedtuple can also be used here
class OperationType(typing.TypedDict):
    description: str
    amount: float


class PersonAccount:
    def __init__(
        self,
        firstname: str,
        lastname: str,
        incomes: list[OperationType],
        expenses: list[OperationType],
    ) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
        pass

    def add_income(self, amount: float, description: str) -> None:
        self.incomes.append({"description": description, "amount": amount})

    def add_expense(self, amount: float, description: str) -> None:
        self.expenses.append({"description": description, "amount": amount})

    def total_income(self) -> float:
        return sum([income.get("amount") for income in self.incomes])

    def total_expense(self) -> float:
        return sum([expense.get("amount") for expense in self.expenses])

    def account_balance(self) -> float:
        return self.total_income() - self.total_expense()

    def account_info(self) -> str:
        infos = [
            f"Account of {self.firstname} {self.lastname}",
            f"Total Income: ${self.total_income():.2f}",
            f"Total Expenses: ${self.total_expense():.2f}",
            f"Balance: ${self.account_balance():.2f}",
        ]

        infos.append("\nIncome Details:")
        for income in self.incomes:
            infos.append(f"- ${income['amount']:.2f}: {income['description']}")

        infos.append("\nExpense Details:")
        for expense in self.expenses:
            infos.append(f"- ${expense['amount']:.2f}: {expense['description']}")

        return "\n".join(infos)


account = PersonAccount(
    "son",
    "gohan",
    incomes=[
        OperationType(description="Reward", amount=90),
        OperationType(description="gift from father", amount=200),
    ],
    expenses=[
        OperationType(description="buy joystick", amount=47),
        OperationType(description="buy computer", amount=27),
    ],
)
account.add_income(30, "gift from mother")
account.add_expense(40, "renewing my setup")
print(account.account_info())
