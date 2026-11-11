from datetime import datetime, time, timedelta, timezone
from zoneinfo import ZoneInfo, available_timezones
from pydantic import BaseModel


def iso_str_now(exclude_microseconds: bool = True, with_timezone: bool = False) -> str:
    """
    获取当前时间的 ISO 格式字符串
    :param exclude_microseconds: 是否排除毫秒
    :return: ISO 格式字符串
    """
    if exclude_microseconds:
        # return datetime.now().astimezone().replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%S%z")
        # return datetime.now().astimezone().replace(microsecond=0).isoformat()
        return datetime.now().astimezone().isoformat(timespec="seconds")  # recommended
        return datetime.now().isoformat(timespec="seconds")

    if with_timezone:
        return datetime.now().astimezone().isoformat(timespec="seconds")

    return datetime.now().isoformat()


def handle_common_datetime():
    today_start = datetime.combine(datetime.now().date(), time.min)
    print(today_start)


def get_now_iso_8601():
    print(datetime.now(tz=timezone(timedelta(hours=8))))  # UTC+8
    print(datetime.now(tz=timezone(timedelta(hours=-8))))  # UTC-8
    print(datetime.now(timezone.utc))
    print(datetime.now(ZoneInfo('Asia/Shanghai')))
    return datetime.now(timezone.utc)


class Model(BaseModel):
    date: datetime


if __name__ == "__main__":
    # print(iso_str_now(exclude_microseconds=True))
    # print(available_timezones())
    # get_now_iso_8601()
    m = Model(date=datetime.now(timezone.utc).astimezone())
    print(m.model_dump_json())
    print(m.date)
    m = Model(date=datetime.now(timezone.utc))
    print(m.model_dump_json())
    print(m.date)
    m = Model(date=datetime.now(timezone.utc))
    print(m.model_dump_json())
    print(m.date)
    m = Model(date=datetime.now().astimezone())
    print(m.model_dump_json())
    print(m.date)

    # handle_common_datetime()
