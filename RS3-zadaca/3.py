import asyncio

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'},
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'},
]


async def autorizacija(korisnik_iz_baze, lozinka):
    # Simulacija dekripcije i provjere lozinke
    await asyncio.sleep(2)
    lozinka_iz_baze = next(
        (zapis['lozinka'] for zapis in baza_lozinka
         if zapis['korisnicko_ime'] == korisnik_iz_baze['korisnicko_ime']),
        None
    )
    korisnik = korisnik_iz_baze['korisnicko_ime']
    if lozinka == lozinka_iz_baze:
        return f"Korisnik {korisnik}: Autorizacija uspješna."
    return f"Korisnik {korisnik}: Autorizacija neuspješna."


async def autentifikacija(korisnik):
    # Simulacija upita prema bazi podataka u Cloudu
    await asyncio.sleep(3)
    korisnicko_ime = korisnik['korisnicko_ime']

    pronaden = next(
        (zapis for zapis in baza_korisnika
         if zapis['korisnicko_ime'] == korisnicko_ime
         and zapis['email'] == korisnik['email']),
        None
    )

    if pronaden is None:
        return f"Korisnik {korisnicko_ime} nije pronađen."

    return await autorizacija(pronaden, korisnik['lozinka'])


async def main():
    korisnik = {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'lozinka123',
    }
    rezultat = await autentifikacija(korisnik)
    print(rezultat)


asyncio.run(main())