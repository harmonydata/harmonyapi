"""
Scheduler contains a task that runs every 12th hour
"""

from fastapi.concurrency import run_in_threadpool
from rocketry import Rocketry
from rocketry.conds import cron

from services.instruments_cache import InstrumentsCache
from services.vectors_cache import VectorsCache

app = Rocketry(executation="async")


@app.task(cron("0 */12 * * *"))
async def do_every_12th_hour():
    """
    Save caches

    Runs at minute 0 past every 12th hour
    """

    try:
        await run_in_threadpool(InstrumentsCache().save)
    except (Exception,) as e:
        print(f"Could not save instruments cache: {str(e)}")

    try:
        await run_in_threadpool(VectorsCache().save)
    except (Exception,) as e:
        print(f"Could not save vectors cache: {str(e)}")
