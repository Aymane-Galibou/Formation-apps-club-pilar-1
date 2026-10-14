from abc import ABC, abstractmethod


# 1. ABSTRACT BASE CLASS (Contract Definition)
class PipelineStep(ABC):

    @abstractmethod
    def run(self, data: list[dict]) -> list[dict]:
        """Transforms and returns the dataset."""
        pass


# 2. CONCRETE PIPELINE STEPS
class DropNulls(PipelineStep):

    def run(self, data: list[dict]) -> list[dict]:
        """Removes any row containing missing/None values."""
        return [
            row
            for row in data
            if all(val is not None and val != "" for val in row.values())
        ]


class StandardizeText(PipelineStep):

    def __init__(self, column: str):
        self.column = column

    def run(self, data: list[dict]) -> list[dict]:
        """Strips whitespace and converts text column to UPPERCASE."""
        for row in data:
            if self.column in row and isinstance(row[self.column], str):
                row[self.column] = row[self.column].strip().upper()
        return data


class ClipOutliers(PipelineStep):

    def __init__(self, column: str, min_val: float, max_val: float):
        self.column = column
        self.min_val = min_val
        self.max_val = max_val

    def run(self, data: list[dict]) -> list[dict]:
        """Clips numeric values within specified min/max bounds."""
        for row in data:
            if self.column in row and isinstance(
                row[self.column], (int, float)
            ):
                row[self.column] = max(
                    self.min_val, min(row[self.column], self.max_val)
                )
        return data


class AddDerivedFeature(PipelineStep):

    def __init__(
        self, source_col: str, target_col: str, transform_fn
    ):
        self.source_col = source_col
        self.target_col = target_col
        self.transform_fn = transform_fn

    def run(self, data: list[dict]) -> list[dict]:
        """Creates a new column based on a custom calculation."""
        for row in data:
            if self.source_col in row:
                row[self.target_col] = self.transform_fn(row[self.source_col])
        return data


# 3. PIPELINE ORCHESTRATOR
class Pipeline:

    def __init__(self, steps: list[PipelineStep]):
        self.steps = steps

    def run(self, data: list[dict]) -> list[dict]:
        """Sequentially executes all steps in order."""
        for step in self.steps:
            data = step.run(data)
        return data


# --- EXECUTION EXAMPLE ---

raw_data = [
    {"name": " alice ", "city": "casablanca", "salary": 12000, "status": "active"},
    {"name": "bob", "city": None, "salary": 5000, "status": "pending"},
    {"name": "charlie", "city": "rabat", "salary": 150000, "status": ""},
    {"name": "david","city": "marrakech ","salary": 35000,"status": "active",},
]

# Build sequence of steps using specialized classes
data_pipeline = Pipeline(
    [
        DropNulls(),
        StandardizeText(column="city"),
        ClipOutliers(column="salary", min_val=0, max_val=50000),
        AddDerivedFeature(
            source_col="salary",
            target_col="tax",
            transform_fn=lambda s: s * 0.2,
        ),
    ]
)

clean_data = data_pipeline.run(raw_data)
print(clean_data)