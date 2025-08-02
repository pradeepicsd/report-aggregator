import pandas as pd

class ReportParser:
    def parse(self, filepath: str) -> pd.DataFrame:
        return pd.read_csv(filepath)
