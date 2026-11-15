import asyncio
import random

async def dohvati_korisnike(vrijeme):
    await asyncio.sleep(vrijeme)
    return [
        {"id": 1, "ime": "Ana", "email": "ana@example.com"},
        {"id": 2, "ime": "Marko", "email": "marko@example.com"},
        {"id": 3, "ime": "Ivana", "email": "ivana@example.com"},
    ]

async def dohvati_proizvode(vrijeme):
    await asyncio.sleep(vrijeme)
    return [
        {"id": 101, "naziv": "Laptop", "cijena": random.randint(500, 1500)},
        {"id": 102, "naziv": "Miš", "cijena": random.randint(10, 50)},
        {"id": 103, "naziv": "Tipkovnica", "cijena": random.randint(20, 100)},
    ]

async def main():
    korisnici, proizvodi = await asyncio.gather(
        dohvati_korisnike(3),
        dohvati_proizvode(5),
    )

    print("Korisnici:")
    for korisnik in korisnici:
        print(korisnik)

    print("Proizvodi:")
    for proizvod in proizvodi:
        print(proizvod)

asyncio.run(main())