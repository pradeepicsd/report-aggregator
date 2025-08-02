import pandas as pd

class CABFormatter:
    def format(self, df: pd.DataFrame) -> pd.DataFrame:
        cab_df = pd.DataFrame()
        cab_df["account_id"] = df["lineItem/UsageAccountId"]
        cab_df["service"] = df["product/ProductName"]
        cab_df["usage_type"] = df["lineItem/UsageType"]
        cab_df["cost"] = df["lineItem/UnblendedCost"]
        cab_df["start_time"] = df["lineItem/UsageStartDate"]
        cab_df["end_time"] = df["lineItem/UsageEndDate"]
        return cab_df

    def save(self, df: pd.DataFrame, path: str):
        df.to_csv(path, index=False)
        return path
