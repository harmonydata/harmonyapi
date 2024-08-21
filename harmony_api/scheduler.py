"""
MIT License

Copyright (c) 2023 Ulster University (https://www.ulster.ac.uk).
Project: Harmony (https://harmonydata.ac.uk)
Maintainer: Thomas Wood (https://fastdatascience.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor

from harmony_api.services.instruments_cache import InstrumentsCache
from harmony_api.services.vectors_cache import VectorsCache

# Jobstores
jobstores = {
    "default": MemoryJobStore()
}

# Executors
executors = {
    "default": ThreadPoolExecutor(),
}

scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, timezone="UTC")


@scheduler.scheduled_job(
    trigger="cron", max_instances=1, year="*", month="*", day="*", hour="*/12", minute="0", second="0"
)
def do_every_12th_hour():
    """
    Save the caches to disk.

    Runs at minute 0 past every 12th hour.
    """

    # Save instruments cache to disk
    try:
        InstrumentsCache().save()
    except (Exception,) as e:
        print(f"Could not save instruments cache: {str(e)}.")

    # Save vectors cache to disk
    try:
        VectorsCache().save()
    except (Exception,) as e:
        print(f"Could not save vectors cache: {str(e)}.")
