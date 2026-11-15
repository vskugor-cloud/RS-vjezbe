import asyncio
async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)
asyncio.run(main())

# 1. main() stvori tri taska, po jedan za svaki timer. Taskovi se samo stave u red za izvršvanje, pa se timeri još nisu počeli izvršavati. 
# 2. main() se pauzira s await asyncio.gather, a event loop preuzima kontrolu.
# 3. Event loop preuzima taskove redom. Svaki izvrši kod od prvog await, ispiše prvu poruku odbrojavanja i čeka / spava jednu sekundu, dok event loop prelazi na sljedeći task.
# 4. Nakon otprilike jedne sekunde sva tri taska se bude i ispisuju sljedeću poruku i ponovno čekaju. To se ponavlja, te Timer1 završava nakon 3 sekunde i ispisuje 
# vrijeme je isteklo, Timer2 u 5 sekundi i Timer3 u 7 sekundi. Kad je i zadnji task gotov, gather vraća rezultate, main() završava, a asyncio.run() zatvara event loop.
# Ukupno vrijeme izvršavanja je 7 sekunudi, jer se izvršavaju istovremeno. 