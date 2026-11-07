"""用两个 UNRATE 初值演示日级发布时间与预测截点的关系。"""

from datetime import date, datetime, time, timedelta, timezone

UTC = timezone.utc
CUTOFF = datetime(2023, 1, 15, 23, tzinfo=UTC)
OBSERVATIONS = [
    ("2022-12", "3.5%", date(2023, 1, 6)),
    ("2023-01", "3.4%", date(2023, 2, 3)),
]


def release_status(release_date: date, cutoff: datetime) -> str:
    """只有发布日期时，用 UTC−12 到 UTC+14 的民用时区覆盖可能时刻。"""
    if cutoff.utcoffset() is None:
        raise ValueError("cutoff 必须包含时区")
    midnight = datetime.combine(release_date, time.min, UTC)
    earliest = midnight - timedelta(hours=14)
    upper_exclusive = midnight + timedelta(days=1, hours=12)
    if upper_exclusive <= cutoff:
        return "BEFORE_CUTOFF"
    if earliest > cutoff:
        return "AFTER_CUTOFF"
    return "INDETERMINATE"


if __name__ == "__main__":
    for reference_month, initial_value, release_date in OBSERVATIONS:
        print(f"{reference_month}  {initial_value}  {release_status(release_date, CUTOFF)}")
