import asyncio 

async def dohvati_podatke():
    await asyncio.sleep(3);
    podaci = [broj for broj in range (1,11)]
    print ("Podaci dohvaćeni")
    return podaci

async def main():
    podaci = await dohvati_podatke()
    print (podaci)

asyncio.run (main())