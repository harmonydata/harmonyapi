"""
Scheduler contains a task that runs every 12th hour
"""

from fastapi.concurrency import run_in_threadpool
from services.instruments_cache import InstrumentsCache
from rocketry import Rocketry
from rocketry.conds import cron

app = Rocketry(executation="async")


@app.task(cron("* * * * *"))
async def do_every_12th_hour():
    """
    Save cache to Azure Blob Storage

    Runs at minute 0 past every 12th hour
    """

    try:
        save = InstrumentsCache().save
        await run_in_threadpool(save)
    except (Exception,) as e:
        print(
            f"ERROR:\t  Scheduler could not save caches to Azure Blob Storage: {str(e)}"
        )
