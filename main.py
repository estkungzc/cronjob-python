import schedule
import time
import logging
from typing import Any, Callable, List

from jobs import job_1, job_2
from utils import setup_logging

from threading import Thread


setup_logging()


def main() -> None:
    logging.info("[START] Running Cronjob...")

    # Scheduling your tasks
    my_jobs: List[Callable[..., Any]] = [job_1, job_2]
    for job in my_jobs:
        schedule.every(10).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
