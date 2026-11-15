import asyncio

async def secure_data(podaci):
    await asyncio.sleep(3)
    return {
        'prezime': podaci['prezime'],
        'broj_kartice': str(hash(podaci['broj_kartice'])),
        'CVV': str(hash(podaci['CVV'])),
    }

async def main():
    lista_podataka = [
        {'prezime': 'Horvat', 'broj_kartice': '4111111111111111', 'CVV': '123'},
        {'prezime': 'Novak', 'broj_kartice': '5500000000000004', 'CVV': '456'},
        {'prezime': 'Kovačević', 'broj_kartice': '340000000000009', 'CVV': '789'},
    ]
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in lista_podataka]
    rezultati = await asyncio.gather(*zadaci)
    for rezultat in rezultati:
        print(rezultat)

asyncio.run(main())