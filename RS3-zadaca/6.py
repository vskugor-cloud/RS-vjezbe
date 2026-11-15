import asyncio
import time

async def fetch_data(param):
    print(f"Nešto radim s {param}...")
    await asyncio.sleep(param)
    print(f"Dovršio sam s {param}.")
    return f"Rezultat za {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))  # schedule
    task2 = asyncio.create_task(fetch_data(2))  #schedule

    result1 = await task1
    print("Fetch 1 uspješno završen.")

    # Dok main čeka task1, event loop izvršava i task2.
    # Ako main završi odmah, task2 bi bio otkazan, pa ga čekamo
    # samo pasivno kroz sleep, bez await task2.
    await asyncio.sleep(1.5)

    return [result1]

t1 = time.perf_counter()
results = asyncio.run(main()) # pokretanje event loop-a
t2 = time.perf_counter()
print(results)
print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")